from flask import Flask
from flask import render_template
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config['SQLA_DATABASE_URI'] = 'sqlite:////tmp/pizza.db'

# This avoids the notifications on terminal
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize the db
db = SQLAlchemy(app)

# create a model
class Pizza(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String, nullable = False)


      def __repr__(self):
        return '<Pizza %r>' % self.name




@app.route('/')
def  index():
   return render_template ('index.html')

@app.route('/about')
def about():
   return render_template ('about.html')

@app.route('/contact')
def contact():
   return render_template ('contact.html')

@app.route('/menu', methods=['POST','GET'])
def menu():
   if request.method == 'POST':
      pizzatype = request.form[' ']

   return render_template ('menu.html')

@app.route('/cart')
def cart():
   return render_template ('cart.html')