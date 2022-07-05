# SEOTECHSUMMER
gt1. **Setup instructions**
    * NEED TO HAVE TWITTER DEVELOPER ACCOUNT
    * Libraries to Install
      * python twitter API: tweepy
      * install pandas as pd
    * Environment Variables
      * MY_BEARER_TOKEN which is your 
        bearer token given from twitter account
        * You're bearer token is used to create 
          a client using tweepy 

2. **How to run code**
   * Type python3 filename.py to run code
   * This code requires user input 
   * The input required is a date from the past 
     7 days in the form of MM/DD/YYYY
     * If date is not formatted correctly a 
       message with display 
  
3. **An overview of how your code works**
    This code uses user input to obtain a date 
    from the past 7 days. It uses the input to 
    collect the at most 10 tweets from that date.
    The data returned is the date and time the 
    tweet was created, the username of the person
    who posted the tweet and a short description 
    of the tweet