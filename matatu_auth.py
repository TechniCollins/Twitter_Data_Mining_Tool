import tweepy

consumer_token = "HpzN1KeynT4gADPnwZFVYqW57"
consumer_secret = "ADTRTCH4d81olOvI3OuWzjKvEozZv4SHwckNlbEKmsSebGsnsS"
access_token = "1084028173082419200-qrcGBdUKEZMcPPiUU8nA91d0jEoJPM"
access_token_secret = "uPLrwD2y2Wr2VaG5h9826UtTT5ShMGx2t5dJM4hhKjPa4"

auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)