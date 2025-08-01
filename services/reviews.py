from models.reviews import ReviewCreate, Review, Sentiment

def recognize_sentiment(text: str) -> Sentiment:
    sentiments = {
        'хорош': Sentiment.POSITIVE,
        'люблю': Sentiment.POSITIVE,
        'плохо': Sentiment.NEGATIVE,
        'ненавиж': Sentiment.NEGATIVE
    }

    for sentiment in sentiments.keys():
        if sentiment in text.lower():
            return sentiments[sentiment]

    return Sentiment.NEUTRAL

def create_review(
    review: ReviewCreate
) -> Review:
    return Review(
        text=review.text,
        sentiment=recognize_sentiment(review.text)
    )