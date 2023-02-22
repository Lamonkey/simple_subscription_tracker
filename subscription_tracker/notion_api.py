import requests




# retreive the database 
def retreive_databse(notion_databse_id, notion_api_key):
    url = f'https://api.notion.com/v1/databases/{notion_databse_id}'
    headers = {
        'Authorization': f'Bearer {notion_api_key}',
        'Notion-Version': '2022-06-28'
    }
    response = requests.get(url, headers=headers)
    return(response.content)


# add a new entry to the database
def add_entry(name, tags, date, price, notion_api_key, notion_database_id):
    url = 'https://api.notion.com/v1/pages'

    headers = {
        'Authorization': 'Bearer ' + notion_api_key,
        'Content-Type': 'application/json',
        'Notion-Version': '2022-06-28'
    }
    data = {
        "parent": { "database_id": notion_database_id },
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
