from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/read',methods=['GET','POST'])
def getname():
    if(request.method=='POST'):
        myname=request.form.get('name')
        rollno=str(request.form.get('roll'))
        contactno=str(request.form.get('contactno'))
        addmno=str(request.form.get('addmno'))
        return "Name="+myname+"Rollno ="+rollno+"contactno ="+contactno+"addmno ="+addmno



@app.route('/')
def login():
    return render_template("new.html")


if(__name__=='__main__'):
    app.run()