#sudo apt-get install python{,3}-pyaudio
#from __future__ import division
import pyaudio
import os
import wave
import threading
import sys
import math
import struct
import random
try:
	from itertools import izip
except ImportError:
	izip = zip
	xrange = range

def sine_tone(fileName, frequency, duration, volume=1, sample_rate=44100):
	print(fileName)
	n_samples = int(sample_rate * duration)
	restframes = n_samples % sample_rate

	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(1), #8bit
			channels=1, #mono
			rate=sample_rate,
			output=True)
	s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
	samples = (int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))
	for buf in izip(*[samples]*sample_rate): # write several samples at a time
		stream.write(bytes(bytearray(buf)))

	#fill remainder of frameset with silence
	stream.write(b'\x80' * restframes)

	stream.stop_stream()
	stream.close()
	p.terminate()
	
	
	
	waveFile = wave.open(fileName, 'wb')
	waveFile.setnchannels(1)
	waveFile.setsampwidth(2)
	waveFile.setframerate(sample_rate)
	
	for buf in izip(*[samples]*sample_rate):
	   #value = samples[i]
	   #data = struct.pack('<h', value)
	   waveFile.writeframesraw( bytes(bytearray(buf)) )
	#print("Done for "+str(fileName))
	for i in range(300):
		value = random.randint(-32767, 32767)
		data = struct.pack('<h', value)
		waveFile.writeframesraw( data )
	#waveFile.writeframes(b''.join(samples))
	#waveFile.writeframesraw( b'' * restframes )
	waveFile.close()

for x in range(12):
	defaultFrequency = 440.00
	defaultDuration = 1
	fileName = "file" + str(x)
	sine_tone(fileName, defaultFrequency* (1.059463**(x-4)), defaultDuration, 1, 44100)