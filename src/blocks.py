from textnode import text_to_textnodes

def main():
    markdown = "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"

    block = "> This is line one containg ```code```.\n> This is line two that actually has ![alt-image](www.image.com)\n> This is line three that is so **bold**..."
    # print(block_to_block_type(block))
    # print(markdown_to_blocks(markdown))
    print(block_to_children(block, 'a'))

def markdown_to_blocks(markdown):
    """
    Takes markdown text and converts it into a stripped list of separated blocks.
    """

    list_of_blocks = markdown.split('\n\n')
    stripped_list_of_blocks = []
    for block in list_of_blocks:
        if block != "":
            stripped_list_of_blocks.append(block.strip())
    return stripped_list_of_blocks

def block_to_block_type(block):
    """
    Takes a block as input and returns its type: header, code, ordered list, unordered list, quote, or normal paragraph.
    """
    
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

    return 'p'

def markdown_to_html_node(markdown):
    """
    Takes full markdown document and returns a single HTML node that contains children with nested elements.

    Markdown -> Blocks -> 
    Text -> TextNode -> HTMLNode

    Split markdown into blocks of text. For each block, split the text into TextNodes. Convert each TextNode into HTMLNode.
    """

    blocks = markdown_to_blocks(markdown)
    parent_nodes = []
    for block in blocks:
        block_tag = block_type_to_tag(block_to_block_type(block))
        block_children = block_to_children(block, block_tag)
        parent_block = ParentNode(block_tag, block_children, None)
        parent_nodes.append(parent_blocK)

def block_type_to_tag(block_type):
    """
    Helper function that takes as input block type and returns corresponding tag value in string form
    """
    return None

def block_to_children(block, block_tag):
    """
    Helper function that takes TextNodes within a block and returns a nested ParentTag with tagged children.
    """
    block_lines = block.split('\n')
    block_text_nodes = []
    for line in block_lines:
        line_nodes = text_to_textnodes(line)
        block_text_nodes.extend(line_nodes)
    return block_text_nodes


"""
[
    TextNode(> This is line one containg , text, None), 
    TextNode(code, code, None), 
    TextNode(., text, None), 
    TextNode(> This is line two that actually has , text, None), 
    TextNode(alt-image, image, www.image.com), 
    TextNode(> This is line three that is so , text, None), 
    TextNode(bold, bold, None), 
    TextNode(..., text, None)
]
"""

if __name__=="__main__":
    main()
