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
	for submission in subreddit.hot(limit=3): 
		url = submission.url
		if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
			#response = requests.get(submission.url)
			#encoded_image = base64.b64encode(response.content)
			#decoded_image= base64.b64decode(encoded_image)
			link_list.append(url)
			print(link_list)
	return jsonify({'name' : link_list})

if __name__ == '__main__':
	app.run(debug=True)