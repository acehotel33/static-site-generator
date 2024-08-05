def main():
    leafnode = LeafNode("p", "Hello paragraph", {"href": "hey.com", "key": "value"})
    child1 = HTMLNode()
    child2 = HTMLNode("h2")
    node2 = HTMLNode("h1", "Title of paragraph",[child1, child2], {"target": "_blank", "some_key": "some_value"})
    print(leafnode.to_html())

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(tag={self.tag!r}, value={self.value!r}, children={self.children!r}, props={self.props!r})'         

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        prop_string = ""
        for prop in self.props:
            new_prop = f" {prop}" + "=" + f"\"{self.props[prop]}\""
            prop_string += new_prop
        return prop_string

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value==None:
            raise ValueError("The 'value' parameter is required")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag==None:
            return value
        open_tag = f"<{self.tag}{self.props_to_html()}>"
        close_tag = f"</{self.tag}>"
        html = open_tag + self.value + close_tag
        return html

main()