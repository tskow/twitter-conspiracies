from city_to_state import city_to_state_dict
import us
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------------------------------------------------------
# Script that recodes self reported location of tweet to 1 of 50 US states. 
# This code was modified from a Medium article by Krish
# Source: https://medium.com/swlh/extracting-location-data-from-twitter-54c837144038  
# -------------------------------------------------------------------------------------------------------------------------


two_word_states = {
    "New Hampshire": "New Hampshire",
    "New Jersey": "New Jersey",
    "New York": "New York",
    "New Mexico": "New Mexico",
    "North Carolina": "North Carolina",
    "North Dakota": "North Dakota",
    "Rhode Island":"Rhode Island",
    "South Carolina":"South Carolina",
    "South Dakota":"South Dakota",
    "West Virginia":"West Virginia"
}
print(type(two_word_states))

def get_state_abbr(x):
    if re.match('({})'.format("|".join(two_word_states)), x.lower()):
        tokens = [re.match('({})'.format("|".join(two_word_states)), x.lower()).group(0)]
    elif re.match('({})'.format("|".join(city_to_state_dict.keys()).lower()), x.lower()):
        k = re.match('({})'.format("|".join(city_to_state_dict.keys()).lower()), x.lower()).group(0)
        tokens = [city_to_state_dict.get(k.title(), np.nan)]
    else:
        tokens = [j for j in re.split("\s|,", x) if j not in ['in', 'la', 'me', 'oh', 'or']]
    for i in tokens:
        if re.match('\w+', str(i)):
            if us.states.lookup(str(i)):
                return us.states.lookup(str(i)).abbr


def main():

    #xs = ["las veas", "San Francisco, adsfhwsdf", "CA", "MA", "Seattle"]
    df = pd.read_csv("user_meta_data.csv", encoding='latin-1')
    none_count = 0
    states_dict = {}
    for index, row in df.iterrows():

        if row['location'] == row['location']:
            res = get_state_abbr(row['location'])
            if res == None:
                none_count+=1
            else:
                if res in states_dict.keys():
                    states_dict[res]+=1
                else:
                    states_dict[res] =1

        else:
            none_count+=1


    print("Failure rate:" + str(none_count) + "/" + str(len(df)))
    #print(states_dict)
    #plt.bar(range(len(states_dict)), list(states_dict.values()), align='center')
    ##plt.xticks(range(len(states_dict)), list(states_dict.keys()))
    ##plt.xlabel('States')
    #plt.ylabel('Count')



if __name__ == '__main__':
    main()




