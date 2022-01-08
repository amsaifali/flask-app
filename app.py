from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
# from PyQt5.QtCore import *
# from PyQt5.QtWebEngineWidgets import *
# from PyQt5.QtWidgets import QApplication
# from threading import Timer
# import sys

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_BINDS'] = {
    'database1': 'sqlite:///database1.db'
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

class admin(db.Model):
    aid = db.Column(db.Integer, primary_key=True)
    aname = db.Column(db.String(80))
    amail = db.Column(db.String(120))
    apassword = db.Column(db.String(80))

class Data(db.Model):
    __bind_key__ = 'database1'
    sno = db.Column(db.Integer, primary_key=True)
    storename = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Integer)
    atta = db.Column(db.Integer)
    sugar = db.Column(db.Integer)
    rice = db.Column(db.Integer)
    pulses = db.Column(db.Integer)
    subghee = db.Column(db.Integer)
    gghee = db.Column(db.Integer)
    gsale = db.Column(db.Integer)
    otheramount = db.Column(db.Integer)
    totalamount = db.Column(db.Integer)


@app.route("/",methods=["GET", "POST"])
def index():
    
     return render_template("index.html")


@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        login = user.query.filter_by(username=username, password=password).first()
        if login is not None:
            return redirect(url_for("input"))
    return render_template("login.html")

@app.route("/adminlogin",methods=["GET", "POST"])
def adminlogin():
    if request.method == "POST":
        aname = request.form["aname"]
        apassword = request.form["apassword"]
        
        adminlogin = admin.query.filter_by(aname=aname, apassword=apassword).first()
        if adminlogin is not None:
            return redirect(url_for("areport"))
    return render_template("adminlogin.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        register = user(username = username, email = email, password = password)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/aregister", methods=["GET", "POST"])
def aregister():
    if request.method == "POST":
        aname = request.form['aname']
        amail = request.form['amail']
        apassword = request.form['apassword']

        register = user(aname = aname, amail = amail, apassword = apassword)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("adminlogin"))
    return render_template("aregister.html")



@app.route("/input", methods=['GET', 'POST'])
def input():
    if request.method=='POST':
        storename = request.form['storename']
        date = request.form['date']
        atta = request.form['atta']
        sugar = request.form['sugar']
        rice = request.form['rice']
        pulses = request.form['pulses']
        subghee = request.form['subghee']
        gghee = request.form['gghee']
        gsale = request.form['gsale']
        otheramount = request.form['otheramount']
        totalamount = request.form['totalamount']
        data = Data(storename=storename,date=date,atta=atta,sugar=sugar,rice=rice,pulses=pulses,subghee=subghee,gghee=gghee,gsale=gsale,otheramount=otheramount,totalamount=totalamount)
        db.session.add(data)
        db.session.commit()
    return render_template("input.html")

@app.route("/ainput", methods=['GET', 'POST'])
def ainput():
    if request.method=='POST':
        storename = request.form['storename']
        date = request.form['date']
        atta = request.form['atta']
        sugar = request.form['sugar']
        rice = request.form['rice']
        pulses = request.form['pulses']
        subghee = request.form['subghee']
        gghee = request.form['gghee']
        gsale = request.form['gsale']
        otheramount = request.form['otheramount']
        totalamount = request.form['totalamount']
        data = Data(storename=storename,date=date,atta=atta,sugar=sugar,rice=rice,pulses=pulses,subghee=subghee,gghee=gghee,gsale=gsale,otheramount=otheramount,totalamount=totalamount)
        db.session.add(data)
        db.session.commit()
    return render_template("ainput.html")


@app.route("/report")
def report():
    allData = Data.query.all()
    print(allData)
    return render_template("report.html", allData=allData)

@app.route("/areport")
def areport():
    allData = Data.query.all()
    print(allData)
    return render_template("areport.html", allData=allData)


@app.route("/dashboard")
def dashboard():
    allData = Data.query.all()
    print(allData)
    return render_template("dashboard.html", allData=allData)



@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        storename = request.form['storename']
        date = request.form['date']
        atta = request.form['atta']
        sugar = request.form['sugar']
        rice = request.form['rice']
        pulses = request.form['pulses']
        subghee = request.form['subghee']
        gghee = request.form['gghee']
        gsale = request.form['gsale']
        otheramount = request.form['otheramount']
        totalamount = request.form['totalamount']
        data = Data.query.filter_by(sno=sno).first()
        data.storename=storename
        data.date=date
        data.atta=atta
        data.sugar=sugar
        data.rice=rice
        data.pulses=pulses
        data.subghee=subghee
        data.gghee=gghee
        data.gsale=gsale
        data.otheramount=otheramount
        data.totalamount=totalamount
        db.session.add(data)
        db.session.commit()
        return redirect("/report")
        
    data = Data.query.filter_by(sno=sno).first()
    return render_template("update.html", data=data)
    

@app.route("/delete/<int:sno>")
def delete(sno):
    data = Data.query.filter_by(sno=sno).first()
    db.session.delete(data)
    db.session.commit()
    return redirect("/report")


# def ui(location):
#     qt_app = QApplication(sys.argv)
#     web = QWebEngineView()
#     web.setWindowTitle("Management System")
#     web.resize(900, 800)
#     # web.setZoomFactor(1.5)
#     web.load(QUrl(location))
#     web.show()
    
#     sys.exit(qt_app.exec_())
    
# if __name__ == "__main__":
#     Timer(1,lambda: ui("http://127.0.0.1:5000/")).start()
#     app.run(debug = False)



# url = "report.html"
# table = pd.read_html(url)[0]
# table.to_excel("data/datafile.xlsx")
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     form = Nameform()
#     if form.validate_on_submit():
#         old_name = session.get('name')
#         if old_name is not None and old_name != form.name.data:
#             flash('Looks like you have changed your name!')
#         session['name'] = form.name.data
#         form.name.data = ''
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'))
#         form = form, name = session.get('name'))




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)