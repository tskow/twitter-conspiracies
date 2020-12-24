#handling data
import pandas as pd
import numpy as np
from scipy import stats
from operator import itemgetter


#handling information
import re
import json

#handling plots
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------------------------------------------------------------------------------------------------
# Script to extract features from JSON twitter data. 
# Can produce a Netorkx graph of twitter data using tweet data or can output a 
# CSV with node and edge relations between twitter users. To use add the name of the textfile which
# contains the JSON data you want to use. 
# This code was modified from a Medium article by Euge Inzaugarat
# Source: https://medium.com/future-vision/visualizing-twitter-interactions-with-networkx-a391da239af5
# -------------------------------------------------------------------------------------------------------------------------




def get_basics(tweets_final, tweets_df):
    tweets_final["screen_name"] = tweets_df["user"].apply(lambda x: x["screen_name"])
    tweets_final["user_id"] = tweets_df["user"].apply(lambda x: x["id"])
    tweets_final["followers_count"] = tweets_df["user"].apply(lambda x: x["followers_count"])
    return tweets_final

def get_usermentions(tweets_final,tweets_df):
    # Inside the tag 'entities' will find 'user mentions' and will get 'screen name' and 'id'
    tweets_final["user_mentions_screen_name"] = tweets_df["entities"].apply(lambda x: x["user_mentions"][0]["screen_name"] if x["user_mentions"] else np.nan)
    tweets_final["user_mentions_id"] = tweets_df["entities"].apply(lambda x: x["user_mentions"][0]["id_str"] if x["user_mentions"] else np.nan)
    return tweets_final

def get_retweets(tweets_final, tweets_df):
    # Inside the tag 'retweeted_status' will find 'user' and will get 'screen name' and 'id'    
    tweets_final["retweeted_screen_name"] = tweets_df["retweeted_status"].apply(lambda x: x["user"]["screen_name"] if x is not np.nan else np.nan)
    tweets_final["retweeted_id"] = tweets_df["retweeted_status"].apply(lambda x: x["user"]["id_str"] if x is not np.nan else np.nan)
    return tweets_final


# Get the information about replies
def get_in_reply(tweets_final, tweets_df):
    # Just copy the 'in_reply' columns to the new dataframe
    tweets_final["in_reply_to_screen_name"] = tweets_df["in_reply_to_screen_name"]
    tweets_final["in_reply_to_status_id"] = tweets_df["in_reply_to_status_id"]
    tweets_final["in_reply_to_user_id"]= tweets_df["in_reply_to_user_id"]
    return tweets_final

def fill_df(tweets_final, tweets_df):
    get_basics(tweets_final, tweets_df)
    get_usermentions(tweets_final, tweets_df)
    get_retweets(tweets_final, tweets_df)
    get_in_reply(tweets_final, tweets_df)
    return tweets_final

# Get the interactions between the different users
def get_interactions(row):
    # From every row of the original dataframe
    # First we obtain the 'user_id' and 'screen_name'
    user = row["user_id"], row["screen_name"]
    # Be careful if there is no user id
    if user[0] is None:
        return (None, None), []
    
    # The interactions are going to be a set of tuples
    interactions = set()
    
    # Add all interactions 
    # First, we add the interactions corresponding to replies adding the id and screen_name
    interactions.add((row["in_reply_to_user_id"], row["in_reply_to_screen_name"]))
    # After that, we add the interactions with retweets
    interactions.add((row["retweeted_id"], row["retweeted_screen_name"]))
    # And later, the interactions with user mentions
    interactions.add((row["user_mentions_id"], row["user_mentions_screen_name"]))
    
    # Discard if user id is in interactions
    interactions.discard((row["user_id"], row["screen_name"]))
    # Discard all not existing values
    interactions.discard((None, None))
    # Return user and interactions
    return user, interactions

def main():

    pd.set_option('display.float_format', lambda x: '%.f' % x)

    tweets_df = pd.read_json("all_data3.txt", lines=True, encoding="utf8")

    tweets_final = pd.DataFrame(columns = ["created_at", "id", "in_reply_to_screen_name", "in_reply_to_status_id", "in_reply_to_user_id",
                                      "retweeted_id", "retweeted_screen_name", "user_mentions_screen_name", "user_mentions_id", 
                                       "text", "user_id", "screen_name", "followers_count"])
    equal_columns = ["created_at", "id", "text"]
    tweets_final[equal_columns] = tweets_df[equal_columns]
    tweets_final = fill_df(tweets_final, tweets_df)
    tweets_final = tweets_final.fillna('None')
    tweets_final = tweets_final.where((pd.notnull(tweets_final)), None)
    print(tweets_final.head())
    for col in tweets_final.columns: 
       print(col) 
    print('number of row: ')
    print(len(tweets_final.index))
    df_final = pd.DataFrame(columns = ['souce', 'target'])
    i = 0
    for row in tweets_final.iterrows():
        if (i % 100 ==0):
            print(i)
        i = i +1
        #print(row[1])
        #print(1)
        if row[1]['in_reply_to_screen_name'] != 'None':
            #df2 = {'source': row[1]['screen_name'], 'target': row[1]['in_reply_to_screen_name']}
            #df_final = df_final.append(df2, ignore_index=True)
            df_final.loc[len(df_final.index)] = [row[1]['screen_name'], row[1]['in_reply_to_screen_name']]
        if row[1]['retweeted_screen_name'] != 'None':
            #df2 = {'source': row[1]['screen_name'], 'target': row[1]['retweeted_screen_name']}
            #df_final = df_final.append(df2, ignore_index=True)
            df_final.loc[len(df_final.index)] = [row[1]['screen_name'], row[1]['retweeted_screen_name']]

        if row[1]['user_mentions_screen_name'] != 'None':
           # df2 = {'source': row[1]['screen_name'], 'target': row[1]['user_mentions_screen_name']}
            #df_final = df_final.append(df2, ignore_index=True)
            df_final.loc[len(df_final.index)] = [row[1]['screen_name'], row[1]['user_mentions_screen_name']]

    print('done')

    
    print(df_final.head)
    print(len(df_final.index))
    df_final.to_csv('gephi_df3.csv') 










if __name__ == '__main__':
    main()
