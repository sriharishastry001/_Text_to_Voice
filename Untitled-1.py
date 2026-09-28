from gtts import gTTS
text="Every morning, the streets become peaceful as the sun slowly rises. People begin their day by going for walks, buying groceries, or heading to work. Birds fly between the trees while the cool breeze makes the morning pleasant. A simple morning walk can help clear the mind and prepare us for a productive day."
tts=gTTS(text=text,lang="en")
tts.save("hello1.mp3")
print("Done!")
