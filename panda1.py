import pandas as pd

data = {'car':{1:'ertiga',2:'sonet',3:'jazz'},
        'brand':{1:'maruti',2:'kia',3:'honda'}
        }

df = pd.read_json('data.json')

print(df)