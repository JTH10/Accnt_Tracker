import pandas as pd
import re
#Update MONTH to reflect month of current .csv statement
MONTH = 'august'

file = f"wells_{MONTH}.csv"

statement = pd.read_csv(file, header=None)

statement.columns = ['Date', 'Amount', 'Star', 'Blank', 'Name']


df = statement[['Name', 'Amount', 'Date']]

# Remove unneccesary data in 'Amount' column
pmts = df.loc[df['Amount'] >= 150.00]

# Rename data in "Name" column based on values in "Amount" Column
pmts.loc[pmts['Name'].str.contains('700001'), 'Name'] = 'Washington'
pmts.loc[pmts['Name'].str.contains('02525'), 'Name'] = 'Schultz'
pmts.loc[pmts['Amount'] == 574.56, 'Name'] = 'Farmer'
pmts.loc[pmts['Amount'] == 916.67, 'Name'] = 'Goldstein'

#Sort DF by Date, then Amount & Reset Index.
pmts = pmts.sort_values(['Date', 'Amount']).reset_index(drop=True)


pmts.to_csv(f'HMPmts{MONTH}.csv')

