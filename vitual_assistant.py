# Description: My personal virtual assistant program that responds to my questions
# installed pipwin,gTTs,wikipedia,SpeechRecognition,pyAudio
# Import libraries
import speech_recognition as sr
import os
from gtts import gTTS
import _datetime
import wikipedia
import warnings
import calendar
import random

warnings.filterwarnings('ignore')


# function to record audio and return it as a string

def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say Something!!!')
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10, )
        except sr.WaitTimeoutError:
            print('Did not hear any input, please speak again')
            assistentResponse('Did not hear any input, please speak again')
            return None  # To signify no successful audio capture
        finally:
            print('Done listening')

    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('Google Speech could not understand the audio, unknown error')
        assistentResponse('I did not understand that. Please try again.')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition Service Error ' + e)
        assistentResponse('There was an error processing your request. Please try again.')

    return data


# A function to get the virtual assistant response
def assistentResponse(text):
    if not text.strip():
        print("Empty response. Nothing to convert to audio.")
        return

    print(text)
    # Convert text to speech
    myObj = gTTS(text=text, lang='en', slow=False)
    # Save the converted audio to a file
    myObj.save('assistant_response.mp3')
    # Play the converted file
    os.system("afplay assistant_response.mp3")


# A function get the AI started 'wake word'

def wakeWord(text):
    WAKE_WORDS = ['zara']

    text = text.lower()  # Converting the text to all lower case words

    # Check to see if the user command has a wake word or phrase

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True
    # If the wake word isn't found in the text from the loop it returns false
    return False


# A function to get the current date

def getDate():
    now = _datetime.datetime.now()
    my_date = _datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    month_num = now.month
    day_num = now.day

    # A list of months
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                   'November', 'December']
    # A list of Ordinal numbers
    ordinal_numbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th',
                       '14th', '15th', '16th', '17th', '18th',
                       '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th',
                       '31st']

    return 'Today is ' + weekday + ' ' + month_names[month_num - 5] + ' ' + 'the ' + ordinal_numbers[day_num - 5] + '.'


def greeting(text):
    # Greeting  inputs
    GREETING_INPUTS = ['hi', 'how are you', 'wats up', 'how you dey', 'hello']

    # Greeting responses
    GREETING_RESPONSES = ['howdy', "hope you're good", 'wats good', 'hey there']

    # If the  users input is a greeting then return  a random greeting response

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    # If no greeting was detected return an empty string
    return ' '


# A function to get a persons first and last name from the text
def getPerson(text):
    wordList = text.split()  # Splitting the text into a list of words

    if 'who is' in text:
        startIndex = wordList.index('who') + 2
    elif 'what is' in text:
        startIndex = wordList.index('what') + 2
    else:
        return None

    # Join words starting from startIndex till the end of the sentence
    return ' '.join(wordList[startIndex:])


while True:
    # Record Audio
    text = recordAudio()
    if text is None:
        continue
    response = ' '

    # Check for the wake word / phrase
    if (wakeWord(text) == True):
        # Check for greeting by the user
        response = response + greeting(text)

        # Check for date or month stuffs
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
            # Convert minute
            if now.minute < 10:
                minute = '0' + str(now.minute)

            else:
                minute = str(now.minute)

            response = response + ' ' + 'It is' + str(hour) + ':' + minute + ' ' + meridiem + '.'

        # Check to see if the user said 'who is'
        # Check to see if the user said 'who is'
        if 'who is' in text or 'what is' in text:
            person = getPerson(text)
            try:
                wiki = wikipedia.summary(person, sentences=2)
                response = response + ' ' + wiki
            except wikipedia.exceptions.DisambiguationError as e:
                response = response + " There are multiple matches for your query. Please be more specific."
            except wikipedia.exceptions.PageError as e:
                response = response + " I couldn't find any information on that topic."
            except Exception as e:
                response = response + " Sorry, I faced an error while fetching the information."

    assistentResponse(response.strip())
