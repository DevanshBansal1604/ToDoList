from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def func():
    return render_template("index.html")

@app.route("/sub", methods=['POST'])
def submit():
    if request.method=="POST":

        desc=request.form['desc']
        dead=request.form['dead']

        pres=str(datetime.now().time())
        pres=datetime.strptime(pres,"%H:%M:%S.%f")

        print(pres)

        dead=datetime.strptime(dead, "%H:%M")

        diff=dead-pres

        ls.append((desc,diff))

        for i in range(1, len(ls)):
            j = i-1
            while j >= 0:
                if ls[i][1] < ls[j][1]:
                    ls[i], ls[j] = ls[j], ls[i]
                
                j-=1
        
        print(ls)
        msg="Task Has Been Added Successfully!"
        
    return render_template("sub.html",todolist=ls,msgs=msg)

if __name__ == "__main__":
    ls=[]
    app.run(debug=True)