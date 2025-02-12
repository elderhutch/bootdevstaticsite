from htmlnode import *

props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

testing = HTMLNode("<a>", "This is the text", None, props)
readout = testing.props_to_html()
leaftest = LeafNode("<a>", "Testing Text", props)
leaftest2 = LeafNode("<a>", "Testing Text")
leaftest3 = LeafNode("", "Test")
leaftest4 = leaftest3.to_html

#print(leaftest.props_to_html)

print(leaftest4)