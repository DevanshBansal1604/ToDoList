from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def func():
    msg="empty"

    return render_template("index.html",msgs=msg)

@app.route("/",methods=["POST"])
def submit():
    if request.method=="POST":

        desc=request.form['desc']
        dead=request.form['dead']

        pres=str(datetime.now().time())
        pres=datetime.strptime(pres,"%H:%M:%S.%f")

        print(pres)

        strdead=dead

        dead=datetime.strptime(dead, "%H:%M")

        diff=dead-pres

        ls.append((desc,diff.seconds,strdead))


        for i in range(1, len(ls)):
            k=i
            j = k-1
            while j >= 0:
                if ls[k][1] < ls[j][1]:
                    ls[k], ls[j] = ls[j], ls[k]
                
                k-=1
                j-=1
        
        print(ls)
        msg="Task Has Been Added Successfully!"
        return render_template("index.html",todolist=ls,msgs=msg)

if __name__ == "__main__":
    ls=[]
    app.run(debug=True)