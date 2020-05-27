from flask import Flask, render_template, Response, jsonify, request
from camera import VideoCamera
from audio import AudioRecorder
import gcloud

app = Flask(__name__)

video_camera = None
global_frame = None
audio_recorder = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/record_status', methods=['POST'])
def record_status():
    global video_camera
    global audio_recorder

    if video_camera == None:
        video_camera = VideoCamera()

    if audio_recorder == None:
        audio_recorder = AudioRecorder()

    json = request.get_json()

    status = json['status']

    if status == "true":
        video_camera.start_record()
        audio_recorder.start()
        return jsonify(result="started")
    else:
        video_camera.stop_record()
        audio_recorder.stop()
        audio_recorder = None

        # Speech Recognize
        gcloud.recognize()
        return jsonify(result="stopped")

def video_stream():
    global video_camera 
    global global_frame

    if video_camera == None:
        video_camera = VideoCamera()
        
    while True:
        frame = video_camera.get_frame()

        if frame != None:
            global_frame = frame
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')

@app.route('/video_viewer')
def video_viewer():
    return Response(video_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)