import argparse

from s3bot.cli import commands

def build_s3bot_parser():
    """Create the s3bot arg parser."""
    parser = argparse.ArgumentParser()


    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

    freeze_parser = subparsers.add_parser("freeze",
                                          help="freeze a file or directory")
    freeze_parser.add_argument("path",
                               help="path to freeze",
                               type=str)

    return parser

def main():
    """Main entrypoint."""
    parser = build_s3bot_parser()
    argmap = parser.parse_args()

    subcommand = argmap.subcommand
    kwargs = vars(argmap)
    kwargs.pop("subcommand")

    getattr(commands, subcommand)(**kwargs)
