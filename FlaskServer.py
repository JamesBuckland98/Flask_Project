import os
from flask import Flask, redirect, request
import datetime
app = Flask(__name__)

# @app.route('/')
# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

if __name__ == "__main__":
    app.run(debug=True)
