
import tweepy
import redis
import json
from pymongo import MongoClient
from datetime import datetime
from datetime import timedelta

from configs.twitterConfig import radius, key, secret, accessToken, accessTokenSecret

from configs.redisConfig import redis_host, redis_port

from configs.mongoConfig import mongo_host, mongo_username, mongo_password, mongo_authSource
#import mongodb

class TwitterModel:

    def connect(self):  
        try:
            self.auth = tweepy.OAuthHandler(key, secret)
            self.auth.set_access_token(accessToken, accessTokenSecret)
            return True
        except tweepy.TweepError:
            #'Error! Failed to connect'
            return False

    def search(self, searchData, geo=''):
        r = redis.Redis(host=redis_host, port=redis_port)
       
        searchResult = ''
        if r.get(searchData):
            #print("have cash ", r.get(searchData).decode("utf-8"))
            searchResult = r.get(searchData).decode("utf-8")
        else:
            api = tweepy.API(self.auth)
            if geo == '': 
                result = api.search(searchData)
            else:
                temp = str(geo["lat"])+","+str(geo["lng"])+","+radius
                result = api.search(searchData, rpp=50,geocode=temp )

            if len(result) > 0:
                temp = []
                for target_list in result:
                    print("text => ",target_list._json['text'],"\n")
                    print("geo => ",target_list._json['geo'],"\n")
                    if target_list._json['geo'] is not None:
                        data = {
                            "text": target_list._json['text'],
                            "coordinates": target_list._json['geo']['coordinates'],
                        }
                        temp.append(data)

                print("====================================================================","\n")

                if len(temp) > 0:
                    searchResult = json.dumps(temp)
                    ttl = timedelta(hours=1)
                    r.setex(searchData, searchResult, ttl)

        #update to mongo
        client = MongoClient("mongodb://"+mongo_username+":"+mongo_password+"@"+mongo_host+"/"+mongo_authSource)
        db = client[mongo_authSource]
        search = db['search']
        search.update( {'textsearch': searchData}, { '$inc': { 'count': 1 } }, upsert=True)
        client.close()

        return searchResult
        
        