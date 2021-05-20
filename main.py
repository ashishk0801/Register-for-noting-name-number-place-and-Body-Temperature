import pandas as pd
df = pd.DataFrame(columns=["Name", "Phone Number", "Place", "Body Temperature"])

while True:
    a = input('Name:')            #Type 'quit' for the 'Name:' prompt to terminate the execution
    if a == 'quit' :
        break
    b = input('Phone Number:')
    c = input('Place:')
    d = input('Body Temperature:')

    df = df.append({"Name":a,"Phone Number":b,"Place":c,"Body Temperature":d},ignore_index=True)


print(df)
df.to_excel('register.xlsx')