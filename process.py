from flask import Flask, render_template, request, jsonify
import praw
import base64
import requests

app = Flask(__name__)
reddit = praw.Reddit('BestBuyBot')
mods = []

@app.route('/')
def index():
	return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
	link_list =[]
	title_list =[]
	comment_list=[]
	subName = request.form['name']
	subreddit = reddit.subreddit(subName)
	for submission in subreddit.hot(limit=20): 
		url = submission.url
		if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
			link_list.append(url)
			title_list.append(submission.title)
			print(link_list)
			print("---------------------------------\n")
	return jsonify({'name' : link_list, 'title' : title_list } )

if __name__ == '__main__':
	app.run(debug=True)