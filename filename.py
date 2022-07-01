import tweepy

# your bearer token
MY_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAMMDeQEAAAAAMz660hdSEQZjQmiJmZj9soNCmqw%3DMY3CJ67dLS0EYWqTcVjLPYt3bzuhAyNTPFl8S7O2LaWNIoJjnB"
# create your client 
client = tweepy.Client(bearer_token=MY_BEARER_TOKEN)

search_query = "#covid19 -in:retweets"

# query to search for tweets
query = "#covid19 lang:en -is:retweet"

# your start and end time for fetching tweets
start_time = "2022-06-29T00:00:00Z"
end_time = "2022-06-30T00:00:00Z"

# get tweets from the API
tweets = client.search_recent_tweets(query=query,
                                     start_time=start_time,
                                     end_time=end_time,
                                     tweet_fields = ["created_at", "text", "source"],
                                     user_fields = ["name", "username", "location", "verified", "description"],
                                     max_results = 10,
                                     expansions='author_id'
                                     )

# tweet specific info
print(len(tweets.data))
# user specific info
print(len(tweets.includes["users"]))

# first tweet
first_tweet = tweets.data[0]
print(dict(first_tweet))


#codio@pythonhope-scriptjester:~/workspace$ 

'''
from pytwitter import Api


api = Api(bearer_token="AAAAAAAAAAAAAAAAAAAAAMMDeQEAAAAAMz660hdSEQZjQmiJmZj9soNCmqw%3DMY3CJ67dLS0EYWqTcVjLPYt3bzuhAyNTPFl8S7O2LaWNIoJjnB")

api.get_tweet("1354143047324299264", expansions=["attachments.media_keys"], media_fields=["type","duration_ms"])
Response(data=Tweet(id=1354143047324299264, text="Academics are one of the biggest groups using..."))




import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("AAAAAAAAAAAAAAAAAAAAAMMDeQEAAAAAMz660hdSEQZjQmiJmZj9soNCmqw%3DMY3CJ67dLS0EYWqTcVjLPYt3bzuhAyNTPFl8S7O2LaWNIoJjnB")


def create_url():
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    usernames = "usernames=TwitterDev,TwitterAPI"
    user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
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


def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()
#next attempt


from pytwitter import Api


api = Api(bearer_token="AAAAAAAAAAAAAAAAAAAAAMMDeQEAAAAAMz660hdSEQZjQmiJmZj9soNCmqw%3DMY3CJ67dLS0EYWqTcVjLPYt3bzuhAyNTPFl8S7O2LaWNIoJjnB")

api.get_tweet("1354143047324299264", expansions=["attachments.media_keys"], media_fields=["type","duration_ms"])
Response(data=Tweet(id=1354143047324299264, text="Academics are one of the biggest groups using..."))


# import requests
# import os
# import json
# #import pandas as pd
# import csv
# import datetime
# import dateutil.parser
# import unicodedata
# import time

#client secret = Dtyv2Ti5Ow6IjxUV9Ze9gLsQI6MMSMLO20FWjmx47oH7p_Aq_c
os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAMMDeQEAAAAAMz660hdSEQZjQmiJmZj9soNCmqw%3DMY3CJ67dLS0EYWqTcVjLPYt3bzuhAyNTPFl8S7O2LaWNIoJjnB'
def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)
    #url = https://twitter.com/TwitterDev

#checks status. Desired result: response code 200
def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

#Inputs for the request
bearer_token = auth()
headers = create_headers(bearer_token)
keyword = "xbox lang:en"
start_time = "2021-03-01T00:00:00.000Z"
end_time = "2021-03-31T00:00:00.000Z"
max_results = 15

url = create_url(keyword, start_time,end_time, max_results)
json_response = connect_to_endpoint(url[0], headers, url[1])
print(json.dumps(json_response, indent=4, sort_keys=True))

import requests
import os
import json
import tweepy
os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAMMDeQEAAAAAQCG2jArvbj12WGClQ%2BKn5QKcuOk%3Dr3SVl396F5YiJFcJA3WOXixfRO33gCoRIKyBX8xrSvwf6Mvum4'

url = "https://stream.twitter.com/1/statuses/sample.json"

auth = {'username': 'username', 'password': 'password'}
r = requests.get("https://stream.twitter.com/1/statuses/sample.json", params=auth)
print(r.status_code)



def auth():
    return os.getenv('TOKEN')



def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)


def connect_to_endpoint(url, headers, params, next_token = None):
    params['next_token'] = next_token   #params object received from create_url function
    response = requests.request("GET", url, headers = headers, params = params)
    print("Endpoint Response Code: " + str(response.status_code))
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

url = create_url(keyword, start_time,end_time, max_results)
json_response = connect_to_endpoint(url[0], headers, url[1])

print(json.dumps(json_response, indent=4, sort_keys=True))

CLIENT_ID = 'PZZZXrXDYYinlE0LtTRQrfEpq'
CLIENT_SECRET= '6YGG5XzTPODCbIdFRPGI58SopwcKFrg6a5ywZNZq3Uor9c2QSL'

AUTH_URL = 'https://api.twitter.com/oauth/authorize'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}




      
curl -u "PZZZXrXDYYinlE0LtTRQrfEpq:6YGG5XzTPODCbIdFRPGI58SopwcKFrg6a5ywZNZq3Uor9c2QSL" \
  --data 'grant_type=client_credentials' \
  'https://api.twitter.com/oauth2/token'


      
curl "https://api.twitter.com/2/tweets?ids=1261326399320715264,1278347468690915330" \
  -H "Authorization: Bearer AAAAAAAAAAAAAAAAAAAAAMMDeQEAAAAA4p71COrAvPc0LStkr10f2eG258I%3Dyr3zOmQTjNnBnnr01JH7Hp9DMoQAU2t2OYmspWouuO52PWoJy1"

    
'''