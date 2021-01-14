import requests


def transcribe_audio(data):
    key = "ffdfecec244d42159de45ea652cbb083"

    url = "https://eastus2.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US"

    payload = data
    headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Connection': 'keep-alive',
    'Content-Type': 'audio/wav; codecs=audio/pcm; samplerate=16000',
    'Accept': 'application/json',
    #'Transfer-Encoding': 'chunked',
    'Expect' : '100-continue'

    }

    response = requests.request("POST", url, headers=headers, data = payload)
    #print(response)
    #print(response.text.encode('utf8'))
    return response