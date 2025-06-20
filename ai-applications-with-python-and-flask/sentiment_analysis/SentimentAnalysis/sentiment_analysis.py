import requests
import json

def sentiment_analyzer(text_to_analyse):
    '''
    This function uses the Watson API to analyze the sentiment of a given text
    '''

    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Send the request to the sentiment analysis service
    response = requests.post(url, json = myobj, headers=header)

    # Format reponse to json
    formatted_response = json.loads(response.text)

    # Extract info
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None

    # Create dictionary with extraced info
    output = {'label': label, 'score': score}

    return output