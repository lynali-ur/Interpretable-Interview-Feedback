from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io


def recognize():
    client = speech_v1.SpeechClient()

    # The language of the supplied audio
    language_code = "en-US"

    # Sample rate in Hertz of the audio data sent
    sample_rate_hertz = 16000

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    encoding = enums.RecognitionConfig.AudioEncoding.LINEAR16
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
    }
    with io.open(".\\data\\audio.wav", "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)

    f = open(".\\data\\transcript.txt", "w")
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        f.write(alternative.transcript)
        print(u"Transcript: {}".format(alternative.transcript))