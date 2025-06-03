import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Define test class
class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        
        # Test positive sentiment:
        result1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result1['label'], 'SENT_POSITIVE')

        # Test negative sentiment:
        result2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result2['label'], 'SENT_NEGATIVE')

        # Test neutral sentiment
        result3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result3['label'], 'SENT_NEUTRAL')

# Call the test 
unittest.main()