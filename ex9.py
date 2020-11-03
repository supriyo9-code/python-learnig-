# Nwes Paper Reader
import requests
import json

def speak(str):
    from win32com.client import Dispatch

    speak =Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':
    speak("Hey Boss news for today.. Lets begin")
    url = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=f495fea7d0d048c2ab24fbfe7d755665"
    news =  requests.get(url).text
    news_dict = json.loads(news)
    print(news_dict["articles"])
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        speak("Moving on to the next news..Listen Carefully")
