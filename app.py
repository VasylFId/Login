from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method =="GET":
       return render_template("index.html")
    else :
      user = request.form["user"]
      pas = request.form["pw"]
      if user == "bob"and pas == "123":
          return "hi bob"
      else:  
          return "user not verifeidl" 

@app.route("/signup" )
def signup():
   return "signup"
      
