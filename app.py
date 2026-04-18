
from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key="secret123"

slots = [{"id":i,"occupied":False,"vehicle":""} for i in range(1,11)]

@app.route('/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        if request.form['username']=='admin' and request.form['password']=='admin123':
            session['user']='admin'
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    occ=sum(1 for s in slots if s["occupied"])
    free=len(slots)-occ
    return render_template('dashboard.html', slots=slots, occ=occ, free=free)

@app.route('/park/<int:sid>', methods=['POST'])
def park(sid):
    for s in slots:
        if s["id"]==sid:
            s["occupied"]=True
            s["vehicle"]=request.form['vehicle']
    return redirect('/dashboard')

@app.route('/exit/<int:sid>')
def exitv(sid):
    for s in slots:
        if s["id"]==sid:
            s["occupied"]=False
            s["vehicle"]=""
    return redirect('/dashboard')

if __name__=='__main__':
    app.run(debug=True)
