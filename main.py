from flask import Flask, render_template, request, jsonify
import praw
import base64
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

reddit = praw.Reddit('BestBuyBot')
mods = []
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
@limiter.limit("20 per day")
def process():
	link_list =[]
	title_list =[]
	comment_list=[]
	subName = request.form['name']
	subtype = request.form ['type']
	if subName and subtype:
			if subtype == 'hot':
				subreddit = reddit.subreddit(subName).hot(limit=30)
			elif subtype == 'new':
				subreddit = reddit.subreddit(subName).new(limit=30)
			elif subtype == 'rising':
				subreddit = reddit.subreddit(subName).rising(limit=30)
			else:
				print('Something went wrong, unknown subtype: {}'.format(subtype))
				raise

			for submission in subreddit: 
						url = submission.url
						if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
							link_list.append(url)
							title_list.append(submission.title)				
							print("---------------------------------\n")
			return jsonify({'name' : link_list, 'title' : title_list } )		
	return jsonify({'error' : 'Missing data!'})



if __name__ == '__main__':
	    app.run(debug=True)