from controllers.twitterController import TwitterController
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app)
TwitterController(app)

@app.route("/")
def main():
    return "Welcome!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")