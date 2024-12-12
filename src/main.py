from block_markdown import markdown_to_blocks

def main():
    test_md = """# Heading


Paragraph
text here



* List item
* List item
"""
    print(markdown_to_blocks(test_md))


if __name__ == "__main__":
    main()
