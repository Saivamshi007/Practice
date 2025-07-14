import pandas as pd

data = {"name":["Sai","Teja"],
        "age":[26,28]
        
        }
df = pd.DataFrame(data)

new_row = pd.DataFrame({"name":["sai"],"age":[54]})
df = pd.concat([df,new_row],ignore_index=True)

print(df)