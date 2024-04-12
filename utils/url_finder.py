import re


def find(text) -> str:
    pattern = r"(https?://\S+)"
    match = re.search(pattern, text)

    if match:
        url = match.group(0)
        print("URL match:", url)
        return url
    else:
        print("未找到URL")
        return ""
