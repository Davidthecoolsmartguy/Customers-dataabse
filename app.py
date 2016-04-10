from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for, render_template,flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators , SubmitField,SelectField,TextAreaField
import datetime

timenow = datetime.datetime.now()
displaytimenow  = timenow.strftime("%m-%d-%y %H:%M")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/a/Desktop/flask_movie/test.db'
app.config['SECRET_KEY'] = 'super-secret'

app.debug = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False)
    last_name = db.Column(db.String(120), unique=False)
    phone = db.Column(db.String(120), unique=False)
    device = db.Column(db.String(120), unique=False)
    problem = db.Column(db.String(120), unique=False)
    checkin = db.Column(db.String(120), unique=False)
    checkout = db.Column(db.String(120), unique=False)
    datastate = db.Column(db.String(120), unique=False)
    def __init__(self, first_name,last_name,phone,device,problem,checkin,checkout,datastate):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.device = device
        self.problem = problem
        self.checkin = checkin
        self.checkout = checkout
        self.datastate = datastate
        #datastate is going to be check if it delted or not
    
    def __repr__(self):
        return '<User %r>' % self.first_name

class Userform(Form):
    first_name= TextField("First Name")
    last_name = TextField("Last name")
    phone = TextField("Phone")
    device =  SelectField(u'Type of device', choices=[('laptop', 'Laptop'), ('phone', 'Phone'), ('desktop', 'Desktop'),('software', 'Software'),('tablet', 'Tablet')])
    problem = TextAreaField('Problem')
    submit = SubmitField("ADD")




@app.route('/')
def index():
    form = Userform()
    return render_template('add_user.html',form = form)


@app.route('/add_customer', methods=['POST'])
def add_customer():
    problemhere = request.form['problem']
    if problemhere == '':
        problemhere = 'No probelm written'    
    user = User(first_name= request.form['first_name'], last_name =request.form['last_name'],phone=request.form['phone']\
    ,\
        device=request.form['device'],problem=request.form["problem"],checkin=displaytimenow ,checkout="", datastate=1
        )
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('active_tasks'))



# on get display information 
# If delete buttuon is press get id and delete it
# if invoice button is press pass
@app.route('/active_tasks',methods=['GET', 'POST'])
def active_tasks():
    user = User.query.filter_by(datastate=1)
    if request.method == 'POST':
        if "submit" in request.form:
            task_id = request.form.get("submit","")
            updatehere = User.query.filter_by(id=task_id).first()
            updatehere.datastate = 2
            db.session.commit()
            return redirect(url_for("pending_customers"))
        elif "delete" in request.form:
            task_id = request.form.get("delete","")
            updatehere = User.query.filter_by(id=task_id).first()
            updatehere.datastate = 99
            db.session.commit()
            return redirect(url_for("active_tasks"))
        else:
            return ("you should not be here")
            
            
    elif request.method == 'GET':
        return render_template('active_tasks.html', user=user)
        




# if invoice button is press pass
@app.route('/pending_customers',methods=['GET', 'POST'])
def pending_customers():
    user = User.query.filter_by(datastate=2)
    if request.method == 'POST':
        if "submit" in request.form:
            task_id = request.form.get("submit","")
            updatehere = User.query.filter_by(id=task_id).first()
            updatehere.datastate = 3
            db.session.commit()
            return redirect(url_for("paid_customers"))
        elif "delete" in request.form:
            task_id = request.form.get("delete","")
            updatehere = User.query.filter_by(id=task_id).first()
            updatehere.datastate = 99
            db.session.commit()
            return redirect(url_for("paid_customers"))
        else:
            return ("you should not be here")
            
    elif request.method == 'GET':
        return render_template('pending_customers.html', user=user)

@app.route('/paid_customers',methods=['GET', 'POST'])
def paid_customers():
    user = User.query.filter_by(datastate=3)
    if request.method == 'POST':
        if "submit" in request.form:
            task_id = request.form.get("submit","")
            updatehere = User.query.filter_by(id=task_id).first()
            updatehere.datastate = 3
            db.session.commit()
            return redirect(url_for("pending_customers"))
        elif "delete" in request.form:
            task_id = request.form.get("delete","")
            updatehere = User.query.filter_by(id=task_id).first()
            updatehere.datastate = 99
            db.session.commit()
            return redirect(url_for("paid_customers"))
        else:
            return ("you should not be here")
            
    elif request.method == 'GET':
        return render_template('paid_customers.html', user=user)

@app.route('/deleted_customers',methods=['GET', 'POST'])
def deleted_customers():
    user = User.query.filter_by(datastate=99)
    if request.method == 'POST':
        if "submit" in request.form:
            task_id = request.form.get("submit","")
            updatehere = User.query.filter_by(id=task_id).first()
            updatehere.datastate = 3
            db.session.commit()
            return redirect(url_for("deleted_customers"))
        elif "delete" in request.form:
            task_id = request.form.get("delete","")
            updatehere = User.query.filter_by(id=task_id).first()
            updatehere.delete(updatehere)
            db.session.commit()
            return redirect(url_for("deleted_customers"))
        else:
            return ("you should not be here")
            
    elif request.method == 'GET':
        return render_template('deleted_customers.html', user=user)




if __name__ == "__main__":
    app.run()