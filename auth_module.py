import pandas as pd

def load():
    return pd.read_csv("credentials.csv")

credentials = load()

def account_creation(username, email, password):
    global credentials
    if credentials['Username'].isin([username]).any():
        return "Username already exists"
    elif credentials['Email'].isin([email.lower()]).any() or ("gmail.com" != email[-9:]):
        return "Email already exists or it's invalid"
    else:
        new_row = pd.DataFrame([[username, email.lower(), password]], columns=credentials.columns)
        result = pd.concat([credentials, new_row], axis=0) 
        credentials = result.reset_index(drop=True)
        credentials.to_csv('credentials.csv', index=False)
        credentials = load()  # Reload credentials after updating the CSV
        return "Account created successfully"

def login(username_or_email, password):
    global credentials
    user_exists = (credentials['Username'] == username_or_email) | (credentials['Email'] == username_or_email.lower())
    if user_exists.any():
        correct_password = credentials.loc[user_exists, 'Password'].values[0]
        if correct_password == password:
            return "Login successful"
        else:
            return "Invalid password"
    else:
        return "Invalid login details"

