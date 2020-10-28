import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date
from time import time 

def playIt():
    try:
        df = pd.read_csv('./modules/data.csv')

        now = pd.to_datetime('now')

        df['birthdate'] = pd.to_datetime(df['birthdate'], errors='coerce')
        df['age'] = (now - df['birthdate']).astype('<m8[Y]').astype('int')

        start = time()
        for index, row in df.iterrows():
            print("Person No.",index+1,"of age",row['age'],"Named",row['username'],"lives at: ",' '.join(row['address'].split('\n')))
        elapsed = time() - start

        print('Printing time: ',elapsed)
        return ""
    
    except Exception as e:
        print("exception: ",e)
        return e

if __name__ == '__main__':
    playIt()
    # df = df.head(10)
    # average_age = df['age'].mean()
    # print("average_age: ", average_age)