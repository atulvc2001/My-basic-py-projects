#text to speech converter
import pyttsx3

# rendering content from webpage
import requests
from bs4 import BeautifulSoup

# Function which speaks
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    # initializing the engine with the Microsoft Speech API
    engine = pyttsx3.init("sapi5")

    # using a specific getProperty method
    voices = engine.getProperty("voices")

    # Setting the property of the Voice as the ID of voices[0]
    engine.setProperty("voice", voices[0].id)

    # Requesting text from the website
    res = requests.get(input("Enter the URL here: ")).text
    soup = BeautifulSoup(res, "html.parser")

    # initialising list
    articles = []

    # Extracting <p> tags
    for i in range(len(soup.findChildren("p"))):
        article = soup.findChildren("p")[i].getText().strip()
        articles.append(article)

    # Joining the list elements and printing them
    text = " ".join(articles)
    print(text)

    # Calling the the speaking function
    speak(text)
    engine.runAndWait()


