import re

def extract_markdown_images(text):
    text_links = re.findall(r"!\[([A-Z,a-z, ]*)\]\((https:\/\/[\w,.,/,-]*)\)", text) 
    return text_links

def extract_markdown_links(text):
    text_links = re.findall(r"\[([A-Z,a-z, ]*)\]\((https:\/\/[\w,@,.,/,-]*)\)", text) 
    return text_links


