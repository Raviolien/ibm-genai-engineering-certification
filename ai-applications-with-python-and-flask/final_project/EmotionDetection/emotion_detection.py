import requests
import json

def emotion_detector(text_to_analyze):
    '''
    This function uses the Wasson NLP library to 
    detect emotions from a text 
    '''
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Header specifying the model ID for the emotion detector service 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Dctionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Send the request to the emotion detector service
    response = requests.post(url, json = myobj, headers=header)

    # Format reponse to json
    formatted_response = json.loads(response.text)

    # Extract emotions scores
    if response.status_code == 200:
        anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
        disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
        fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
        joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
        sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']

        # Create dictionary with emotions for output
        emotions = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

    # If the response status code is 400, set all to None
    elif response.status_code == 400:
        anger_score = disgust_score = fear_score = joy_score = sadness_score = None

    # Create dictionary with emotions for output
    emotions = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    
    # Find the dominant emotion
    if all(score is not None for score in emotions.values()):
        dominant_emotion = max(emotions, key=emotions.get)
    else:
        dominant_emotion = None

    # Add dominant emotion to emotion_scores
    emotions['dominant_emotion'] = dominant_emotion

    return emotions