import json, api, requests

def get_book_details(book_title) : 
    url = f"https://www.googleapis.com/books/v1/volumes?q={book_title}&maxResults=1"
    response = requests.get(url)
    data = response.json()
    if "items" not in data or len(data["items"]) == 0:
        return 0
    return data['items'][0]['volumeInfo']

with open('articles_status.json' , 'r') as file :
    articles = json.load(file)
articles = [articles[0]]
ind = 0
for article in articles :
    if article['written'] == 0 : 
        try:
            with open('writing-format-prompt.txt','r') as file :
                res = api.send_message(eval(file.read()))  
            data = get_book_details(article['name']) 
            data['imageLinks']['thumbnail'] = 'https://www.drupal.org/files/issues/2019-07-21/missing.png' if ("imageLinks" not in data) or ("thumbnail" not in data["imageLinks"]) else data['imageLinks']['thumbnail']
            article['written'] = 1
            with open('articles_status.json','w') as file : 
                articles[ind] = article
                json.dump(articles , file)
            with open('post-format.txt' , 'r') as file :
                res = eval(file.read())
            with open(f"docs/{article['category']}/{data['title']}.md" , 'w') as file : 
                file.write(res)
            print(f"Article {article['name']} Done!")
        except Exception as e:
            print(f"Error while writing article {article['name']}. : {e}")
    ind += 1