from selenium.common import NoSuchElementException


class Watcher:
    @staticmethod
    def filter_valid_user(elements) -> list:
        print(f'elements count:', len(elements))
        if len(elements) == 0:
            raise Exception('No user elements found!')

        # 遍历元素列表，检查元素的HTML中是否是用户链接
        specific_string = 'MS4'
        filtered_elements = [element for element in elements if specific_string in element.get_attribute('outerHTML')]

        # 使用字典来存储已经添加的name，确保唯一性
        # 字典的键是name，值是相应的字典（第一次出现的）
        unique_hrefs = {}

        # 对筛选后的元素列表进行操作
        for element in filtered_elements:
            # print(element.get_attribute('outerHTML'))  # 或者任何你需要对元素进行的操作
            try:
                href = element.get_attribute('href')
                # print('href:', href)

                if href not in unique_hrefs:
                    unique_hrefs[href] = element

            except NoSuchElementException:
                print('No href found inside this ')
                continue

        # 打印字典的值
        for value in unique_hrefs.values():
            print(value.get_attribute('outerHTML'))

        # 获取字典的值集合，这些是唯一的元素
        filtered_unique_items = list(unique_hrefs.values())

        if len(filtered_unique_items) == 0:
            raise Exception('No valid user found!')

        return filtered_unique_items
