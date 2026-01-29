from flask import Flask, request

app: Flask = Flask(__name__) #this tells flask where to look for resources (name is reference to the module it resides in)

count = 0 

data_set = {"1":"some data"}

@app.route("/", methods = ["GET"])
def hello_world():
    return "Hello World"

app.run()