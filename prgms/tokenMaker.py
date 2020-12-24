
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import RegexpTokenizer


import pandas as pd



def main():

    def tokenize(tweets):

        #word_tokens = word_tokenize(tweet)
        
        punct_tokenizer = WordPunctTokenizer()
       # punct_tokens = punct_tokenizer.tokenize(tweet)

        match_tokenizer = RegexpTokenizer("[\w']+")
        #match_tokens = match_tokenizer.tokenize(tweet)

        space_tokenizer = RegexpTokenizer("\s+", gaps=True)
        #space_tokens = space_tokenizer.tokenize(tweet)

        tweet_tokenizer = TweetTokenizer()
        #tweet_tokens = tweet_tokenizer.tokenize(tweet)

        punct_tokens = []
        match_tokens = []
        space_tokens = []
        tweet_tokens = []
        for tweet in tweets:
            punct_tokens.append(punct_tokenizer.tokenize(tweet))
            match_tokens.append(match_tokenizer.tokenize(tweet))
            space_tokens.append(space_tokenizer.tokenize(tweet))
            tweet_tokens.append(tweet_tokenizer.tokenize(tweet))







        tokenizers = {'WordPunctTokenize':punct_tokens,
             'RegrexTokenizer for matching':match_tokens,
             'RegrexTokenizer for white space': space_tokens,
             'TweetTokenizer': tweet_tokens }
        print(tokenizers)
        df = pd.DataFrame.from_dict(tokenizers)
        return df



    sampleTweet1 = "https://t.co/9z2J3P33Uc FB needs to hurry up and add a laugh/cry button 😬😭😓🤢🙄😱 Since eating my feelings"
    sampleTweet2 = "MAGA, keep trump in Office, dont let dirty dems take over #QAnon #PizzaGate"
    sampleTweet3 = '#QAanon tears apart families'
    tweetList = [sampleTweet1, sampleTweet2, sampleTweet3]
    df = tokenize(tweetList)
    df.to_csv('tokens.csv')


if __name__ == '__main__':
    main()