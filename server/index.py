from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/foo', methods=['POST']) 
def foo():
    if not request.json:
        abort(400)
    print request.json
    return json.dumps(request.json)
    
if __name__ == "__main__":
    app.run()