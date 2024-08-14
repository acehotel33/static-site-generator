import re

def main():
    text = "[top boot dev](https://www.boot.dev)"
    print(extract_markdown_links(text)) 

def extract_markdown_images(text):
    """
    Extracts markdown images from given text and returns a list of tuples for all: (alt_text, link)
    """
    list_of_tuples = []
    list_of_regex = re.findall(r"\!\[.*?\]\(.*?\)", text)
    for match in list_of_regex:
        if (match.count('[') + match.count(']')) % 2 != 0:
            raise Exception("Incorrect Markdown syntax: missing '[' or ']'")
        if (match.count('(') + match.count(')')) % 2 != 0:
            raise Exception("Incorrect Markdown syntax: missing '(' or ')'")
        alt_text = re.findall(r"\[.*?\]", match)
        link = re.findall(r"\(.*?\)", match)
        list_of_tuples.append((alt_text[0].strip('[]'), link[0].strip('()')))
    return list_of_tuples

def extract_markdown_links(text):
    """
    Extracts markdown links from given text and returns a list of tuples for all: (alt_text, link)
    """
    list_of_tuples = []
    list_of_regex = re.findall(r"(?<!!)\[.*?\]\(.*?\)", text)
    for match in list_of_regex:
        if (match.count('[') + match.count(']')) % 2 != 0:
            raise Exception("Incorrect Markdown syntax: missing '[' or ']'")
        if (match.count('(') + match.count(')')) % 2 != 0:
            raise Exception("Incorrect Markdown syntax: missing '(' or ')'")
        alt_text = re.findall(r"\[.*?\]", match)
        link = re.findall(r"\(.*?\)", match)
        list_of_tuples.append((alt_text[0].strip('[]'), link[0].strip('()')))
    return list_of_tuples

if __name__ == "__main__":
    main() 