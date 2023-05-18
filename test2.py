from pywhispercpp.model import Model
import os

model = Model('medium', n_threads=os.cpu_count())
segments = model.transcribe('temporary_audio.wav', language="auto", speed_up=True)
for segment in segments:
    print(segment.text)