import flask
from flask import request  #获取参数
from flask_cors import CORS
from flask import Flask, render_template, request, make_response, jsonify, redirect
import requests
import os
import json


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



server = flask.Flask(__name__) #创建一个flask对象
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