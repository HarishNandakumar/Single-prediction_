import pandas as pd

def search_account_head(file_path, search_term):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Check if the search term is in any of the columns
    matching_rows = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
    
    if not matching_rows.empty:
        return matching_rows['Account Head'].tolist()
    else:
        return []

# Example usage
file_path = 'data.csv'  # Replace with the path to your CSV file
search_term = input("Enter the search term: ")

account_heads = search_account_head(file_path, search_term)

if account_heads:
    print("Account Head(s) found:")
    for account_head in account_heads:
        print(account_head)
else:
    print("No Account Head found for the given search term.")
