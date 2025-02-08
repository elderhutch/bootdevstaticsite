from htmlnode import HTMLNode

props = {
    "href": "https://www.google.com",
    "target": "_blank",
}

testing = HTMLNode("<a>", "This is the text", None, props)
readout = testing.props_to_html()
print(testing)
print(readout)