from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
#create model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'
#display all books in db
@app.route('/books')
def get_books():
    Books=Book.query.all()
    output=[]
    for book in Books:
        book_date={'name':book.name,'description':book.description}
        output.append(book_date)
    return {'books':output}
    #return {"id":"id data"}


"""
notes
terminal code
from "project name" import app, db
app.app_context().push()
db.create_all()
from "project name" import "class name"
"obj"="class name(all the db columns)"
db.session.add("class name")
db.session.commit()
"class name".query.all()
when adding more after first
db.session.add("class name"(all columns))
"""