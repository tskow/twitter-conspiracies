
import tweepy
import csv
import pandas as pd
import datetime
from history import twitterHistory
from jsonParse import parse



def scrape(date):
    #wordlist =['#Qanon', '#TheGreatAwakening', '#qmapjapan', '#QArmyJapanFlynn', '#QArmyJapan', '#QArmy', '#QAJ','#missingChildren','#JusticelsComing', '#GreatAwakening','#FactsMatter', '#DeepState', '#DarkToLight', '#ChinaVirus', '#BillGatesIsEvil', '#AntifaTerrorists','#WWG1WG', 'qanon', 'thegreatawakening', 'greatawakening', 'qarmy', 'savethechildren', 'covid911', 'pizzagate', 'qanons', 'wayfairgate', 'flynn', 'anons', 'qarmyworldwide', 'mikeflynn', 'trump2q20', 'flynn2020', 'deepstatedems', 'wakeupamerica', 'qanon17', 'trump2q2q', 'obamagate']
    wordlist = ['#Qanon', '#TheGreatAwakening']
    for word in wordlist:
        filename = word + '_' + date + '.csv'
        json = twitterHistory(word+'_'+str(date), 50, date, word)
        parse(json, filename)


def main():
    #current_time = datetime.datetime.now()
    date = datetime.datetime(2016, 6, 1)
    date = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
    scrape(date)

if __name__ == '__main__':
    main()





