import wget
url = 'https://docs.google.com/spreadsheets/d/1FTXLaN84KB6ra3JSTvycQb7dU9ekXUDToIg9x4MJsu0/edit?usp=sharing'

response = wget.download(url)

