import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='请提供视频地址')

    # 添加命令行参数
    parser.add_argument('--url', help='url地址')

    return parser.parse_args()
