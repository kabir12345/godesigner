# import libraries
from flask import Flask, request, app, url_for, render_template
from utils.model import model_intial, generate_output
import os

# intitalising flask app
app = Flask(__name__)

model_id = None
pipe = None
# index.html route
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.form.get('prompt')
    if model_id is None or pipe is None:
        model_id, pipe = model_intial()
    gen_image = generate_output(data, pipe)
    filename = 'static/generated_image.png'
    gen_image.save(filename)
    return render_template("index.html", generated_image=url_for('static',filename='generated_image.png'))

# health check warm up
@app.route('/health-check')
def health_check():
    return 'OK', 200



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,port=port)


