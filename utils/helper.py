import re


def extract_likes(text):
    match = re.search(r'([\d,]+)\s+likes', text)
    if match:
        number_str = match.group(1).replace(',', '')
        return int(number_str)
    return 0