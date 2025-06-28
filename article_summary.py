import wikipedia

def summarize_topic():
    try:
        topic = input("Enter a topic to search on wikipedia: ") .strip()
        summary = wikipedia.summary(topic, sentences=5) #Fetches sentences from the page
        print("Wikipedia summary:")
        print(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        print("The topic is ambiguous. Suggestions:")
        print(", ".join(e.options[:5])) #Prints a few suggested specific topic

    except wikipedia.exceptions.PageError:
        print("No page found")

    except Exception as e:
        print("qn unexpected error occurred:",str(e))

if __name__ == "__main__":
    summarize_topic()