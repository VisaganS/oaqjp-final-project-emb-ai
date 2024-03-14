import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        emotions = {
            'anger': formatted_response['emotionPredictions'][0]['emotion']['anger'],
            'disgust': formatted_response['emotionPredictions'][0]['emotion']['disgust'],
            'fear': formatted_response['emotionPredictions'][0]['emotion']['fear'],
            'joy': formatted_response['emotionPredictions'][0]['emotion']['joy'],
            'sadness': formatted_response['emotionPredictions'][0]['emotion']['sadness']
        }
        dominant_emotion = None
        highest_emotion_value = 0

        for emotion, value in emotions.items():
            if value > highest_emotion_value:
                dominant_emotion = emotion
                highest_emotion_value = value

    elif response.status_code == 400:
         emotions = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None
        }
         dominant_emotion = None
        
    return {'anger': emotions['anger'], 'disgust': emotions['disgust'], 'fear': emotions['fear'], 'joy': emotions['joy'], 'sadness': emotions['sadness'], 'dominant_emotion': dominant_emotion}


    