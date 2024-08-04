def main():
    examplenode = HTMLNode("p", "Hello paragraph", None, {"href": "hey.com", "key": "value"})
    print(examplenode.props_to_html())
    print(examplenode)

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

main()