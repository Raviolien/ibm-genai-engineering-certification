import requests

def sentiment_analyzer(text_to_analyse):
    '''
    This function uses the Watson API to analyze the sentiment of a given text
    '''

    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    # Headers for the request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Send the request to the sentiment analysis service
    response = requests.post(url, json = myobj, headers=header)
    
    return response.text