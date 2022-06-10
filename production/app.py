from flask import *

#app
app = Flask(__name__)

@app.route('/')
def test():
    print("hello")
    return render_template("index.html")

    

if __name__ == '__main__':
    app.run(debug=True)
