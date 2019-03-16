from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

def rating(score):
    if(score > -1 and score < -0.5):
        return 1
    elif(score > -0.5 and score <= 0):
        return 2
    elif(score > 0 and score < 0.5):
        return 3
    elif(score > 0.5 and score < 1):
        return 4


def sentiment_analyser_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print(score)


sentiment_analyser_scores("this is cool")
