from flask import Flask

aap=Flask("name ")

@app.route("/")
def index():
  return render_template("B.html")
