import pandas as pd

data = pd.read_csv('local_data/train.csv')

print(data.at[0,'Survived'])