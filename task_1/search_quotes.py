import connect
from models import Author, Quote


def search_by_author(author_name):
    author = Author.objects(fullname=author_name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            print(quote.quote)
    else:
        print("Author not found")

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    for quote in quotes:
        print(quote.quote)

def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    for quote in quotes:
        print(quote.quote)

def main():
    while True:
        user_input = input("Enter command: ")
        if user_input.startswith("name:"):
            author_name = user_input[len("name:"):].strip()
            search_by_author(author_name)
        elif user_input.startswith("tag:"):
            tag = user_input[len("tag:"):].strip()
            search_by_tag(tag)
        elif user_input.startswith("tags:"):
            tags = user_input[len("tags:"):].strip()
            search_by_tags(tags)
        elif user_input == "exit":
            break
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
