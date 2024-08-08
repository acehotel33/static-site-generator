import re

def main():
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))

    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))   

    text = "[top boot dev](https://www.boot.dev)"
    print(extract_markdown_links(text)) 

def extract_markdown_images(text):
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