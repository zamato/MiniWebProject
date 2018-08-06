
import tweepy
#import redis
#import mongodb

class TwitterModel:

    def __init__(self):
        self.key = 'VBoot3MLru0J2eJUY8vbGkEx0'
        self.secret = 'L5S8ZFB4RXjcTSbFLGXrtidSZwNcU2q9OIdYeZmmIaSKcGQFBG'
        self.accessToken = '3182363612-NtDoSYYF4sMsEiEkcZmzGInPRbza26kq8aNoJLj'
        self.accessTokenSecret = 'h2sDYvAQuqJX0q2lypMFkxTeul3TuDNKkDT6hVPGz7oBN'
        
    def connect(self):  
        try:
            self.auth = tweepy.OAuthHandler(self.key, self.secret)
            self.auth.set_access_token(self.accessToken, self.accessTokenSecret)
            return True
        except tweepy.TweepError:
            #'Error! Failed to connect'
            return False

    def search(self, searchData, geo=''):
        api = tweepy.API(self.auth)
        if geo == '': 
            return api.search(searchData)
        else:
            temp = {
                'latitide': geo["lat"],
                'longitude': geo["lng"],
                'radius': '1 km'
            }
            return api.search(searchData, geocode = temp )

            

        #api.update_status('tweepy + oauth!')

        #update to mongo

        #update to radis