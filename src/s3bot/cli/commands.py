"""s3bot command line tool abstraction."""

import s3bot.freeze

# Save a stack frame, don't need a wrapper function.
freeze = s3bot.freeze.freeze
