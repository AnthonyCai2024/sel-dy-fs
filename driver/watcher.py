from time import sleep

from driver.web_driver import WebDriver


class Watcher:
    @staticmethod
    def filter_valid_user(elements) -> dict:
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
                if href not in unique_hrefs:
                    unique_hrefs[href] = element

            except Exception as e:
                print(f'No href found inside this,', e)
                continue

        return unique_hrefs

    @staticmethod
    def follow_user(web_driver: WebDriver, filtered_dict, max_count):
        # 定义起始索引,第一个是自己,不用关注
        index = 0

        # 遍历唯一元素列表
        for key, element in filtered_dict.items():
            index += 1
            print(f'index++:', index)

            if index > max_count:
                print(f'已经关注了{max_count}个用户,程序退出!')
                break
            # elif index > 1:
            #     print(f'程序开始关注!')
            # else:
            #     print(f'程序跳过第一个关注:')
            #     continue

            try:
                # 对第一个元素执行操作，比如点击

                print(f'key:', key)
                print(f'element:', element.get_attribute('outerHTML'))
                element.click()

                sleep(2.6)
                web_driver.switch_to_latest_window()

                button = web_driver.find_element('button[data-e2e="user-info-follow-btn"][type="button"]')
                button_html = button.get_attribute('outerHTML')
            except Exception as e:
                print(f'No button found inside this,', e)
                web_driver.close_switch_to_main_window()
                continue

            sleep(0.3)

            if '已关注' in button_html:
                print('已关注,不需再次点击')
            else:
                web_driver.execute_click(button)

            sleep(0.9)

            # 关闭当前标签页
            web_driver.close_current_tab()

            # # 关闭当前窗口
            # # 获取当前所有打开的标签页的句柄
            # handles = driver.window_handles
            #
            # handle_count = len(handles)
            #
            # # 切换到新打开的标签页
            # driver.switch_to.window(handles[handle_count - 1])
