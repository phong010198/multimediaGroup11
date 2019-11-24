import pyaudio
import os
import wave
import threading
import sys
from __future__ import division
import math

print("Nhập tên file:")
name = input()
wf = wave.open(name, 'rb')

p = pyaudio.PyAudio()

# define callback
def callback(in_data, frame_count, time_info, status):
	data = wf.readframes(frame_count)
	return (data, pyaudio.paContinue)
while (0<1):
	# open stream using callback, and start
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True,
		stream_callback=callback)
	stream.start_stream()
	while stream.is_active():
		time.sleep(0.1)
	stream.stop_stream()
	stream.close()
	wf.close()
p.terminate()