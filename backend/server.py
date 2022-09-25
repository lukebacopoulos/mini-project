﻿import flask
from flask import request  #获取参数
from flask_cors import CORS
from flask import Flask, render_template, request, make_response, jsonify, redirect



server = flask.Flask(__name__) #创建一个flask对象
CORS(server)
@server.route('/login', methods=['get','post'])
def login():
    name = request.values.get('username') #获取参数
    if name:
        #sql = 'select User from user where User="%s"'%username
        #data = conn_mysql(sql)     
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
    return user_sentiments;
            



server.run(port=5000,debug=True)