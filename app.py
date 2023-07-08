# import libraries
from flask import Flask, request, app, jsonify, url_for, render_template, send_file
from utils.model import model_intial, generate_output
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from werkzeug.middleware.profiler import ProfilerMiddleware
app = ProfilerMiddleware(app, restrictions=[20])

# intitalising flask app
app = Flask(__name__)

# loading model
model_id, pipe = model_intial()


# index.html route
@app.route("/")
def homepage():
    return render_template("index.html")


# api route
@app.route("/generate_image_api", methods=["POST"])
def generate_image_api():
    data = request.json["data"]["prompt"]
    gen_image = generate_output(data, pipe)
    byte_io = BytesIO()
    gen_image.save(byte_io, "PNG")
    byte_io.seek(0)
    return send_file(byte_io, mimetype="image/png")


@app.route("/generate", methods=["POST"])
def generate():
    print(request.form)
    data = request.form.get('prompt')
    print(data)
    print("\n\n")
    gen_image = generate_output(data, pipe)
    filename = 'static/generated_image.png'
    gen_image.save(filename)
    return render_template("index.html", generated_image=url_for('static',filename='generated_image.png'))

# health check warm up
@app.route('/health-check')
def health_check():
    return 'OK', 200



if __name__ == "__main__":
    app.run(debug=True,port=5001)
