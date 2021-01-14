from subprocess import run, PIPE

import flask
from flask import logging, Flask, render_template, request, url_for, jsonify
import speech_to_text_as_api
from sentiment import get_sentiment
from keyphrase import get_keywords


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/audio', methods=['POST'])
def audio():
    with open('recorded_audio.wav', 'wb') as f:
        f.write(request.data)
    file = open(r'recorded_audio.wav','rb')
    data = file.read()
    response = transcribe_recorded_audio(data)
    #sent_response = sentiment.get_sentiment(input_text, input_lang, output_text, output_lang)
    print(response)
    print("====================")
    print(type(print(response.text.encode('utf8'))))
    text = response.json()
    transcribed_text = text['DisplayText']
    print(transcribed_text)
    #res = analyze_sentiment(transcribed_text)
    print(type(print(response.text.encode('utf8'))))
    return transcribed_text

def transcribe_recorded_audio(data):
    print('<<<<<<In transcribe function>>>>>')
    response = speech_to_text_as_api.transcribe_audio(data)
    return response

@app.route('/sentiment')
def sentiment():
    data = flask.request.args.get('word')
    print(request.args)
    #data = request.get_json()
    print("Printing data from sentiment analysis call...................")
    print(data)
    #input_text = data['inputText']
    #input_text = "good"
    response = analyze_sentiment(data)
    print(response)
    print(type(response))
    r = response['documents'][0]['score']
    print(r*100)
    return jsonify({'html':str(round(r*100,2))+"% positive"})


def analyze_sentiment(textdata):
    print('<<<<<<<In analyze_sentiment function>>>>>>')
    response = get_sentiment(textdata)
    return response

@app.route('/keyphrase')
def keyphrase():
    data = flask.request.args.get('word')
    print(request.args)
    #data = request.get_json()
    print("Printing data from keyphrase extraction call...................")
    print(data)
    #input_text = data['inputText']
    #input_text = "good"
    response = get_keywords(data)
    print(response)
    r = response['documents'][0]['keyPhrases']
    str_r = ' , '.join(r)
    print(type(str_r))
    print(str_r)
    return jsonify({'html':str_r})

# @app.route('/get_word')
# def get_prediction():
#   word = flask.request.args.get('word')
#   return flask.jsonify({'html':"SUCCESS"})



if __name__ == "__main__":
    #app.logger = logging.getLogger('audio-gui')
    app.run(debug=True)
