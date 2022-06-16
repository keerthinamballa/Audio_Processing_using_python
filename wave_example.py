import wave
obj = wave.open("audio.wav", "rb")

print("Number of channels ", obj.getnchannels())
print("Sample width ", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frames ", obj.getnframes())
print("Parameters", obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print(t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames))

obj.close()

obj_new = wave.open("audio_new.wav", "wb")

obj_new.setnchannels(2)
obj_new.setsampwidth(2)
obj_new.setframerate(8000.0)
# obj_new.setnframes(268327)

obj_new.writeframes(frames)
obj_new.close()