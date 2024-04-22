from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def hello_world():
    user = request.args.get("user")
    pas = request.args.get("pw")
    if user == None:
      return render_template("index.html")
    elif user == "bob"and pas == "123":
       return "hi bob"
    else:  
      return "user not verifeid"
      
