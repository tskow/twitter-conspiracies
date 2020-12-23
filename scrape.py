import tweepy
import csv
import pandas as pd
import datetime
import json

# -------------------------------------------------------------------------------------------------------------------------
# Script to queries twitter API with given seed words below. 
# Can scrape raw JSON or in CSV format
# Author: Tyler Skow  
# -------------------------------------------------------------------------------------------------------------------------


path = '/Documents/THESIS/prgms/datascrape'

def save_json(file_name, file_content):
  with open(path + file_name, 'w', encoding='utf-8') as f:
    json.dump(file_content, f, ensure_ascii=False, indent=4)

def scrape(fileName, query):
    consumer_key = 'BohsdeC0vtoBunjl0kc9Kzdb3'
    consumer_secret = 'e5wyAIQpVRGHMsRjoEif1QBtc7w4m0AHi0hcW2LX9zjNl8sZSO'
    access_token = '1300899730713526274-DSRQsmwrRRA8o5zcwupz5ZZJCjWnC7'
    access_token_secret = 'O9vGd2Wqi2csXX1L1mQ7R51DZTcZy3bB2Tk6MOM8JYQb4'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)
    f = open(fileName, "a")

    #csvFile = open(fileName, 'a')
    #csvWriter = csv.writer(csvFile)
    #csvWriter.writerow(["created_at", "id", "user_id", "user_name", "screen_name", "location", "follower_count", "friend_count", "text",
    # "retweet_count", "place_full_name", "hashtags", "user_mentions_screen_name", "user_mentions_id", 'in_reply_to_user_id',
    #  'in_reply_to_screen_name', 'retweeted_screen_name', 'retweeted_status', 'retweeted_id', 'in_reply_to_status_id'])
    i =1
    for tweet in tweepy.Cursor(api.search,q=query,count=1000 ,lang="en", since="2020-10-27").items():
        #print(tweet._json)
        #json_str = json.dumps(tweet[0]._json)
        #json.dump(tweet, f)
        #print(json.dumps(tweet._json))
        f.write(json.dumps(tweet._json))
        f.write('\n')
        if (i == 400):
            break
        i+=1
    """ for tweet in tweepy.Cursor(api.search,q=query,count=10,lang="en", since="2020-10-27").items():
        f.write(tweet)
        print(tweet.text)
        i += 1
        if tweet.place is not None and len(tweet.entities["hashtags"]) != 0 and len(tweet.entities["user_mentions"]) !=0:
            csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location,
             tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, tweet.place.full_name, tweet.entities['hashtags'][0]['text'],
              tweet.entities['user_mentions'][0]['screen_name'], tweet.entities['user_mentions'][0]['id'], tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name,
               tweet.retweeted_status['user']['screen_name'], tweet.in_reply_to_status_id])


        elif len(tweet.entities["hashtags"]) != 0 and len(tweet.entities["user_mentions"]) !=0:
            csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, "None", tweet.entities['hashtags'][0]['text'], tweet.entities['user_mentions'][0]['screen_name'], tweet.entities['user_mentions'][0]['id'], tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name, tweet.retweeted_status, tweet.in_reply_to_status_id])
        elif len(tweet.entities["user_mentions"]) !=0:
            csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, "None", "None", tweet.entities['user_mentions'][0]['screen_name'], tweet.entities['user_mentions'][0]['id'], tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name, tweet.retweeted_status, tweet.in_reply_to_status_id])

        elif len(tweet.entities["hashtags"]) != 0:
            csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, "None", tweet.entities['hashtags'][0]['text'], "None", "None", tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name, tweet.retweeted_status, tweet.in_reply_to_status_id])

        elif tweet.place is not None:
            csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, tweet.place.full_name, "None", "None", "None", tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name, tweet.retweeted_status, tweet.in_reply_to_status_id])

        else:
            csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, "None", "None", "None", "None", tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name, tweet.retweeted_status, tweet.retweeted_id, tweet.in_reply_to_status_id])
      #  elif tweet.entities.user_mentions is not None:
       #     csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, 'None', "None", tweet.entities.user_mentions_screen_name, tweet.entities.user_mentions_id, tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name])
       # elif tweet.entities.hashtags is not None:
       #     csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, "None", tweet.entities.hashtags.text, "None", "None", tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name])
       # elif tweet.place is not None:
       #     csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, tweet.place.full_name, "None", "None", "None", tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name])
      #  else:
       #     csvWriter.writerow([tweet.created_at, tweet.id, tweet.user.id, tweet.user.name, tweet.user.screen_name, tweet.user.location, tweet.user.followers_count, tweet.user.friends_count, tweet.text, tweet.retweet_count, "None", "None", "None", "None", tweet.in_reply_to_user_id, tweet.in_reply_to_screen_name])

 """
def main():
    current_time = datetime.datetime.now()

#'#QAnon', '#Trump2020',
    #wordlist =['#QAnon','#TheGreatAwakening', '#qmapjapan', '#QArmyJapanFlynn', '#QArmyJapan', '#QArmy', '#QAJ','#missingChildren','#JusticelsComing', '#GreatAwakening','#FactsMatter']
    wordlist =['#Qanon', '#DeepState', '#DarkToLight', '#ChinaVirus', '#BillGatesIsEvil', '#AntifaTerrorists','#WWG1WG', 'qanon','thegreatawakening', 'greatawakening', 'qarmy', 'savethechildren', 'covid911', 'pizzagate', 'qanons', 'wayfairgate', 'flynn', 'anons', 'qarmyworldwide', 'mikeflynn', 'trump2q20', 'flynn2020', 'deepstatedems', 'wakeupamerica', 'qanon17', 'trump2q2q', 'obamagate']
    wordlist2 = ['#Qanon', '#WWG1WGA', "where we go one, we go all", "#voterfraud", '#DeepState', '#DarkToLight', '#ChinaVirus', '#BillGatesIsEvil', '#AntifaTerrorists','#WWG1WG', 'qanon', 'thegreatawakening', 'greatawakening', 'qarmy', 'savethechildren', 'covid911', 'pizzagate', 'qanons', 'wayfairgate', 'flynn', 'anons', 'qarmyworldwide', 'mikeflynn', 'trump2q20', 'flynn2020', 'deepstatedems', 'wakeupamerica', 'qanon17', 'trump2q2q', 'obamagate']
    wordlist3 = ['#BidenHarris2020']
    #wordlist3 = ['#Trump2020']
    #wordlist = ['#QAnon']

    wordlist4 = ['#cooking', '#covid19', "#cats"]
    #wordlist = ['#StankyTrump']
    for word in wordlist:
        fileName = word + '-' + str(current_time.day) +'-'+ str(current_time.month) + '.json'
        scrape(fileName, word)
        print(word)

if __name__ == '__main__':
    main()