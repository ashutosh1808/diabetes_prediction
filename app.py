from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
@app.route("/")
def home():
	return render_template("home.html")

@app.route("/pred",methods=["POST"])
def predict():
	msg=""
	glu=int(request.form["glu"])
	preg=int(request.form["preg"])
	bmi=float(request.form["bmi"])
	age=int(request.form["age"])
	d=[[glu,preg,bmi,age]]
	with open("db.model","rb") as f:
		model1=pickle.load(f)
	res=model1.predict(d)[0]
	if res==0:			msg="diabetes not detected!"
	elif res==1:			msg="diabetes detected!"
	return render_template("home.html",msg=msg)
if __name__=="__main__":
	app.run(debug=True,use_reloader=True)