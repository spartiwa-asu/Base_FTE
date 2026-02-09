from flask import Flask, render_template
#from flask_bootstrap import Bootstrap5

app = Flask(__name__) #
#bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("home.html", title="Home Page")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact Us")

if __name__ == "__main__":
    app.run(debug=True)