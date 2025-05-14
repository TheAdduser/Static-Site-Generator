from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if all(line.startswith("> ") for line in block.split("\n")):
        return BlockType.QUOTE

    if all(line.startswith("- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST

    lines = block.split("\n")
    if all(re.match(r"^\d+\. ", line) for line in lines):
        numbers = [int(re.match(r"^(\d+)\. ", line).group(1)) for line in lines]
        expected = list(range(1, len(numbers) + 1))
        if numbers == expected:
            return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
