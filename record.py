import pandas as pd

def save_message(message):
    # create a dataframe to store the message
    df = pd.DataFrame({'message': [message]})
    
    try:
        messages = pd.read_csv('messages.csv')
    except FileNotFoundError:
        messages = pd.DataFrame(columns=['message'])
    
    messages = messages.append(df, ignore_index=True)
    messages.to_csv('messages.csv', index=False)