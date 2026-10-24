from colorama import Fore, Style
import pyfiglet
import argparse

PROGRAM = "Blackmore"
VER_NUMBER = 0.1
REPO_URL = "https://github.com/Arismendi17/Blackmore"
DESCRIPTION = "IoT vulnerability detection and mapping tool"

parser = argparse.ArgumentParser(
        prog=PROGRAM,
        description=DESCRIPTION,
        epilog=REPO_URL)


def main():
    parser.add_argument("-V", "--version", action=VersionAction, nargs=0,
                        help="display Blackmore version info")
    parser.add_argument("mode", choices=["scan", "graph"],
                        help="the operation mode for %(prog)s")

    args = parser.parse_args()
    return 0


class VersionAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        ascii_art_title = pyfiglet.figlet_format(PROGRAM, font="slant")
        lines = ascii_art_title.splitlines(True)
        print('\n' + Fore.BLUE + lines[0] + lines[1] + lines[2] +
              Fore.GREEN + lines[3] +
              Fore.RED + lines[4] + Style.RESET_ALL)
        print(DESCRIPTION)
        print(f"Version: {VER_NUMBER}")
        print(REPO_URL + '\n')
        parser.exit()


# main function call
main()
