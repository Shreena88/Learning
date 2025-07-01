import requests

def get_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"Word: {data[0]['word']}")
        print(f"Pronunciation: {data[0]['phonetics'][0].get('text','N/A')}")
        print(f"Part of speech: {data[0]['meanings'][0]['partOfSpeech']}")
        print(f"Definition: {data[0]['meanings'][0]['definitions'][0]['definition']}")
        example = data[0]['meanings'][0]['definitions'][0].get('example')
        if example:
            print(f"Example: {example}")
    else:
        print("Word not found or an error occurred.Try again.")

if __name__ == "__main__":
    word_input = input("Enter a word to search: ").strip()
    get_meaning(word_input)