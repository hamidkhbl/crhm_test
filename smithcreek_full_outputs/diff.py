import pandas as pd
import numpy as np

#Read Ubuntu output file
df_u = pd.read_csv("Ubuntu_export.csv")
print("Ubuntu output shape: ",df_u.shape)

#Read legacy output file
df_l = pd.read_csv("Legacy_full_export.csv")
print("Legacy output shape: ", df_l.shape)

# Temperory: get top records of Ubuntu as legacy file is not completed
df_u = df_u.head(df_l.shape[0])
print("Ubuntu output shape: ",df_u.shape)

# Join based on time
df = df_u.merge(df_l, on='time')
print('Merged shape:',df.shape)
#df.to_csv("merged.csv")
print(df.info())

# Find rows where sign of the numbers are different
#print(df[df['WS_outflow@F(1)_x'] > 0 & df['WS_outflow@F(1)_y'] < 0].count())

# Calculate difference of absolute values
##df['diff_1'] = df['WS_outflow@F(1)_x'] -





