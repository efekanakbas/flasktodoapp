from flask import Flask,render_template,request,redirect,session,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form,StringField,PasswordField,validators
from passlib.hash import sha256_crypt

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/linko/Desktop/TodoApp/todo.db"
db=SQLAlchemy()
db.init_app(app)

class Kullanıcılar(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(80),unique=True)
    complete=db.Column(db.Boolean)

@app.route("/")
def home():
   todos=Kullanıcılar.query.all()
   return render_template("home.html",todos=todos)

@app.route("/add",methods=["POST"])
def add():
    title=request.form.get("title")
    user=Kullanıcılar(title=title,complete=False)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("home"))
@app.route("/update/<string:id>")
def update(id):
    todo=Kullanıcılar.query.filter_by(id=id).first()
    todo.complete=not todo.complete
    db.session.commit()
    return redirect(url_for("home"))
@app.route("/delete/<string:id>")
def sil(id):
    todo=Kullanıcılar.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


        
  




if __name__=="__main__":
    with app.app_context():    
        db.create_all()
    app.run(debug=True)