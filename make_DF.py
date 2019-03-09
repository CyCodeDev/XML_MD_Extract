import pandas as pd
import pickle

d = open('Equity_Mappings.pickle', 'rb')
d = pickle.load(d)

#d = eval(open('CMO_FIELDS_FOR_MUNI_MAPPING_2.txt', 'r').read())

#f_list = list(p_data)
#df = pd.DataFrame.from_items(data_list)
#f_list[0]  f_list[1])
#print(list(p_data)[0])


df = pd.DataFrame(d[0])
df.to_csv('EQUITY_MAPPINGS_1.csv', index=None)
print(df.head())