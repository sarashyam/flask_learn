from datetime import datetime
from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # to initialize the app
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)
    
    def __repr__(self) -> str: # to print the data in customized way
        return f"{self.sno} - {self.title}"


@app.route("/", methods=['GET','POST'])  # these are the end points from which we reach there
def hello_world():
    # return 'Hello, World!'
    if request.method == "POST":
        print(request.form['title1'])
        print(request.form['desc'])
        title = request.form['title1']
        descr = request.form['desc']
        print("Post")
        todo = Todo(title = title , desc = descr)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    #print(allTodo)
    return render_template('index.html',allTodo=allTodo)


@app.route('/show')
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return " this is the product page"

@app.route('/update/<int:sno>',methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        title = request.form['title1']
        descr = request.form['desc']
        print("Post")
        todo = Todo.query.filter_by(sno =sno).first()
        todo.title = title
        todo.desc = descr
        db.session.add(todo)
        db.session.commit()
    redirect("/")
        
    up_Todo = Todo.query.filter_by(sno =sno).first()
    # allTodo = Todo.query.all()
    # print(allTodo)
    return render_template('update.html',todo=up_Todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    del_Todo = Todo.query.filter_by(sno =sno).first()
    db.session.delete(del_Todo)
    db.session.commit()
    print(del_Todo)
    return redirect("/")


#--------- this is imp because if not present - the app will not work ---------
if __name__ == "__main__":
        with app.app_context():
            db.create_all()
    #app.run(debug=True)
        app.run(debug=True)
#--------------------------------------------------------------------------
