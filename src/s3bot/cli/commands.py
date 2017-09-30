"""s3bot command line tool abstraction."""

import s3bot.freeze
from s3bot.s3_interface import S3Wrapper

# Save a stack frame, don't need a wrapper function.
freeze = s3bot.freeze.freeze

def ls(*args):
    """List the contents of the default bucket, with prefixes in the
    args."""

    s3 = S3Wrapper()
    contents = dict((arg, '') for arg in args)

    if args:
        for arg in args:
            contents[arg] = list(s3.bucket_contents(arg))
    else:
        # empty prefix; root of the bucket
        contents[''] = list(s3.bucket_contents(''))

    for pfx, cnts in contents.items():
        if pfx:
            print("{}:".format(pfx))
        else:
            print("bucket root:")

        for item in cnts:
            print("\t{}".format(item))
        print("")
