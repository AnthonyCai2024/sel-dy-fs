import re


def find(text) -> str:
    pattern = r"(https?://\S+)"
    match = re.search(pattern, text)

    if match:
        url = match.group(0)
        print("URL match:", url)
        return url

    # raise exception
    raise Exception("URL not found,请使用双引号包裹URL地址")
