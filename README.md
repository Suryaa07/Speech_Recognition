# Speech Recognition with Python

This repository contains a Python script for performing speech recognition using the SpeechRecognition library. With this script, you can capture audio input from a microphone, send it to Google's speech recognition service, and receive the transcribed text as output. The code handles various error scenarios and provides informative messages to the user.

## Prerequisites

Before you can use this script, you need to install the required Python packages. You can install them using pip:

```bash
pip install SpeechRecognition
```

## Usage

1. Import the `speech_recognition` library:

   ```python
   import speech_recognition as sr
   ```

2. Create a recognizer object:

   ```python
   recognizer = sr.Recognizer()
   ```

3. Use a microphone as the audio source:

   ```python
   with sr.Microphone() as source:
   ```

4. Prompt the user to speak:

   ```python
   print("Speak something...")
   ```

5. Capture audio from the microphone:

   ```python
   audio = recognizer.listen(source)
   ```

6. Attempt to recognize the speech using Google's speech recognition service:

   ```python
   try:
       text = recognizer.recognize_google(audio)
       print("You said: " + text)
   ```

7. Handle the case when the speech cannot be understood:

   ```python
   except sr.UnknownValueError:
       print("Sorry, I couldn't understand what you said.")
   ```

8. Handle the case when there is an error with the speech recognition request:

   ```python
   except sr.RequestError as e:
       print("Sorry, there was an error with the request. {0}".format(e))
   ```

## How It Works

This script uses the SpeechRecognition library to access the microphone, capture audio, and then send that audio to Google's speech recognition service. If Google can recognize the speech, the transcribed text is printed to the console. If Google cannot understand the speech or there is an error with the request, appropriate error messages are displayed.

## Example

Here's an example of how to use this script:

1. Run the script.

2. You will see the message "Speak something..." printed to the console.

3. Speak into the microphone.

4. The script will attempt to recognize what you said and print the transcribed text.

## Acknowledgments

- This script uses the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library.
- Thanks to Google for providing the speech recognition service.

Feel free to use, modify, and distribute this code as needed. Happy speech recognition!
