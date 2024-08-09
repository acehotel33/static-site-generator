def main():
    markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
    # block = "> This is line one.\n> This is line two\n> This is line three..."
    # block = "* This is line one.\n- This is line two."
    # block = "1. hello\n2. can you hear me\n3. i was wondering if after all these years you'd like to meet"
    # block = "1. 2. 3. \n2. \n3. "
    # block = "hello mate"
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
        if len(block) > header_num:
            if block[header_num] == ' ':
               return headers_list[header_num]

    # check for code type
    if block[:3] == '```' and block[:3] == block[-3:] and len(block) >= 6:
        return 'code'
    
    split_lines = block.split('\n')

    # check for quote block
    if block[0] == '>':
        is_quote = True
        for line in split_lines:
            if line[0] != '>':
                is_quote = False
        if is_quote:
            return 'quote'

    # check for unordered list
    if block[0] in ['*', '-']:
        is_unordered = True
        for line in split_lines:
            if not (line[:2] == '* ' or line[:2] == '- '):
                is_unordered = False
        if is_unordered:
            return 'unordered list'

    # check for ordered list
    if block[:2] == "1.":
        line_count = len(split_lines)
        is_ordered = True
        for i in range(line_count):
            if split_lines[i][:3] != f'{i+1}. ':
                is_ordered = False
        if is_ordered:
            return 'ordered list'

    return 'normal paragraph'
if __name__=="__main__":
    main()
