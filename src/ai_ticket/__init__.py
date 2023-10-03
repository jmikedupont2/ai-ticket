import re


def find_name(text):
    pattern = r'(```)?\s*{\s*"messages"\s*:\s*\[\s*\{\s*"role"\s*:\s*"system"\s*,\s*\"content"\s*:\s*"You\s+are\s+(?P<name>[^,]+),.*'
    match = re.match(pattern, text)
    if match:
        extracted_name = match.group(2)
        return extracted_name
    else:
        return None
