import argparse

from s3bot.cli import commands

def build_s3bot_parser():
    """Create the s3bot arg parser."""
    parser = argparse.ArgumentParser()


    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

    freeze_parser = subparsers.add_parser("freeze",
                                          help="freeze a file or directory")
    ls_parser     = subparsers.add_parser("ls",
                                          help="list the contents of S3")

    freeze_parser.add_argument("path",
                               help="path to freeze",
                               type=str)
    ls_parser.add_argument("prefix",
                           help="prefix of paths in the bucket",
                           type=str,
                           nargs="*",
                           default=str())

    return parser

def main():
    """Main entrypoint."""
    parser = build_s3bot_parser()
    argmap = parser.parse_args()

    kwargs = vars(argmap)
    subcommand = kwargs.pop("subcommand")

    getattr(commands, subcommand)(**kwargs)
