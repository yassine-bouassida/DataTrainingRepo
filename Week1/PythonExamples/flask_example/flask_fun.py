from flask import Flask, request

app: Flask = Flask(__name__) #this tells flask where to look for resources (name is reference to the module it resides in)

count = 0 

data_set = {"1":"some data"}

@app.route("/", methods = ["GET"])
def hello_world():
    return "Hello World"

#get request with path parameter
@app.route("/greeting/<name>",methods=["GET"])
def greeting(name:str):
    return f"Hello {name}"

@app.route("/<num1>/add/<num2>", methods = ["GET"])
def addition(num1:str, num2:str):
    result = int(num1) + int(num2)
    return str(result)

@app.route("/login", methods=["POST"])
def login():
    credentials = request.get_json() #sets out variable to the JSON dictionary values
    username = credentials["username"]
    password = credentials["password"]
    if username == "good" and password == "correct":
        return "your credentials are good"
    else:
        return "your credentials are bad!"
    
@app.route("/count",methods=["PUT"])
def add_count():
    global count
    count +=1
    return f"The count is now {count}"


app.run()