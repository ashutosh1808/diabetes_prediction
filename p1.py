import pickle

with open("db.model","rb") as f:
	model=pickle.load(f)


glu=int(input("enter glucose level: "))
preg=int(input("enter no of preg: "))
bmi=float(input("enter bmi: "))
age=int(input("enter age: "))
res=model.predict([[glu,preg,bmi,age]])
print(res)
