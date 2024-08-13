from textnode import text_to_textnodes
from htmlnode import HTMLNode, ParentNode, LeafNode, text_node_to_html_node


def main():

    markdown = "### This is heading 3\n\n## Here we have heading 2\n\nAnd it is followed by a paragraph\n\n```Below it is some code block```\n\n> As well as\n> Some quotes\n\nThrowing in some **bold** and *italic* text for good measure"

    # block = "> This is line one containg ```code```.\n> This is line two that actually has ![alt-image](www.image.com)\n> This is line three that is so **bold**..."

    # print(block_to_block_type(block))
    # print(markdown_to_blocks(markdown))
    # print(block_to_children(block, 'a'))
    # print(markdown_to_html_node(markdown))
    # print(block_clean_of_markdown(block))

    my_node = markdown_to_html_node(markdown)
    print(my_node.to_html())


"""
<div>
    <h3>This is heading 3</h3>
    <h2>Here we have heading 2</h2>
    <p>And it is followed by a paragraph</p>
    <code>Below it is some code block</code>
    <blockquote>
        As well as\n
        Some quotes
    </blockquote>
    <p>
        Throwing in some <b>bold</b> and <i>italic</i> text for good measure
    </p>
</div>

"""


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
    if len(block) == 0:
        return 'p'
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
            return 'blockquote'

    # check for unordered list
    if block[0] in ['*', '-']:
        is_unordered = True
        for line in split_lines:
            if not (line[:2] == '* ' or line[:2] == '- '):
                is_unordered = False
        if is_unordered:
            return 'ul'

    # check for ordered list
    if block[:2] == "1.":
        line_count = len(split_lines)
        is_ordered = True
        for i in range(line_count):
            if split_lines[i][:3] != f'{i+1}. ':
                is_ordered = False
        if is_ordered:
            return 'ol'

    return 'p'

def markdown_to_html_node(markdown):
    """
    Takes full markdown document and returns a single HTML node that contains children with nested elements.

    Markdown -> Blocks -> 
    Text -> TextNode -> HTMLNode

    Split markdown into blocks of text. For each block, split the text into TextNodes. Convert each TextNode into HTMLNode.
    """

    # blocks = markdown_to_blocks(markdown)
    # parent_nodes = []
    # for block in blocks:
    #     block_tag = block_type_to_tag(block_to_block_type(block))
    #     block_children = block_to_children(block, block_tag)
    #     parent_block = ParentNode(block_tag, block_children, None)
    #     parent_nodes.append(parent_block)


    blocks = markdown_to_blocks(markdown)
    # print(blocks)
    parent_nodes = []
    for block in blocks:
        clean_block = block_clean_of_markdown(block)
        # print(clean_block)
        block_tag = block_to_block_type(block)
        # print(block_tag)
        text_children = text_to_textnodes(clean_block)
        nodes_children = []
        for child in text_children:
            nodes_child = text_node_to_html_node(child)
            nodes_children.append(nodes_child)
        # print(children)
        parent_node = ParentNode(block_tag, nodes_children)
        # print(parent_node)
        parent_nodes.append(parent_node)
    final_HTML_node = ParentNode('div', parent_nodes)
    return final_HTML_node

possible_block_tags = ['h1','h2','h3','h4','h5','h6','code','blockquote','ul','ol','p']
headings = ['h1','h2','h3','h4','h5','h6']

def block_clean_of_markdown(block):
    block_tag = block_to_block_type(block)
    if block_tag in headings:
        return block.lstrip('#').strip()
    if block_tag == 'code':
        return block.strip('```').strip()
    if block_tag == 'blockquote':
        lines = block.splitlines()
        cleaned_lines = [line.lstrip('> ').strip() for line in lines]
        return "\n".join(cleaned_lines)
    if block_tag == 'ul':
        lines = block.splitlines()
        cleaned_lines = [line.lstrip('* ').strip() for line in lines]
        return "\n".join(cleaned_lines)
    if block_tag == 'ol':
        lines = block.splitlines()
        cleaned_lines = [line.lstrip(f'{i+1}. ').strip() for i, line in enumerate(lines)]
        return "\n".join(cleaned_lines)
    if block_tag == 'p':
        return block
    raise Exception('No match for block tag was found within possible block tags')

    

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
