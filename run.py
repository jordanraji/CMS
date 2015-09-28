from app import app
from flask import Flask, render_template, redirect, request
import time

app = Flask(__name__, template_folder='app/templates')

@app.route("/")
def index():
	# hour = time.strftime("%H:%M:%S")
	return render_template(
		'index.html', hour = time.strftime("%H:%M:%S")
		)

app.run(host='0.0.0.0', port=8080, debug=True)
