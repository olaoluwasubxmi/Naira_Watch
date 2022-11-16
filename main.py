import tweepy
import yfinance as yahooFinance

api_key = 'ygOHGZoQsRCwW6KrajYWdi76t'
api_secret_key = 'e8xtzbc6R2xdwETDgZKAJc2X50cgYQ6AhU0mDSUTyMPvdVyzWM'
access_token = '1590580697613438976-kVFCZGkv1fnKdmBotmTAI8vtKpLnxr'
access_token_secrets = 'vrFV9ACGSMfywQFjgIFizFmwyiF4nuyUVGKbyGu1HAEmr'


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secrets)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Get naira to usd exchange rate
nairaToUsd = yahooFinance.Ticker("NGN=X")
nairaToUsd = nairaToUsd.info['regularMarketPrice']
print(nairaToUsd)

# Get bitcoin to ngn exchange rate
btcToNgn = yahooFinance.Ticker("BTC-NGN")
print(btcToNgn.info['regularMarketPrice'])
