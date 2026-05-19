import pandas as pd

import matplotlib.pyplot as plt

from get_users_profiles_Aiham import get_users_profiles


def show_users_get_density():

    df_profile = get_users_profiles()

    df_age = df_profile['age']

    df_age.plot(kind='density')

    plt.xlabel("Age")

    plt.ylabel("Density")

    plt.title("Users Age Density")
    plt.show()

show_users_get_density()