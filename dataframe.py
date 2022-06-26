import pandas as pd
from api_call import make_restcountries_call
import time
from encrypt import encrypt

def make_dataframe(data):
    """ 
        Param data (this params is the dict from API CALL)
        Make dataframe with API DATA

        Region - City name - Language - Time
    """
    data_to_frame = [] # List to create rows
    for language in range(len(data.get("languages"))):
        """ Loop of all languages from API CALL """
        t0 = time.time()
        data_to_frame.append([
            data.get("region"),
            data.get("city_name"),
            encrypt(data.get("languages")[language]),
        ])
        t1 = time.time()
        total_time = t1-t0
        data_to_frame[language].append(total_time)
    # Make dataframe
    df = pd.DataFrame(data_to_frame, columns=["Region","City name","Language","Time"])
    total_time = df["Time"].sum()
    time_average = df["Time"].mean()
    time_min = df["Time"].min()
    time_max = df["Time"].max()
    print("\n\t**** DATAFRAME ****\n\n")
    print(df)
    print("\n\nTotal time: ", total_time)
    print("\n\nTime average: ", time_average)
    print("\n\nTime min: ", time_min)
    print("\n\nTime max: ", time_max)
    return df, (total_time,time_average,time_min,time_max,)

