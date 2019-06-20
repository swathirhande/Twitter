import json
import oauth2 as oauth

consumer_key="OYg34O4XmvT58kbpagoUqjF2z"
consumer_secret ="OhluPlDkMBHKABgeQ9l4U9lDpfaLls5Hmtde5B216L0JlA2FHo"

access_token="1141570538931773440-283nrdpicaMoiEEJ49dQoup4jzDEH6"
access_token_secret="0A0YlxyEdousb0EjZqiLdJnmt9IePWD3Gaw8gidkSEbv1"

consumer= oauth.Consumer(key=CONSUMER_KEY,secret=consumer_secret)
access_token =oauth.Token(key=ACCESS_KEY,secret=access_secret)
client=oauth.Client(consumer,access_token)

timeline_endpoint="https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=Socioauth&count=1"

response,data=cient.request(timeline_endpoint)

tweets=json.loads(data)
for tweet in tweets:
	print data
