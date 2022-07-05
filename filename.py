import tweepy
import pandas as pd
import sqlalchemy as db
import datetime


# GOAL: have user input date from past 7 days to get tweets from that day
# your bearer token
MY_BEARER_TOKEN = ("AAAAAAAAAAAAAAAAAAAAAMMDeQEAAAAAMz660hdSEQZjQmiJmZj"
                   "9soNCmqw%3DMY3CJ67dLS0EYWqTcVjLPYt3bzuhAyNTPFl8S7"
                   "O2LaWNIoJjnB")

# create your client with bearer_token
client = tweepy.Client(bearer_token=MY_BEARER_TOKEN)


def get_date():
    try:
        user_date = input("Enter the date you want tweets from past"
                          "7 days(in MM/DD/YYYY):")
        date = datetime.datetime.strptime(user_date, "%m/%d/%Y").date()
        print("Searching tweets from " + str(date))
        return date
    except ValueError:
        print("You did not form the date correctly. Please insert the month " +
              "then the day then the year.")
        get_date()


# simply a string that tells the Twitter API what kind of tweets
# you want to search for
search_query = "#covid19 -in:retweets"

# query to search for tweets
query = "#covid19 lang:en -is:retweet"

# your start and end time for fetching tweets
# start_time = "2022-06-29T00:00:00Z"
# end_time = "2022-06-30T00:00:00Z"

# get tweets from the API
# would test if function only returns requested information in dict format


def get_tweets():
    date = get_date()
    start_time = str(date) + "T00:00:00Z"
    end_time = str(date + datetime. timedelta(days=1)) + "T00:00:00Z"
    try:
        tweets = client.search_recent_tweets(query=query,
                                             start_time=start_time,
                                             end_time=end_time,
                                             tweet_fields=["created_at",
                                                           "text",
                                                           "source"],
                                             user_fields=["name",
                                                          "username",
                                                          "location",
                                                          "verified",
                                                          "description"],
                                             max_results=10,
                                             expansions='author_id')

        return tweets
    except tweepy.errors.BadRequest:
        print("Invalid Tweet Request. Inputted date is not from",
              "the past 7 days")

# tweet specific info
# print(len(tweets.data))
# user specific info
# print(len(tweets.includes["users"]))

# first tweet
# first_tweet = tweets.data[0]
# print(dict(first_tweet))

# create a dict of records
# check the format of the tweet dictionary so that the keys say the
# kind of information and the correct values are obtained
# also test if only 10 tweets are returned


def create_tweet_dict(tweets):
    if tweets == None:
      return None
    tweet_info_dict = {}
    count = 0

    # iterate over each tweet and corresponding user details
    for tweet, user in zip(tweets.data, tweets.includes['users']):
        tweet_val = [tweet.created_at, user.username, user.description]
        tweet_info_dict[count] = tweet_val
        count += 1
    return tweet_info_dict

# create dataframe from the extracted records
# Test if created database table is formated correctly with properly named
# columns and rows with the correct infomation places in each


def create_database(tweet_info_dict):
    if tweet_info_dict == None:
      return None
    # create dataframe from the extracted records
    tweets_df2 = pd.DataFrame.from_dict(tweet_info_dict, orient='index',
                                        columns=['creates_at', 'username',
                                                 'description'])
    # print(tweets_df2)

    # creating a database from dataframe
    engine = db.create_engine('sqlite:///data_base_name.db')
    tweets_df2.to_sql('tweet_info_dict', con=engine, if_exists='replace',
                      index=False)
    query_result = engine.execute("SELECT * FROM tweet_info_dict;").fetchall()
    return query_result


# Testing Code
if __name__ == "__main__":
    # print(len(get_tweets()))
    # print(type(get_tweets()))
    # get_date()
    tweets = get_tweets()
    tweet_info_dict = create_tweet_dict(tweets)
    query_result = create_database(tweet_info_dict)
    print((pd.DataFrame(query_result)))


# print(pd.DataFrame(query_result))

# print(dict(first_tweet))


# codio@pythonhope-scriptjester:~/workspace$
