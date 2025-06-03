''' 
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotion_detect():
    ''' 
    This code receives the text from the HTML interface and 
    runs emotion detection over it using the emotion_detector()
    function. The output returned shows emotions, their score and 
    the dominant emotion.
    '''
    # Extract text to analyse from page
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion_detector function
    response = emotion_detector(text_to_analyze)

    # Define emotions to check
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness', 'dominant_emotion']

    # Check if emotions are None
    if any(response[emotion] is None for emotion in emotions):
        output = "Invalid text! Please try again!"
    else:
        # Format the output string
        output = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']}, "
            f"'disgust': {response['disgust']}, "
            f"'fear': {response['fear']}, "
            f"'joy': {response['joy']} and "
            f"'sadness': {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )

    return output

@app.route("/")
def render_index_page():
    ''' 
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    # Render HTML template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    