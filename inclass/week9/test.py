import pandas as pd

data = pd.DataFrame([1,5,3,9,2,5,9,1,4,6,9,3,4,7,8,3,9,2,4,3,1,8], columns=['RandNum'])

print(data.iloc[1:,:])