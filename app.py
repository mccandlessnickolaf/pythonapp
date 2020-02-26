import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

def get(self):
     self.redirect("https://zippyloan.com/", True)
