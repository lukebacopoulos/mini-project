import flask
from flask import request  #获取参数
from flask_cors import CORS
from flask import Flask, render_template, request, make_response, jsonify, redirect
import requests
import os
import json
import botometer
import tweepy as tw 
my_api_key = "Dz9ACU3Urp1ynBZ4730uWbPEm";
my_api_secret = "405TgoVjxfiYynmiJQvspCDGBWXaRJOiIKE9me1Lb7m7TDUYgb";
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = "@KyrieIrving";
tweets = tw.Cursor(api.search,
              q=search_query,
              lang="en",
              since="2020-09-16").items(50)
tweets_copy=[];
for tweet in tweets:
    tweets_copy.append(tweet)

#print(api.get_status(id=tweet.id, tweet_mode='extended').full_text);

#rapidapi_key = "622309e583msh5b2a10deeab0445p1135f1jsna197ab950dcc"
#twitter_app_auth = {
#    'consumer_key': 'Dz9ACU3Urp1ynBZ4730uWbPEm',
#    'consumer_secret': '405TgoVjxfiYynmiJQvspCDGBWXaRJOiIKE9me1Lb7m7TDUYgb',
#    'access_token': '1569461659487600641-bLKNe5yY4ok1Pby4byqCc0rDfab6TU',
#    'access_token_secret': '6VkaJxAghcWXPk4eZ6gDGlb3VMrn09eiN7md8URjwliz3',
#  }
#bom = botometer.Botometer(wait_on_ratelimit=True,
#                          rapidapi_key=rapidapi_key,
#                          **twitter_app_auth)

# Check a single account by screen name
#result = bom.check_account('@clayadavis')
#print(result);


bearer_token = "AAAAAAAAAAAAAAAAAAAAABgPhAEAAAAA9lRkuEbxjkaNynlZbod17t4OkzU%3DDVpStDdxPwwHomYeaW4JvYKRJpdHfpvuOjkWiXTL8E89D3KrUI"

def create_url(user_names_list, user_fields ):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    user_names = ','.join(user_names_list) if len(user_names_list)>1 else user_names_list[0]
    
    usernames = f"usernames={user_names}"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    print(url)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()



server = flask.Flask(__name__) 
CORS(server)
@server.route('/login', methods=['get','post'])
def login():
    name = request.values.get('username');
    users_list = [name];
    user_fields  = "user.fields=description,created_at,public_metrics"
    url = create_url(users_list,user_fields)
    json_response = connect_to_endpoint(url)

        
    return json.dumps(json_response, indent=4, sort_keys=True);
            

server.run(port=5000,debug=True)