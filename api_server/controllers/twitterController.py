from models.twitterModel import TwitterModel
from flask import request

class TwitterController:
    def __init__(self, app):
        self.numbers = []
        self.twitterApi = TwitterModel()
        self.isConnect = False

        @app.route("/api/v1/getInfoTwitter", methods=['POST'])
        def getInfoTwitter():
            if not self.isConnect :
                self.isConnect = self.twitterApi.connect()

            if self.isConnect:
                #search
                reqData = request.get_json()
                return self.twitterApi.search(reqData["text"], reqData["geo"])
            else:
                return 'error to connect Twitter'
 
        
    

        