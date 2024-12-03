from flask import Flask, render_template, url_for

app = Flask(__name__)

my_friends = ["Андрей", "Алексей", "Даниил", "Иван"]



@app.route("/")
def index():
    return render_template("base.html")


@app.route("/friends")
def friends():
    return render_template("friends.html", my_friends=my_friends)


if __name__ == "__main__":
    app.run(debug=True)
