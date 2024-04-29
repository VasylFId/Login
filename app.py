from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method =="GET":
       return render_template("index.html")
    else :
        f = open("login.txt","r")
        user = f.readline().strip()
        pw = f.readline().strip()
        f.close()
        if user == request.form["user"] and pw == request.form["pw"]:
            return "Shalam " + user
        else :
            return "fail"
@app.route("/signup", methods=["GET","POST"])
def signup():
   if request.method == "GET" :
         return  render_template("signup.html")
   else :
        print(  request.form["user"])
        print(  request.form["pw"])  
        f = open("login.txt", "a")

        f.write(request.form["user"])
        f.write("\n")
        f.write(request.form["pw"])
        f.close()
        return "Signup is nice"
