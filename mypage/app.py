from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)


@app.route('/mypage/me')
def me():
    return render_template("AboutMe.html")


@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'GET':
        print("We received GET")
        return render_template("Contact.html")

    else:
        print("We received POST")
        print(request.form)
        return redirect("/mypage/me")


if __name__ == '__main__':
    app.run(debug=True)
