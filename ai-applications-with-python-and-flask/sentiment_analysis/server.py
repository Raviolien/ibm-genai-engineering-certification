''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app
app = Flask('Sentiment Analyzer')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Extract text to analyse from page
    text_to_analyze = request.args.get('textToAnalyze')

    # Call sentiment analyzer function
    response = sentiment_analyzer(text_to_analyze)

    # Extract the label and score from the response
    label = response['label']
    label = label.split('_')[1]
    score = response['score']

    # Check if the label is None, indicating an error or invalid input
    if label is None:
        return "Invalid input! Try again."
    # Return a formatted string with the sentiment label and score
    return (
        f"The given text has been identified as {label} with a score of {score}."
    )

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    # Render HTML template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)