import openai
import os
from gtts import gTTS
openai.api_key = "openai.api keyinizi buraya giriniz"

a=input("Sorunuzu giriniz. :")
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=a,
    max_tokens=500
)
print(response)
text= response.choices[0].text.replace("\n","")
print(text)
tts = gTTS(text=text,lang="tr")
tts.save("Openai.mp3")
os.system("Openai.mp3")

