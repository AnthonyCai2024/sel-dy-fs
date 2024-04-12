import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='请提供视频地址')

    # add url argument
    parser.add_argument('--url', help='url地址')

    # add max count argument
    parser.add_argument('--count', help='最大关注次数')

    return parser.parse_args()
