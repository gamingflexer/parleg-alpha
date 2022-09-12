from flask import *
from main import *
import cv2

camera = None
if len(sys.argv) == 2:
    camera = cv2.VideoCapture(sys.argv[0])
else:
    camera = cv2.VideoCapture(0)
    
width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))

#app
app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(camera), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/start')
def start_model():
    print("Model STARTED....")
    # print(Video_path)
    # detection(Video_path)
    return render_template("test.html")


@app.route('/stop')
def stop_model():
    print("Model STOPPED....")
    return render_template("index.html")
    
@app.route('/csv')
def download_csv():
    print("Downloading CSV....")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
