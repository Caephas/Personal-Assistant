## Personal Virtual Assistant

A voice-operated assistant that responds to your commands and questions using Speech Recognition and other Python libraries.

### Features:
- Wake word recognition to initiate the virtual assistant.
- Greeting responses based on user's greeting.
- Ability to tell the current date and time.
- Fetches information from Wikipedia based on "who is" or "what is" questions.
- Error handling for unclear commands or if the information is not found.

### Prerequisites:
You need the following libraries:
- pipwin
- gTTS
- wikipedia
- SpeechRecognition
- pyAudio

You can install these libraries using pip.

### Usage:

Simply run the script. When you see the prompt 'Say Something!!!', you can ask questions or give commands.

The wake word is set to 'zara'. Start with this to activate the assistant.

Example:
- "Zara, who is Albert Einstein?"
- "Zara, what is the date today?"

### Code Structure:

- **recordAudio()**: Records audio and returns it as a string.
- **assistentResponse(text)**: Converts the response string to speech and plays it.
- **wakeWord(text)**: Checks if the wake word or phrase is present in the user's command.
- **getDate()**: Provides the current date.
- **greeting(text)**: Returns a greeting response.
- **getPerson(text)**: Extracts the name of the person or object that information is requested for.
- Main loop that checks for the user's command and provides the appropriate response.

### Acknowledgements:
This assistant uses Google's Speech Recognition service to recognize speech and Wikipedia's API to fetch information.
