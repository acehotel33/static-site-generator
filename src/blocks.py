def main():
    markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

    print(markdown_to_blocks(markdown))

def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split('\n\n')
    stripped_list_of_blocks = []
    for block in list_of_blocks:
        if block != "":
            stripped_list_of_blocks.append(block.strip())
    return stripped_list_of_blocks

if __name__=="__main__":
    main()

[
    '# This is a heading', 

    'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
    
    '* This is the first list item in a list block\n* This is a list item\n* This is another list item']