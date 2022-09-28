def tweet_exits(tweet_id: int):
    with open("data/last_tweet.txt", "r") as tweets_file:
        return str(tweet_id) in tweets_file.read()


def write_file(tweet_id: int):
    with open("data/last_tweet.txt", "w") as tweets_file:
        tweets_file.write(str(tweet_id))
