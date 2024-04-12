from utils.argument_parser import parse_arguments

if __name__ == '__main__':
    max_count = 200
    args = parse_arguments()
    print(f"input url: {args.url}")
    if args.count:
        print(f"input count: {args.count}")
        max_count = int(args.count)
    else:
        print("no count input,will use default value 200")
