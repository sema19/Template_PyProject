import argparse
import json

def read_arguments():
    parser = argparse.ArgumentParser(
        prog='Template Python',
        description='Simple output of a json file with greetings and settings')
    parser.add_argument('-f', '--filename', help="output filename")
    parser.add_argument('-g', '--greeting', help="greeting text")
    parser.add_argument('-u', '--user', help="user name")

    args = parser.parse_args()
    return args

def read_config():
    pass

def main():
    args = read_arguments()
    config = read_config()
    data ={"greeting": f"{args.greeting} {args.user}",
           "arguments": vars(args)
           }
    print(data)
    json.dumps(data)


if __name__ == "__main__":
    main()