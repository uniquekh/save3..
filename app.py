import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def scammer():
    return 'scammer_botz'


if __name__ == "__main__":   
    app.run()
