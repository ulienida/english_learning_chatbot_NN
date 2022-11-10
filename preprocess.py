"""
preprocess the csv datafile to an acceptable csv with appropriate rows and columns
1. get rid of label column
2. transpose the rows and columns
3. line up child and parent dialogue sequences
"""

import pandas as pd
from pandas import read_csv
df = pd.read_csv('pcit_dataset.csv')
# create the new dataset
new_df = pd.DataFrame(columns=['Speaker', 'Utterance'])

for ind in df.index:
    if not pd.isnull(df['child talk'][ind]):
        new_df.loc[len(new_df.index)] = ['child', df['child talk'][ind]]
    if not pd.isnull(df['parent talk'][ind]):
        new_df.loc[len(new_df.index)] = ['parent', df['parent talk'][ind]]

new_df.to_csv('beginner_dataset_pcit.csv', index=False)