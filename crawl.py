import requests
from bs4 import BeautifulSoup

def crawl_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    html = str(soup)

    #write html in text file
    try:
        with open("data/text.txt", 'w', encoding='utf-8') as file:
            file.write(html)
        print(f"Successfully wrote to text.txt")
    except Exception as e:
        print(f"An error occurred: {e}")

    return str(soup)

#crawl_url("https://fastapi.tiangolo.com/")
