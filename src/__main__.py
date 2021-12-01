# This Python file uses the following encoding: utf-8
import sys
import modules.cli_execution
from . import __version__

def main():
    """
    main run function
    """
    options = modules.cli_execution.parse_args(sys.argv[:1])

    # Print version and exit with --version option
    if options.version:
        raise SystemExit('{}'.format(__version__))
    
    modules.cli_execution.cli_execution()

if __name__ == "__main__":
    main()
