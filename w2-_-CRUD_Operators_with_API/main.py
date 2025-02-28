import requests
from API_KEY import API_KEY

URL = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API_KEY}" 

def fetch_news(*args):
    list_of_news = []
    response = requests.get(URL)
    
    if response.status_code == 200:

        data = response.json()
        id = 1 # IDs are kept as strings, so I wanted to give them manually.

        for article in data["articles"]:
            news_item = [id]

            for field in args:
                if field in article or field in article.get("source", {}):

                    if field == 'source':
                        news_item.extend([value for value in article.get("source", {}).values()])

                    elif field == 'id' or field == 'name':
                        for k, v in article.get("source").items():
                            if k == field:
                                news_item.append(v)

                    else:
                        news_item.append(article.get(field, f"No info for '{field}'"))


            list_of_news.append(news_item)

            id += 1
    
        return list_of_news

# ==================================================================== #

### CRUD Operators ###

## Create
def create_news(news_list, *news_details):
    new_id = max([news[0] for news in news_list], default=0) + 1
    news_list.append([new_id] + list(news_details))
    return news_list

## Read
def read_news(news_list):
    for news in news_list:
        print(news)

## Update
def update_news(news_list, news_id, *new_details):
    for news in news_list:
        if news[0] == news_id:
            news[1:] = list(new_details)
            print("\nNews updated successfully.")
            return news_list
    print(f"ID {news_id} not found.")
    return news_list


## Delete
def delete_news(news_list, news_id):
    for news in news_list:
        if news[0] == news_id:
            news_list.remove(news)
            print("\nNews deleted successfully.")
            return news_list
    print(f"ID {news_id} not found.")
    return news_list

""" 
    From this dataset, I suggest you pull the "author" and "title" parts to make them shorter and more visible, 
    so we can see the CRUD operations more clearly. Because the text length in the other titles is too long.

    I still used *args so that the user can pull the information from the requested header.
 """

def get_user_fields():
    user_input = input("Enter the news fields you would like to receive (example: author, title, description): ")
    fields = user_input.split()
    return fields
    


user_fields = get_user_fields()
news_list = fetch_news(*user_fields)


while True:
    print("\nOptions:")
    print("1. View news")
    print("2. Create news")
    print("3. Update news")
    print("4. Delete news")
    print("5. Exit")

    choice = input("Choose an option: ")

    match choice:
        case "1":
            print("\nNews List:")
            read_news(news_list)

        case "2":
            details = input("Enter new news details (separate by comma): ").split(",")
            news_list = create_news(news_list, *details)
            print("\nNews created successfully.")
            
        case "3":
            news_id = int(input("Enter the ID of the news to update: "))
            new_details = input("Enter new details (separate by comma): ").split(",")
            news_list = update_news(news_list, news_id, *new_details)

        case "4":
            news_id = int(input("Enter the ID of the news to delete: "))
            news_list = delete_news(news_list, news_id)

        case "5":
            print("\nHave a nice day..")
            break

        case _:
            print("\nInvalid option. Please choose a valid one.")