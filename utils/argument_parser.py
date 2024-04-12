import argparse


def parse_arguments():
    max_count = 200

    parser = argparse.ArgumentParser(description='请提供视频地址')

    # add url argument
    parser.add_argument('--url', help='url地址')

    # add max count argument
    parser.add_argument('--count', help='最大关注次数')

    args = parser.parse_args()

    print(f"input url: {args.url}")
    if args.count:
        print(f"input count: {args.count}")
        max_count = int(args.count)
    else:
        print("no count input,will use default value 200")

    if args.url:
        return args.url, max_count
    else:
        # throw new exception
        raise Exception("url参数不能为空")
