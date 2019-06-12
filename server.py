from flask import Flask, render_template, request, redirect, flash
from mysqlconn import connectToMySQL

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=['POST'])
def index2():
    mysql = connectToMySQL('mydb')
    query = "INSERT INTO email (email) VALUES (%(em)s);" 
    data = {
        "em": request.form["email"]
    }
    users= mysql.query_db(query,data)
    print(users)
    return redirect("/sucess")

@app.route("/sucess")
def index3():
    mysql = connectToMySQL('mydb')
    users = mysql.query_db('SELECT * FROM email;')
    print(users)
    return render_template("sucess.html", all_users=users)


            
if __name__ == "__main__":
    app.run(debug=True)
    