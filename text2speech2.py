from gtts import gTTS
import os
text='Text To Speech Program'
language='en'
conv=gTTS(text=text,lang=language,slow=False)
conv.save('audio.mp3')
os.system('audio.mp3')