from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['Get', 'Posrt'])
def index():
    return render_template('index.html')



app.run(debug = True)