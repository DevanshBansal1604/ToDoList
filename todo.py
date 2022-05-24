from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def func():
    return render_template("index.html")

@app.route("/sub", methods=['POST'])
def submit():
    if request.method=="POST":
        return render_template("sub.html")

if __name__ == "__main__":
    app.run(debug=True)