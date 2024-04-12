import re


class RegFilter:
    @staticmethod
    def url_search(text) -> str:
        pattern = r"(https?://\S+)"
        match = re.search(pattern, text)

        if match:
            url = match.group(0)
            print("URL match:", url)
            return url

        # raise exception
        raise Exception("URL not found,请使用双引号包裹URL地址")

    @staticmethod
    def user_search(text) -> bool:
        # www.douyin.com/user/MS4wLjABAAAATkUrzmZ-
        pattern = r"(www.douyin.com/user/MS4)"
        match = re.search(pattern, text)

        if match:
            return True

        return False



