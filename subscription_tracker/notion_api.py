import requests


import requests
NOTION_API_KEY = "secret_fpzxtvY93ozKaAQrSNk3SdwbwBcUEyKckNZFx5zgHOa"
NOTION_DATABASE_ID = "884fade61b7f429e94e7c2fa030a2697"

# retreive the database 
def retreive_databse():
    url = f'https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}'
    headers = {
        'Authorization': f'Bearer {NOTION_API_KEY}',
        'Notion-Version': '2022-06-28'
    }
    response = requests.get(url, headers=headers)
    return(response.content)


# add a new entry to the database
def add_entry(name, tags, date, price):
    url = 'https://api.notion.com/v1/pages'

    headers = {
        'Authorization': 'Bearer ' + NOTION_API_KEY,
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }
    data = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            "Name": {
                "title": [
                    {
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Tags": {
                "multi_select": [
                    {"name": tags}
                ]
            },
            "Date": {
                "date":{"start": date}
            },
            "Price": { "number": price }
        },
        
    }

    response = requests.post(url, headers=headers, json=data)

    return(response)
