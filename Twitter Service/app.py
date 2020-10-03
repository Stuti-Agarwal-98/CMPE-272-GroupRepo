from flask import Flask, render_template, request, redirect
import tweepy


consumer_key = 
consumer_secret = 
access_token = 
access_token_secret = 

app = Flask(__name__)

@app.route('/')
def index():
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	Retrieve = request.args.get('q')
	public_tweets = api.user_timeline(Retrieve)
	
	#status_id = new_status.id #get the id of tweet
	#api.destroy_status(status_id)	

	return render_template('home.html', tweets=public_tweets)


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

def del_tweet():
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	if request.method == 'POST':
		Create = request.form['Tweet']
		post = api.update_status(Create)
		return redirect('/')
	else:
		return render_template('home.html')

if __name__=='__main__':
	app.run(debug=True)

    