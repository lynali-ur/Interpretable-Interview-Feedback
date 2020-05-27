Interpretable Interview Feedback

Using Pyaudio and OpenCV to record video and audio separatelu to achieve longer video time. The video is passed back to the front end using javascript in real time.

Using flask platform, the server created both audio thread and video thread. When stop recording, audio thread will be set to None in order to record next new attempt. When stop recording, the video, audio, and auto-generated transcript file will all be saved in the data folder.

The audio file is automatically passed through google cloud speech-to-text api, which is required to download before running the prototype.

The packages are listed below and can be installed using the requirements.txt. I recommend installing it under a virtual environment using command:
********pip install -r requirements.txt**********

The google api requires credential for verification purpose, the key is in the GCloudKey.json file, the instruction to set it up can be found here: https://cloud.google.com/docs/authentication/getting-started.


Dependencies:
python 3.7.3

Flask 1.1.1
Werkzeug 0.16.0
pyaudio 0.2.11
opencv-python 4.2.0

Google Cloud SDK 288.0.0
