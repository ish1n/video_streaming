from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def generate():
    while True:
        # read camera
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
        yield b'--frame\b\n'b'Content-Type:image/jpeg\r\n\r\n' + frame + b'\b\n'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generate(), mimetype='multipart/x-mixed-replace;boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)
