import tweepy
import yfinance as yahooFinance
from bitcoin_value import currency
from datetime import date
today = date.today()

#get blackmarket data
api_key = 'dNMdIu61K718jkO4OGN7QpP9o'
api_secret_key = 'nVQ7i66FqoZ8myaQtiMtRPNOF7imdWenogxy4xUVKOV6rpN4Fp'
access_token = '1316143421648785408-IvWxxGRZ5a6HaaHG1RbRpbaUuW932N'
access_token_secrets = 'lmcVhdf149zH3SQuE28V0oKt8kULRWtkF3QeSX76VrwPV'


# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secrets)
api = tweepy.API(auth, wait_on_rate_limit=True)

# get dollar to naira rate
#get euro to naira rate
euro_naira_rate = yahooFinance.Ticker("EURNGN=X").info['regularMarketPrice']
#get dollar to naira rate
dollar_naira_rate = yahooFinance.Ticker("USDNGN=X").info['regularMarketPrice']



# get ethereum dollar rate and convert to naira
ethereum_dollar_rate = yahooFinance.Ticker("ETH-USD").info['regularMarketPrice']
ethereum_naira_rate = ethereum_dollar_rate * dollar_naira_rate

# get bitcoin dollar rate and convert to naira
bitcoin_dollar_rate = currency("USD")
bitcoin_naira_rate = bitcoin_dollar_rate * dollar_naira_rate

# get bnb dollar rate and convert to naira
bnb_dollar_rate = yahooFinance.Ticker("BNB-USD").info['regularMarketPrice']
bnb_naira_rate = bnb_dollar_rate * dollar_naira_rate


#get solana dollar rate and convert to naira
solana_dollar_rate = yahooFinance.Ticker("SOL-USD").info['regularMarketPrice']
solana_naira_rate = solana_dollar_rate * dollar_naira_rate

# get usdt dollar rate and convert to naira
usdt_dollar_rate = yahooFinance.Ticker("USDT-USD").info['regularMarketPrice']
usdt_naira_rate = usdt_dollar_rate * dollar_naira_rate

# get doge dollar rate and convert to naira
doge_dollar_rate = yahooFinance.Ticker("DOGE-USD").info['regularMarketPrice']
doge_naira_rate = doge_dollar_rate * dollar_naira_rate

# get usdc dollar rate and convert to naira
usdc_dollar_rate = yahooFinance.Ticker("USDC-USD").info['regularMarketPrice']
usdc_naira_rate = usdc_dollar_rate * dollar_naira_rate

#get todays date


Dollar_rate = (f"1$ = ₦{dollar_naira_rate}")
Euro_rate = (f"1€ = ₦{euro_naira_rate} ")
Ethereum_rate = (f"1 Ethereum = ₦{ethereum_naira_rate} ")
Bitcoin_rate = (f"1 Bitcoin = ₦{bitcoin_naira_rate} ")
Bnb_rate = (f"1 BNB = ₦{bnb_naira_rate} ")
Solana_rate = (f"1 SOLANA = ₦{solana_naira_rate} ")
Usdt_rate = (f"1 USDT = ₦{usdt_naira_rate} ")
Doge_rate = (f"1 DOGE = ₦{doge_naira_rate} ")
Usdc_rate = (f"1 USDC = ₦{usdc_naira_rate} ")



# Create a tweet with dollar rate euro rate and ethereum rate and bitcoin rate and bnb rate and solana rate and usdt rate and doge rate and usdc rate with today's date

def post_tweet():
   tweets = api.user_timeline(screen_name = "watchingnaira")
   the_message = ("Todays Naira rate "f"{date.today()} \n {Dollar_rate} \n {Euro_rate} \n {Ethereum_rate} \n {Bitcoin_rate} \n {Bnb_rate} \n {Solana_rate} \n {Usdt_rate} \n {Doge_rate} \n {Usdc_rate}")
   api.update_status(the_message)




#post tweet
post_tweet()



