import tweepy
import time

auth = tweepy.OAuthHandler('6NXt9LkialoXMYDM4vqjqFHzg','4Z2GjKSakYLN6F8aTQ2KraR217LNV74aFVlLmKsPCdmP4htA9W')
auth.set_access_token('1345866207107407872-CnDstYyH9vC5fkGHswtqTkFaCZxUPu','3NZ5w3aRhqnxxAPhTsScpbwTjhFGLL73SLwHbMltu86T0')


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = ('não aguento mais', 'nao aguento mais')
numeroDeTweets = 2000

for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        print('tweet retuitado e favoritado')
        tweet.retweet()
        time.sleep(90)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
