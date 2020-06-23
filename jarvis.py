import pyttsx3 as py
import datetime as dt
import speech_recognition as sr
import wikipedia as wiki
import smtplib as protocol
import webbrowser as wb
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import urllib.parse, urllib.request, urllib.error
import os

engine = py.init()
#py.say('Hello Jake! This is Jarvis this side. I hope you are good today!')
#py.speak('I love to program!')

#engine.runAndWait()
engine.setProperty('rate', 225)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

#speak('This is Jarvis A.I. assistant')
def time():
    current_time = dt.datetime.now().strftime('The time is: %I:%M%p')
    speak(current_time)

#time()
def date():
    date = dt.datetime.now().strftime("Today's date is: %d %B %Y")
    speak(date)

def wishMe():
    speak('Welcome back Sir! How may I assist you?')

def voiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('(Listening)')
        r.pause_threshold = 1
        audio = r.listen(source)
        #print('Done listening...')
        try:
            #print('Recognizing...')
            query = r.recognize_google(audio, language = 'en-in')
            print('Piyush: ' + query)
        except Exception as e:
            print(e)
            speak("Sorry sir, couldn't hear you!")
            return 'None'
    return query

def searchWiki():
    speak('What shall I search for?')
    keyword = voiceCommand()
    speak('How many lines of information shall I fetch?')
    try:
        info_volume = int(voiceCommand())
    except:
        speak('Sorry sir, can you repeat please?')
        info_volume = int(voiceCommand())
    try:
        result = wiki.summary(keyword, sentences = info_volume)
    except:
        speak('Please give lesser volume of data to fetch!')
        info_volume = int(voiceCommand())
    print(result)
    speak(result)

def mailList(to):
    if 'myself' in to:
        return 'piyushsrivastava.2422@gmail.com'
    elif 'dad' in to:
        speak('Should I send the message to office I.D. or personal?')
        to = voiceCommand()
        if 'office' in to:
            return 'praveen.ks@adityabirla.com'
        elif 'personal' in to:
            return 'praveenks1967@gmail.com'
    elif 'khushi' in to:
        return 'vanshikastar1234@gmail.com'
    elif 'magloo' in to:
        return 'anas9839#gmail.com'
    else:
        return 'Error'

def sendEmail(to, content):
    try:
        speak('What should I say?')
        content = voiceCommand()
        speak('Whom should I send the message?')
        to = voiceCommand()
        to = mailList(to)
        server = protocol.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('myprojectmailbox.2422@gmail.com', 'cemcod-Qyvtuf-0piqta')
        server.sendmail('myprojectmailbox.2422@gmail.com', to, content)
        server.close()
        speak('Email was successfully sent!')
    except Exception as e:
        print(e)
        speak('Unable to send the message!')

def searchInternet():
    speak('What should I search for?')
    search = 'http://www.google.com/?#q=' + quote(voiceCommand())
    #baseURL = 'http://www.google.com/?#q='
    wb.get('safari').open_new_tab(search)

def downloadSong():
    speak('Please tell me the name of the song!')
    song = voiceCommand() + ' lyrics'
    songurl = '+'.join(song.split())
    finalurl = 'https://www.youtube.com/results?search_query=' + songurl
    downloadPath = '~/Music/'
    try:
        response = urllib.request.urlopen(finalurl).read()
        soup = bs(response, 'html.parser')
        vidID = soup.body.find_all(class_ = 'yt-uix-tile-link')[0]['href']
        link = 'https://www.youtube.com' + vidID
        system("youtube-dl -x --audio-format mp3 -o '/Users/jakehamster/Desktop/%(title)s.%(ext)s ' " + link)
        speak('Downloaded' + song)
        speak('Shall I play the song?')
        choice = voiceCommand()
        if 'yes' in choice:
            os.chdir('/users/jakehamster/desktop')
            files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
            songPlay(files[-1])
            os.system('open ' + files[-1])
        elif 'no' in choice:
            speak('As you wish sir!')
    except Exception as e:
        print(e)
        speak('Unable to download the song you requested!')
'''
def songPlay(song_name):
    try:
        os.system('open ' + song_name)
    except Exception as e:
        print(e)
        speak('Sorry sir! The song might be in some other directory!')
        choice = voiceCommand()
        if 'yes' in choice:

        elif 'no' in choice:
'''

def shutdownSleepRestart():
    speak('Are you sure to shutdown sir? I can logout or sleep instead!')
    choice = voiceCommand()
    if 'shut' in choice and 'down' in choice:
        speak('Shall I shutdown now or delay it?')
        choice = voiceCommand()
        if 'now' in choice:
            os.system('shutdown -h now')
        else:
            try:
                time = ''.join(re.findall('[0-9]+'))
                os.system('shutdown -h +' + time)
            except Exception as e:
                print(e)
                speak('Sorry sir, my attemp failed! Please do it manually!')
    elif 'restart' in choice:
        speak('Shall I restart now or delay it?')
        choice = voiceCommand()
        if 'now' in choice:
            os.system('shutdown -r now')
        else:
            try:
                time = ''.join(re.findall('[0-9]+'))
                os.system('shutdown -r +' + time)
            except Exception as e:
                print(e)
                speak('Sorry sir, my attemp failed! Please do it manually!')
    elif 'sleep' in choice:
        speak('Shall I shutdown now or delay it?')
        choice = voiceCommand()
        if 'now' in choice:
            os.system('shutdown -s now')
        else:
            try:
                time = ''.join(re.findall('[0-9]+'))
                os.system('shutdown -s +' + time)
            except Exception as e:
                print(e)
                speak('Sorry sir, My attemp failed! Please do it manually!')
    elif 'logout' in choice:
        speak('Shall I shutdown now or delay it?')
        choice = voiceCommand()
        if 'now' in choice:
            os.system('shutdown -h now')
        else:
            try:
                time = ''.join(re.findall('[0-9]+'))
                os.system('shutdown -h +' + time)
            except Exception as e:
                print(e)
                speak('Sorry sir, My attemp failed! Please do it manually!')
    else:
        speak("Sorry sir, I didn't understand!")
if __name__ == "__main__":
    wishMe()
    while True:
        query = voiceCommand().lower()
        if 'time' in query or 'date' in query:
            if 'time' in query:
                time()
            if 'date' in query:
                date()
        elif 'wikipedia' in query:
            searchWiki()
        elif 'send an email' in query:
            sendEmail()
        elif 'search' in query and 'internet' in query:
            searchInternet()
        elif 'download' in query and 'song' in query:
            downloadSong()
        elif 'shutdown' in query:
            shutdownSleepRestart()
        elif "go offline" in query:
            speak('Okay sir, have a nice day ahead!')
            quit()
