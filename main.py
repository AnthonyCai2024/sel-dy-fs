from utils.argument_parser import parse_arguments

if __name__ == '__main__':
    args = parse_arguments()
    print(f"input url: {args.url}")
