# Description: My personal virtual assistant program that responds to my questions
# installed pipwin,gTTs,wikipedia,SpeechRecognition,pyAudio
#Import libraries

import speech_recognition as sr
import os
from gtts import gTTS
import _datetime
import wikipedia
import warnings
import calendar
import random

#Ignore warning messages inside our program

warnings.filterwarnings('ignore')
#function to record audio and return it as a string
def recordAudio():

    #Record the audio
    r = sr.Recognizer() #Creating a Recognizer object
    #Open the microphone and start recording

    with sr.Microphone() as source:
        print('Say Something!!!')
        audio = r.listen(source, timeout=1, phrase_time_limit=10,)

    # Use Google Speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google Speech could not understand the audio, unknown error')
    except sr.RequestError as e :
        print('Request results from Google Speech Recognition Service Error ' +  e)
    return  data

# A function to get the virtual assistant response

def assistentResponse(text):
    print(text)
    #Convert text to speech
    myObj = gTTS(text = text, lang = 'en', slow = False)

    #Save the converted audion to a file
    myObj.save('assistant_response.mp3')
    # Play the converted file
    os.system("start assistant_response.mp3")

# A function get the AI started 'wake word'

def wakeWord(text):
    WAKE_WORDS = ['vivian', 'bobby']

    text = text.lower() #Converting the text to all lower case words

    # Check to see if the user command has a wake word or phrase


    for phrase in WAKE_WORDS:
        if phrase in text:
            return  True
    # If the wake word isnt found in the text from the loop it returns false
    return  False

# A function to get the current date

def getDate():
    now = _datetime.datetime.now()
    my_date = _datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    month_num = now.month
    day_num = now.day

    

    #A list of months
    month_names = ['January','February','March','April', 'May', 'June', 'July', 'August', 'September','October', 'November', 'December']
    # A list of Ordinal numbers
    ordinal_numbers = ['1st', '2nd', '3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th',
                       '19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']

    return 'Today is ' + weekday + ' ' + month_names[month_num - 5] + ' ' + 'the ' + ordinal_numbers[day_num -  5] + '.'


def greeting(text):
    #Greeting  inputs
    GREETING_INPUTS = ['hi','how are you','wats up','how you dey', 'hello']

    #Greeting responses
    GREETING_RESPONSES = ['howdy',"hope you're good",'wats good', 'hey there']

    # If the  users input is a greeting then return  a random greeting response

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    # If no greeting was detected return an empty string
    return  ' '

# A function to get a persons first and last name from the text
def getPerson(text):
    wordList = text.split() # Spliting the text into a list of words

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) - 1 and  wordList [i].lower() == 'who' and wordList[i + 1].lower() == 'is':
            return  wordList [i + 2] + ' ' +  wordList [i + 3]


while True:
    # Record Audio
    text = recordAudio()
    response = ' '

    # Check for the wake word / phrase
    if (wakeWord(text)== True):
        #Check for greeting by the user
        response = response + greeting(text)

        #Check for date or month stuffs
        if ('date' in text):
            get_date = getDate()
            response = response + ' ' + get_date
        # Check to see if the user said anything having to do with the time
        if ('time' in text):
            now = _datetime.datetime.now()
            meridiem = ''
            if now.hour >= 12:
                meridiem = 'p.m'
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
            #Convert minute
            if now.minute < 10:
                minute =  '0' + str(now.minute)

            else:
                minute = str(now.minute)

            response = response + ' ' + 'It is' + str(hour) + ':' + minute + ' ' + meridiem + '.'


        #Check to see if the user said 'who is'
        if ('who is'|'what is' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=10)
            response = response +  ' ' + wiki

        #Have the assistant respond back using audio and text from response
        assistentResponse(response)