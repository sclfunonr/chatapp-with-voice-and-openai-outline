from openai import OpenAI
import requests # make request calls to Watson Speech-to-Text API

openai_client = OpenAI()


def speech_to_text(audio_binary):
    # Set up Watson Speech-to-Text HTTP API URL
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url = base_url+'/speech-to-text/api/v1/recognize'

    # Set up parameters for our HTTP request
    params = {
        'model': 'en-US_Multimedia',
    }

    # Set up the body of our HTTP request
    body = audio_binary

    # Send an HTTP Post request
    response = requests.post(api_url, params=params, data=audio_binary).json()
    
    # Parse the response to get our transcribed text
    text = 'null'
    while bool(response.get('results')):
        print('speech to text response:', response)
        text = response.get('results').pop().get('alternatives').pop().get('transcript')
        print('recognised text: ', text)
        return text


def text_to_speech(text, voice=""):
    return None


def openai_process_message(user_message):
    """ Take in a prompt and pass it to OpenAI's GPT-3 API
    to receive a response."""

    # Set the prompt for OpenAI API
    prompt="Act like a personal assistant. You can respond to questions, translate sentences, summarize news, and give recommendations."

    # Call the OpenAI API to process our prompt
    openai_response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": system, "content": prompt},
            {"role": "user", "content": user_message}
        ],
        max_tokens=4000
    )
    print("openai response:", openai_response)

    # Parse the response to get the response message for our prompt
    response_text = openai_response.choices[0].message.content
    return response_text
