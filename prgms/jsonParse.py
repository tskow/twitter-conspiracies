import json
import csv
import pandas as pd




def parse(link, fileName):

    csvFile = open(fileName, 'a')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["created_at", "id", "user_id", "user_name", "screen_name", "location", "follower_count", "friend_count", "text", "retweet_count", "place_full_name", "hashtags", "user_mentions_screen_name", "user_mentions_id", 'in_reply_to_user_id', 'in_reply_to_screen_name', 'in_reply_to_screen_name', 'retweeted_screen_name', 'retweeted_status', 'retweeted_id', 'in_reply_to_status_id'])
    file = open(link)
    jsonData = []
    for line in file:
        json_line = json.loads(line)
        jsonData.append(json_line)

    for data in jsonData:

        if data['place'] is not None and len(data['entities']['hashtags']) > 0 and len(data['entities']['user_mentions']) > 0:
            csvWriter.writerow([data['created_at'], data['id'], data['user']['id'], data['user']['name'], data['user']['screen_name'],
             data['user']['location'], data['user']['followers_count'], data['user']['friends_count'], data['text'], data['retweet_count'],
             data['place']['full_name'], data['entities']['hashtags'][0]['text'], data['entities']['user_mentions'][0]['screen_name'],
             data['entities']['user_mentions'][0]['id'],data['in_reply_to_user_id'], data['in_reply_to_screen_name']])
        elif len(data['entities']['hashtags']) >0 and len(data['entities']['user_mentions']) > 0:
            csvWriter.writerow([data['created_at'], data['id'], data['user']['id'], data['user']['name'], data['user']['screen_name'], data['user']['location'], data['user']['followers_count'], data['user']['friends_count'], data['text'], data['retweet_count'], 'None', data['entities']['hashtags'][0]['text'], data['entities']['user_mentions'][0]['screen_name'], data['entities']['user_mentions'][0]['id'], data['in_reply_to_user_id'],data['in_reply_to_screen_name']])
        elif len(data['entities']['user_mentions']) > 0:
            csvWriter.writerow([data['created_at'], data['id'], data['user']['id'], data['user']['name'], data['user']['screen_name'], data['user']['location'], data['user']['followers_count'], data['user']['friends_count'], data['text'], data['retweet_count'], 'None', 'None', data['entities']['user_mentions'][0]['screen_name'], data['entities']['user_mentions'][0]['id'],data['in_reply_to_user_id'],data['in_reply_to_screen_name']])
        elif len(data['entities']['hashtags']) >0:
            csvWriter.writerow([data['created_at'], data['id'], data['user']['id'], data['user']['name'], data['user']['screen_name'], data['user']['location'], data['user']['followers_count'], data['user']['friends_count'], data['text'], data['retweet_count'], 'None', data['entities']['hashtags'][0]['text'], 'None', 'None',data['in_reply_to_user_id'],data['in_reply_to_screen_name']])
        elif data['place'] is not None:
            csvWriter.writerow([data['created_at'], data['id'], data['user']['id'], data['user']['name'], data['user']['screen_name'], data['user']['location'], data['user']['followers_count'], data['user']['friends_count'], data['text'], data['retweet_count'], data['place']['full_name'], "None", "None", "None",data['in_reply_to_user_id'],data['in_reply_to_screen_name']])
        else:
            csvWriter.writerow([data['created_at'], data['id'], data['user']['id'], data['user']['name'], data['user']['screen_name'], data['user']['location'], data['user']['followers_count'], data['user']['friends_count'], data['text'], data['retweet_count'], "None", "None", "None", "None",data['in_reply_to_user_id'],data['in_reply_to_screen_name']])
            




    #ex = jsonData[0]
    #print(ex['user']['friends_count'])
    #print(ex['followers_count'])


def main():

    
    link = 'twitter_premium_api_demo.json'
    link2 = 'twitter_premium_api_demo2.json'
    link3 = 'history_QAnon_300_2017.json'
    link4 = 'history_QAnon_300.json'



    parse(link, 'test1.csv')
    parse(link2, 'test2.csv')
    parse(link3, 'test3.csv')
    parse(link4, 'test4.csv')
    df = pd.read_csv("test1.csv")
    df2 = pd.read_csv('test2.csv')
    df3 = pd.read_csv("test3.csv")
    df4 = pd.read_csv("test4.csv")

    print(len(df))
    print(len(df2))
    print(len(df3))
    print(len(df4))

    df = pd.concat([df,df2])
    df = pd.concat([df,df3])
    df = pd.concat([df,df4])
    df.to_csv("data_subset.csv")
    df = pd.read_csv("data_subset.csv")
    print(df.columns)
    print(len(df))
    print(df.head(30))

    tweets_final = pd.DataFrame(columns = ["created_at", "id", "in_reply_to_screen_name", "in_reply_to_status_id", "in_reply_to_user_id",
                                      "retweeted_id", "retweeted_screen_name", "user_mentions_screen_name", "user_mentions_id", 
                                       "text", "user_id", "screen_name", "followers_count"])

if __name__ == '__main__':
    main()



