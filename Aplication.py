from flask import Flask

aap=Flask("name ")

@app.route("/")
def index():
  return "hello , world!"
