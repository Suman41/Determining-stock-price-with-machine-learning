from stocklist import StockList
import pandas as pd
import numpy as np
from machine_learning import MachineLearning

all_sectors = {'0': 'Commercial Bank', '1': 'Development Bank', '2': 'Finance', '3': 'Hydropower', '4': 'Mutual Fund',
               '5': 'Life Insurance', '6': 'Microfinance', '7': 'Non-Life Insurance'}
sector_to_search = all_sectors['6']
column_names = ['Number Of Shares', 'Price', 'EPS', 'Book Value', 'Bonus']

micro = StockList(sector_to_search)
micro.search_sector_list()
print(micro.list)

if micro.list:
    data_for_ML = micro.search_datas_for_sector(micro.list)
    append_list = micro.list
    for item in data_for_ML[0]:
        append_list.remove(item)
    df = pd.DataFrame(data_for_ML[1], columns=column_names, index=append_list)
    # print(df)

    def impute_bonus(cols):
        EPS = cols[0]
        Bonus = cols[1]
        if pd.isnull(Bonus):
            if EPS >= 7:
                if sector_to_search == 'Microfinance':
                    return EPS - 15
                else:
                    return EPS - 7
            else:
                return 0.00
        else:
            return Bonus


    df['Bonus'] = df[['EPS', 'Bonus']].apply(impute_bonus, axis=1)
    # df.dropna(inplace=True)
    print(df)

    ml = MachineLearning(df)
    to_input = [[float(input("Enter the total number of shares: ")), float(input("Enter EPS: ")),
                 float(input("Enter Book Value: ")), float(input("Enter the bonus given or expected bonus: "))]]
    to_predict = pd.DataFrame(to_input, columns=['Number Of Shares', 'EPS', 'Book Value', 'Bonus'])
    ml.find_price_regression(to_predict, 'linear')
    ml.find_price_regression(to_predict, 'ridge')

    print(f'Mean of the predicted values: {np.mean(ml.predicted_list)}')
