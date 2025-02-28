from markdown_blocks import markdown_to_blocks 

def extract_title(markdown):
    # use extract blocks func
    blocks = markdown_to_blocks(markdown)
    header = '' 

    # iterate through and see if starts with '# '
    for b in blocks:
        if b.startswith('# '):
            header = b.lstrip('# ')
            return header

    raise ValueError("No h1 header found")
    
    

