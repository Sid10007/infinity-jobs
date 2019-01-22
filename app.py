from flask import Flask, render_template, request, session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_session import Session



engine = create_engine("mysql://root:siddharth@localhost:3306/infinityjobs")
db = scoped_session(sessionmaker(bind = engine))


app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/loginjobseeker")
def loginjobseeker():
	return render_template('loginjobseeker.html')

@app.route("/logincompany")
def logincompany():
	return render_template('logincompany.html')

@app.route("/login", methods = ["POST"])
def login():
	userid = request.form.get("userid")
	session['userid'] = userid
	companyid = request.form.get("companyid")
	session['companyid'] = companyid
	if userid is None:	
		password = request.form.get("password")
		check = db.execute("SELECT companyid FROM companies WHERE password = :password", {"password": password})
		if not len(list(check)) == 0:
			password = request.form.get("password")
			check = db.execute("SELECT companyid FROM companies WHERE password = :password AND companyid = :userid", {"password": password, "userid": companyid})
			check = list(check)	
			if not len(check) == 0:
				companyname = db.execute("SELECT companyname FROM companies WHERE companyid = :companyid", {"companyid": session['companyid']}).fetchall()
				companyname = list(companyname)
				session['companyname'] = companyname[0].companyname
				return render_template("companyhome.html", companyid = session['companyid'])
			else:
				return render_template("h1.html", name = "Wrong id or password!!!!")	
		else:
			return render_template("h1.html", name = "Wrong id or password!!!!")
	else:
		password = request.form.get("password")
		check = db.execute("SELECT userid FROM jobseekers WHERE password = :password AND userid = :userid", {"password": password, "userid": userid})
		check = list(check)
		if not len(check) == 0:
			companies = db.execute("SELECT DISTINCT companyname, jobdesc, jobid FROM jobs").fetchall()
			return render_template("jobseekerhome.html", companies = companies, userid = userid)
		else:
			return render_template("h1.html", name = "Wrong id or password!!!!")
	
@app.route("/signup", methods = ["POST"])
def signup():
	username = request.form.get("username")
	companyname = request.form.get("companyname") 
	if username is None:	
		try:	
			username = request.form.get("companyname")
			useremail = request.form.get("email")
			userid = request.form.get("companyid")
			userpassword = request.form.get("password")
			db.execute("INSERT INTO companies VALUES (:userid, :username, :useremail, :userpassword)", {"userid" : userid, "username": username, "useremail": useremail, "userpassword": userpassword})
			db.execute("COMMIT")
			return render_template("h1.html", name = "Signup successful!! Go back and login...")
		except:
			return render_template("h1.html", name = "CompanyId already exists...Go back and enter another one...")
	else:
		try:	
			username = request.form.get("username")
			useremail = request.form.get("email")
			userid = request.form.get("userid")
			userpassword = request.form.get("password")
			db.execute("INSERT INTO jobseekers VALUES (:userid, :username, :useremail, :userpassword)", {"userid" : userid, "username": username, "useremail": useremail, "userpassword": userpassword})
			db.execute("COMMIT")
			return render_template("h1.html", name = "Signup successful!! Go back and login...")
		except:
			return render_template("h1.html", name = "UserId already exists...Go back and enter another one...")
	
@app.route("/home/applications", methods = ["POST"])
def apply():
	application = request.form.get("companylist")
	jobid = int(application)
	application = "Successfully APPLIED  for JOBID : " + application + "!!! Go back and confirm in the VIEW section...."
	userid = request.form.get("userid")
	db.execute("INSERT INTO applications VALUES (:jobid, :userid)", {"jobid": jobid, "userid": userid})
	db.execute("COMMIT")
	return render_template("h1.html", name = application)

@app.route("/home/view", methods = ["POST"])
def view():
	jobs = list(db.execute("SELECT jobs.jobdesc, jobs.companyname FROM jobs INNER JOIN applications ON jobs.jobid = applications.jobid WHERE applications.userid = :userid", {"userid": session['userid']}).fetchall())
	return render_template("view.html", jobs = jobs)

@app.route("/home/add", methods = ["POST"])
def add():
	jobdesc = request.form.get("jobdesc")
	salary = request.form.get("salary")
	jobid = request.form.get("jobid")
	db.execute("INSERT INTO jobs VALUES (:jobid, :salary, :companyid, :companyname, :jobdesc)", {"jobid": jobid, "salary": salary, "companyid": session['companyid'], "companyname": session['companyname'], "jobdesc": jobdesc})
	db.execute("COMMIT")
	return	render_template("h1.html", name = "JOB SUCCESSFULLY ADDED!!!!")

@app.route("/home/viewapplications", methods = ["POST"])
def view2():
	applications = list(db.execute("SELECT jobs.jobdesc, jobseekers.username FROM jobs INNER JOIN applications ON applications.jobid = jobs.jobid INNER JOIN jobseekers ON jobseekers.userid = applications.userid WHERE jobs.companyname = :companyname", {"companyname": session['companyname']}).fetchall())
	return render_template("view2.html", applications = applications)

@app.route("/admin")
def admin():
	return render_template("adminlogin.html")


@app.route("/admin/show", methods = ["POST"])
def show():
	if request.form.get("admin") == "admin" and request.form.get("password") == "adminpassword":
		jobs = list(db.execute("SELECT jobid, jobdesc, companyname FROM jobs").fetchall())
		users = list(db.execute("SELECT userid, username FROM jobseekers").fetchall())
		return render_template("admin.html", jobs = jobs, users = users) 

@app.route("/admin/show/getdata", methods=["POST"])
def getdata():
	jobid = request.form.get("joblist")
	userid = request.form.get("userlist")
	if not userid is None:
		jobs = list(db.execute("SELECT applications.jobid, jobs.jobdesc, jobs.companyname FROM applications INNER JOIN jobs ON applications.jobid = jobs.jobid WHERE applications.userid = :userid", {"userid": userid}).fetchall())
		return render_template("data.html", jobs = jobs)
	else:
		users = list(db.execute("SELECT applications.userid, jobseekers.username, jobseekers.email FROM applications INNER JOIN jobseekers ON applications.userid = jobseekers.userid WHERE applications.jobid = :userid", {"userid": jobid}).fetchall()) 
		return render_template("data2.html", users = users)