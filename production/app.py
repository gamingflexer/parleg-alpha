from flask import *
from main import *


#app
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")


@app.route('/start')
def start_model():
    print("Model STARTED....🏁")
    print(Video_path)
    detection(Video_path)
    
    return render_template("index.html")

@app.route('/stop')
def stop_model():
    print("Model STOPPED....🛑")
    return render_template("index.html")
    
@app.route('/csv')
def download_csv():
    print("Downloading CSV....📥")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
