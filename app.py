# import libraries
from flask import Flask,request,app,jsonify,url_for,render_template,send_file
from utils.model import model_intial, generate_output
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO


# intitalising flask app
app=Flask(__name__)

# loading model
model_id,pipe=model_intial()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/generate_image_api',methods=['POST'])
def generate_image_api():
    data=request.json['data']['prompt']
    gen_image=generate_output(data,pipe)
    byte_io = BytesIO()
    gen_image.save(byte_io, 'PNG')
    byte_io.seek(0)
    return send_file(byte_io, mimetype='image/png')


if __name__=="__main__":
    app.run(debug=True)
