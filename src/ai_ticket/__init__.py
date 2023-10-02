import re

pattern = r'(```)?\s*{\s*"messages"\s*:\s*\[\s*\{\s*"role"\s*:\s*"system"\s*,\s*\"content"\s*:\s*"You\s+are\s+(?P<name>[^,]+),.*'

def find_name(text):
    if not text:
        return False
    if not isinstance(text,str):
        return False
    match = re.match(pattern, text)
    if match:
        extracted_name = match.group(2)
        return extracted_name
    else:
        return None
