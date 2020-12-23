import tweepy
import csv
import pandas as pd
import datetime
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

# -------------------------------------------------------------------------------------------------------------------------
# Script to takes JSON twitter meta data of tweets and creates a CSV
# file containing all of the closest friends of the user that made a given tweet
# Author: Tyler Skow  
# -------------------------------------------------------------------------------------------------------------------------


def getUserMetaData(id):
    user = api.get_user(id=id)
    followers_count = user.followers_count
    friends_count = user.friends_count
    statuses_count = user.statuses_count
    location = user.location
    screen_name = user.screen_name
    user_id = user.id
    return followers_count, friends_count, statuses_count, location, screen_name, user_id

def getUserFriendList(id, csvWriter):
    freinds = api.friends(id=id)
    res = []
    for friend in freinds:
        temp = []
        followers_count, friends_count, statuses_count, location, screen_name, user_id =  getUserMetaData(friend.id)

        csvWriter.writerow([user_id,screen_name,followers_count,friends_count,statuses_count,location ])


def main():

    ids = []
    file = open('history.json')


    csvFile = open("user_meta_data.csv", 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["user_id", "screen_name", "followers_count", "friends_count", "statuses_count", "location"])

    i = 0
    j = 0
    for line in file:
        json_line = json.loads(line)
        id = json_line['user']['id']
        if id not in ids:
            print(str(i) + "/" + str(j))
            ids.append(id)
            try:
                followers_count, friends_count, statuses_count, location, screen_name, user_id = getUserMetaData(id)
                csvWriter.writerow([user_id,screen_name,followers_count,friends_count,statuses_count,location ])
            except Exception as e:
                print(e)
            i +=1
        j +=1



if __name__ == '__main__':
    main()