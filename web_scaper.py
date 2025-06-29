import requests
from bs4 import BeautifulSoup

def fetch_bbc_news():
    url = 'https://www.bbc.com/news'
    print("Fetching news from",url)
    response = requests.get(url)

    #check if request is successful
    if response.status_code!= 200:
        print("Failed to retrieve data")
        return

    #Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    #Look for <a> tags with headlines
    headline_tags = soup.select('a[href*="/news/"]')

    print("Top BBC News Headlines:")
    count = 0
    for tag in headline_tags:
        text = tag.get_text(strip=True)
        href = tag.get('href')

        if next and href and "/news/" in href and len(text) > 25:
            full_link = f"https://www.bbc.com{href}" if href.startswith("/")else href
            count +=1
            print(f"{count}. {text}")
            print(f" ->Link: {full_link}")

            if count == 10:
                break

    if count == 0:
        print("No headlines found")
#Run the scraper
if __name__ == "__main__":
    fetch_bbc_news()