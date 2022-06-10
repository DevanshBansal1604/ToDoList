from flask import Flask, render_template, request

from datetime import datetime, timedelta

app = Flask(__name__)


@app.route("/")
def func():
    msg="empty"

    return render_template("index.html",msgs=msg)

@app.route("/",methods=["POST"])
def submit():
    if request.method=="POST":
        
        if 'desc' in request.form.keys():
            desc=request.form['desc']
            dead=request.form['dead']

            pres=datetime.strptime("2022-01-01 00:00", "%Y-%m-%d %H:%M")
            

            Ndead=datetime.strptime(dead, "%Y-%m-%dT%H:%M")

            strdead=Ndead.strftime("%Y-%m-%d %H:%M")

            diff=Ndead-pres

            new_desc = desc[::]
            new_desc.replace(" ", "")

            print("ye hai new desc: ", new_desc)

            if(diff.total_seconds()<7200):
                ls.append([desc,diff,strdead,'#FA8072', new_desc])
            elif(diff.total_seconds()<21600):
                ls.append([desc,diff,strdead,'#FDDC56', new_desc])
            else:
                ls.append([desc,diff,strdead,'#EEEEEE', new_desc])

            

            for i in range(1, len(ls)):
                k=i
                j = k-1
                while j >= 0:
                    if ls[k][1] < ls[j][1]:
                        ls[k], ls[j] = ls[j], ls[k]
                    
                    k-=1
                    j-=1
            
            # print(ls)
            now = datetime.now()
        
            for i in ls:
                timeobj = datetime.strptime(i[2], "%Y-%m-%d %H:%M")
                diff2 = timeobj-now

                if diff2.total_seconds()<7200:
                    i[3] = '#FA8072'

                elif diff2.total_seconds()<21600:
                    i[3] = '#FDDC56'

                else:
                    i[3] = '#EEEEEE'

            msg="Task Has Been Added Successfully!"
            return render_template("index.html",todolist=ls,msgs=msg)


        # else:
        #     print("Task",request.form['Done'])
        #     msg="Task Has Been Deleted Successfully!"
        #     return render_template("index.html",todolist=ls,msgs=msg, c=count)
            

        # pres=str(datetime.now().time())
        # pres=datetime.strptime(pres,"%H:%M:%S.%f")

        # print(pres)

        # strdead=dead

        # dead=datetime.strptime(dead, "%H:%M")

        # diff=dead-pres

        # ls.append((desc,diff.seconds,strdead))


        # for i in range(1, len(ls)):
        #     k=i
        #     j = k-1
        #     while j >= 0:
        #         if ls[k][1] < ls[j][1]:
        #             ls[k], ls[j] = ls[j], ls[k]
                
        #         k-=1
        #         j-=1
        
        # print(ls)
        # msg="Task Has Been Added Successfully!"
        # return render_template("index.html",todolist=ls,msgs=msg)

if __name__ == "__main__":
    ls=[]
    
    app.run(debug=True)