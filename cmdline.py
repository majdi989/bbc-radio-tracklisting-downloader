from argparse import ArgumentParser, RawTextHelpFormatter
import sys


def parse_arguments(args=sys.argv[1:]):
    """Parse arguments of script."""
    cmd_description = "Download tracklistings for BBC radio shows.\n\n" \
                      "Saves to a text file, tags audio file or does both.\n" \
                      "To select output file, directory and filename must " \
                      "both be specified.\n" \
                      "Otherwise, an attempt will be made to write " \
                      "text file to current directory.\n" \
                      "If choosing 'both', directory and filename should " \
                      "point to audio file.\n" \
                      "In this case, text file will have same name " \
                      "as audio file, but with .txt."

    # http://stackoverflow.com/questions/7869345/
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter,
                            description=cmd_description)
    action_help = "tag: tag audio file with tracklisting\n" \
                  "text: write tracklisting to text file (default)\n" \
                  "both: tag audio file and write to text file"
    parser.add_argument('action', choices=('tag', 'text', 'both'),
                        default='text', help=action_help)
    parser.add_argument('pid', help="BBC programme id, e.g. b03fnc82")
    parser.add_argument('--directory', help="output directory")
    parser.add_argument('--filename', help="output filename")
    args = parser.parse_args()
    print args.action


def main():
    """Placeholder function for now."""
    parse_arguments()


if __name__ == '__main__':
    main()
