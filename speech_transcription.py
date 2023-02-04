import os
import queue
import sounddevice as sd
import vosk
import sys
import time

# Global Vars
voice_model = 'en-us-light'

q = queue.Queue()
def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def listen(timeout = 60):
    with sd.RawInputStream(samplerate=samplerate, blocksize = 8000, device=None, dtype='int16',
                        channels=1, callback=callback):
        print("[INFO] Listening")

        rec = vosk.KaldiRecognizer(model, samplerate)
        start_time = time.time()

        while (start_time + timeout) > time.time():
            data = q.get()
            if rec.AcceptWaveform(data):
                result = rec.Result()
                print(result)
                return result
            else:
                print(rec.PartialResult())
        return "Cancel"

# Init Model and Microphone
if not os.path.exists(voice_model):
    print ("Please download a model for your language from https://alphacephei.com/vosk/models")
    print ("and unpack as 'model' in the current folder.")
    sys.exit()

device_info = sd.query_devices(None, 'input')
samplerate = int(device_info['default_samplerate'])
model = vosk.Model(voice_model)

listen(timeout=45)