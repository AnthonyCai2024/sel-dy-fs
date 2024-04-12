from utils.argument_parser import parse_arguments
from utils.url_finder import find

if __name__ == '__main__':
    link, count = parse_arguments()

    url = find(link)
