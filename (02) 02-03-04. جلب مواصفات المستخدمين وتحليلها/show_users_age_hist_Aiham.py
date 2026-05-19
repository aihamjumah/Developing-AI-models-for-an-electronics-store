import pandas as pd

import matplotlib.pyplot as plt

from get_users_profiles_Aiham import get_users_profiles

def show_users_age_his():
    df_profile = get_users_profiles()

    df_age = df_profile['age']

    df_age.hist(bins=[0,10,20,30,40,50,60,70,80])

    plt.xlabel("Age")

    plt.ylabel("Count")

    plt.title("Users Age Histogram")
    plt.show()

show_users_age_his()    

print("Trying to connect with password...")
