import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config", help="read from this file")
args = parser.parse_args()
if args.config:
    print("config read it!", args.config)
else:
    print("No config file!")
