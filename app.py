from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def result12():
    if request.method == "POST":
        email = request.form.get("email")
        phone=phone = request.form.get("end")

        return render_template("result12.html", email=email, phone=phone)

    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
