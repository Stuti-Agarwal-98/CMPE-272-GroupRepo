from flask import Flask, render_template, request, redirect
import tweepy
from local_config import *

app = Flask(__name__)

# HTML code by Tripura
# Code by Stuti
@app.route('/')
def retrieve_user_tweets():

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	Retrieve = request.args.get('q')
	public_tweets = api.user_timeline(Retrieve)

	return render_template('home.html', tweets=public_tweets)

# Code by Haley
@app.route('/tweet', methods=['POST','GET'])
def post_tweet():
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	if request.method == 'POST':
		Create = request.form['Tweet']
		post = api.update_status(Create)
		return redirect('/')
	else:
		return render_template('home.html')

# Code by Haley
@app.route('/delete_tweet', methods=['POST','GET'])
def del_tweet():
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	if request.method == 'POST':
		Delete_Tweet = request.form['Tweet']
		del_part = Delete_Tweet.rpartition('/')
		status_id = del_part[2]
		api.destroy_status(status_id)
		return redirect('/')
	else:
		return render_template('home.html')	

# Code by Stuti
@app.route('/delete_all')
def del_all():
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	user_tweets = api.user_timeline
	print(user_tweets)
	for status in tweepy.Cursor(user_tweets).items():
		try:
			api.destroy_status(status.id)
			print("Deleted:", status.id)
		except:
			print("Failed to delete:", status.id)
			return render_template('home.html')	
	return redirect('/')


if __name__=='__main__':
	app.run(debug=True)

    