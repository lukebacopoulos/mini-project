from flask import Flask, render_template, request, make_response, jsonify, redirect
import requests
from flask_cors import CORS
# Initializing flask app
app = Flask(__name__)
CORS(app);
  
# Route for seeing a data



@app.route('/hi', methods=['GET'])
def get_user_info():
    name=str(request.values.get('username'));
    url = "https://api.twitter.com/2/users/by/username/" + name
    payload = {}
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAOHIhAEAAAAAkAZC7Y3JaJF7qPpTvej%2BUZpMPjs%3DUAcdjPQKFpDcdKDc3PHzGRRf42iJf5OkrO8nHi4ZaENMg9agxu',
        'Cookie': 'guest_id=v1%3A166361425689819565'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    user_data = response.json()["data"]
    user_id = response.json()['data']['id']
    url = "https://api.twitter.com/2/users/" + str(user_id) + "/tweets"
    payload = {}
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAOHIhAEAAAAAkAZC7Y3JaJF7qPpTvej%2BUZpMPjs%3DUAcdjPQKFpDcdKDc3PHzGRRf42iJf5OkrO8nHi4ZaENMg9agxu',
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    user_tweets = response.json()['data']
    user_tweets_text = []
    user_tweets_score = []

    user_tweets_data = user_tweets
    num_tweets = 0
    user_sentiments = []
    for tweet in user_tweets_data:
        num_tweets += 1

        sentiment = analyze_text_sentiment(tweet['text'])
        # user_tweets_sentiment[str(num_tweets)] = sentiment
        user_tweets_text.append(sentiment['text'])
        user_tweets_score.append(sentiment['score'])
        tring = [sentiment['text'],sentiment['score']]
        user_sentiments.append(tring)
    return jsonify(user_sentiments)
  
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)