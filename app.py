from flask  import Flask,request,jsonify
from libs.Connection import Connection 
from libs.CleanString import CleanString 
import hashlib
import json

app =Flask(__name__)
app.config["SECRET_KEY"] = "password123"
#--------------home
@app.route("/",methods=["GET"])

def index():
    # obj = User("juan","jperez@loquesea.com")
    return "It's Working"
#--------------home

#------------ list
@app.route("/people",methods=["GET"])
def list():
    con = Connection()
    result = con.query("select * from user p")
    print(result)
    json1 =[]    
    for x in result:
        print(x)
        json1.append({
            "name":x[1],
            "email":x[2]
        })
    # return "result"
    return jsonify(json1)
#------------ list

#------------ auth
@app.route("/auth",methods=["PUT"])
def auth():
    print(request.json)
    email = request.json["email"]
    obj1 = CleanString(email)
    email = obj1.clear()
    password = request.json["password"]
    obj1 = CleanString(password)
    password = obj1.clear()
    result = hashlib.md5(password.encode())
    password = result.hexdigest()
    adr= (email,password)
    con = Connection()
    result = con.query("select * from user p where p.email = %s and p.password = %s" ,adr)
    key = result[0]    
    key1 = app.config["SECRET_KEY"] + key[3]
    result = hashlib.md5(key1.encode())
    key1 = result.hexdigest()
    rItem ={"key":key1}
    return jsonify(rItem)
#------------ auth
#------------ post message
@app.route("/message",methods=["POST"])
def test():
    header = request.headers
    json = request.json
    print(header)
    print(request.json)
    json1 = request.json
    key =header["key1"]
    if 'msg' in json1 and 'tag' in json1 and 'key1' in header and len(key) ==32:
        msg = json1["msg"]
        tag = json1["tag"]
        return request.json, 200
    else:
        return "bad request", 403

#------------ by id
@app.route("/id/<int:id>", methods=["GET"])
def busqueda(id):
    if id > 0:
        return "status success",200
#------------ by id

#------------ by id
@app.route("/tag/<param>", methods=["GET"])
def byTag(param):
    if param > "":
        return "status success",200
#------------ by id


if  __name__ == '__main__':
    app.run(debug = True)

