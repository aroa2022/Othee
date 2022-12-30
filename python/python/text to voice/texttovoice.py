from gtts import gTTS
import os
text = """
من الدولة أو إيراداتها
"""

sp= gTTS(text=text,lang="ar")

sp.save('1.wav')
os.system('1.wav')