from enum import Enum
from textnode import TextNode
from textnode import TextType

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    node2 = TextNode("Finally got it", TextType.ITALIC, "www.imadummy.net")
    node3 = TextNode("Well", TextType.TEXT, "ainthappenin.gov")
    print(node)
    print(node2)
    print(node3)


main()