from datetime import datetime
from flask import Flask, render_template
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


@app.route('/')  # these are the end points from which we reach there
def hello_world():
    # return 'Hello, World!'
    todo = Todo(title = "First todo" , desc = "Statring todo")
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    print(allTodo)
    return render_template('index.html',allTodo=allTodo)
@app.route('/products')

def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return " this is the product page"
#--------- this is imp because if not present - the app will not work ---------
if __name__ == "__main__":
        with app.app_context():
            db.create_all()
    #app.run(debug=True)
        app.run(debug=True)
#--------------------------------------------------------------------------
