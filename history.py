
# -------------------------------------------------------------------------------------------------------------------------
# This codes scapes historical data from Twitter's API. To use
# you must obtain Twitter credientials which can be obtained by through Twitter's developer portal. 
# This code was modified from Luca Hammer
# Source: https://lucahammer.com/2019/11/05/collecting-old-tweets-with-the-twitter-premium-api-and-python/
# -------------------------------------------------------------------------------------------------------------------------


def twitterHistory(filename, nresults, date=None, searchQuery=None):
    
    API_KEY = 'BohsdeC0vtoBunjl0kc9Kzdb3'
    API_SECRET_KEY = 'e5wyAIQpVRGHMsRjoEif1QBtc7w4m0AHi0hcW2LX9zjNl8sZSO'
    DEV_ENVIRONMENT_LABEL = 'dev'
    API_SCOPE = '30day'  # 'fullarchive' for full archive, '30day' for last 31 days

    SEARCH_QUERY = 'flynn'
    RESULTS_PER_CALL = 100  # 100 for sandbox, 500 for paid tiers
    TO_DATE = '2020-12-15' # format YYYY-MM-DD HH:MM (hour and minutes optional)
    FROM_DATE = '2020-11-16'  # format YYYY-MM-DD HH:MM (hour and minutes optional)

    MAX_RESULTS = 999  # Number of Tweets you want to collect

    FILENAME = filename  # Where the Tweets should be saved

    # Script prints an update to the CLI every time it collected another X Tweets
    PRINT_AFTER_X = 1000

    #--------------------------- STOP -------------------------------#
    # Don't edit anything below, if you don't know what you are doing.
    #--------------------------- STOP -------------------------------#

    import yaml
    import csv

    config = dict(
        search_tweets_api=dict(
            account_type='premium',
            endpoint=f"https://api.twitter.com/1.1/tweets/search/{API_SCOPE}/{DEV_ENVIRONMENT_LABEL}.json",
            consumer_key=API_KEY,
            consumer_secret=API_SECRET_KEY
        )
    )

    with open('twitter_keys.yaml', 'w') as config_file:
        yaml.dump(config, config_file, default_flow_style=False)

        
    import json
    from searchtweets import load_credentials, gen_rule_payload, ResultStream

    premium_search_args = load_credentials("twitter_keys.yaml",
                                        yaml_key="search_tweets_api",
                                        env_overwrite=False)

    rule = gen_rule_payload(SEARCH_QUERY,
                            results_per_call=RESULTS_PER_CALL,
                            from_date=FROM_DATE,
                            to_date=TO_DATE
                            )

    rs = ResultStream(rule_payload=rule,
                    max_results=MAX_RESULTS,
                    **premium_search_args)

    csvFile = open('testing', 'a')
    csvWriter = csv.writer(csvFile)

    with open(FILENAME, 'a', encoding='utf-8') as f:
        n = 0
        for tweet in rs.stream():
            
            #print(tweet)
            n += 1
            if n % PRINT_AFTER_X == 0:
                print('{0}: {1}'.format(str(n), tweet['created_at']))
            json.dump(tweet, f)
            f.write('\n')
    return f
    print('done')

def main():
    twitterHistory('#WWG1WGA_30_day2_flyn.json', 2)

if __name__ == '__main__':
    main()