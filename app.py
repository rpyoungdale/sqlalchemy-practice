from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/ryanyoungdale/python-projects/sqlalchemy-flask-practice/todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), unique=True, nullable=False)
    completed = db.Column(db.Boolean)

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/todos', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # from IPython import embed; embed()
        todos = Todo.query.all()
        # from IPython import embed; embed()
        return render_template('index.html', todos=todos)
    if request.method == 'POST':
        todo = Todo(content=request.form['todoitem'], completed=False)
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    # return render_template('index.html')

@app.route('/todos/new')
def new():
    return render_template('new.html')

@app.route('/edit/<int:id>')
def edit(id):
    todo = Todo.query.filter_by(id=id)[0]
    # from IPython import embed; embed()
    todo.completed = True
    db.session.commit()
    return redirect(url_for('index'))





if __name__ == '__main__':
    app.run(debug=True)
