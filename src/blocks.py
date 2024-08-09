def main():
    markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    block = '```code block```'
    print(block_to_block_type(block))
    # print(markdown_to_blocks(markdown))

def markdown_to_blocks(markdown):
    list_of_blocks = markdown.split('\n\n')
    stripped_list_of_blocks = []
    for block in list_of_blocks:
        if block != "":
            stripped_list_of_blocks.append(block.strip())
    return stripped_list_of_blocks

def block_to_block_type(block):
    # check for heading type
    if block[0] == "#":
        length_to_check = min(6, len(block))
        number_of_hashtags = block[:length_to_check].count('#')
        header_num = number_of_hashtags
        for i in range(number_of_hashtags):
            if block[i] != '#':
                header_num = i
                break
        headers_list = ['none', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        if block[header_num] == ' ':
           return headers_list[header_num]

    # check for code type
    if block[:3] == '```' and block[:3] == block[-3:] and len(block) >= 6:
        return 'code'
        

if __name__=="__main__":
    main()
