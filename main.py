''' Python v3.9.2 more information and dependencies, read requirements.txt
    Syntax camelCase '''

# Imports
import argparse
from locale import getdefaultlocale
from src import translators as tr
import sys

# Main function
def main():
    langSystem = systemLanguage()

    # Supported languages
    language = {
        "zh": "chinese",
        "en": "english",
        "de": "german",
        "it": "italian",
        "pl": "polish",
        "pt": "portuguese",
        "ru": "russian",
        "es": "spanish",
        "sv": "swedish",
        "fr": "french",
        None: None,
    }

    # Defining name, use and definition
    parser = argparse.ArgumentParser(
        prog="Trpy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="Trpy is a command line translator, intended to be as practical and fast as possible.\nThe supported languages are: Chinese, English, German, Italian, Polish, Portuguese, Russian, Spanish, Swedish, French.\n\nThis Translator was developed by @VidalGB.\nYou can find the source code at: https://github.com/VidalGB/Trpy",
    )

    # Version argument
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 1.0",
        help="show program's version number and exit.",
    )

    # Of language argument
    parser.add_argument(
        "-o",
        "--of",
        type=str,
        default=None,
        help="Language of the text to be translated (it can be abbreviated, example: 'en' or 'english'), by default it is automatic, but it is not recommended.",
    )

    # To language argument
    parser.add_argument(
        "-t",
        "--to",
        type=str,
        default=f"{langSystem}",
        help="Language to translate the text (it can be abbreviated, example: 'en' or 'english'), by default it is the language of your operating system.",
    )

    # Message argument
    parser.add_argument(
        "-m",
        "--message",
        type=str,
        required=True,
        help='Text to translate, in quotes "Example".',
    )

    # DeepL translator argument (free)
    parser.add_argument(
        "-d",
        action="store_true",
        help="Use the DeepL translator with auth key in version Free.",
    )

    # DeepL translator argument (pro)
    parser.add_argument(
        "-dp",
        action="store_true",
        help="Use the DeepL translator with auth key in version Pro.",
    )

    # Microsoft translator argument
    parser.add_argument(
        "-mi", action="store_true", help="Use the Microsoft translator."
    )

    # My memory translator argument
    parser.add_argument("-me", action="store_true", help="Use the MyMemory translator.")

    # Google translator argument
    parser.add_argument("-g", action="store_true", help="Use the Google translator.")
    args = parser.parse_args()
    print(args)

    controlLanguage(args, language) # Controlling language and referring translators


def controlLanguage(args, language):
    '''Control language suport'''

    of = [True for key, value in language.items() if args.of == key or args.of == value]
    to = [True for key, value in language.items() if args.to == key or args.to == value]
    if to == [True] and of == [True]:

        # Referring translators
        if args.d:
            tr.deeplTranslate(args)
        elif args.dp:
            tr.deeplTranslate(args)
        elif args.g:
            tr.googleTranslate(args)
        elif args.mi:
            tr.microsoftTranslate(args)
        elif args.me:
            tr.memoryTranslate(args)
        else:
            tr.translate(args)

    else:
        if to != [True]:
            sys.stdout.write(
                f'The language "{args.to}" is not supported, please use one of the following languages: Chinese, English, German, Italian, Polish, Portuguese, Russian, Spanish, Swedish, French.\n'
            )
        if of != [True]:
            sys.stdout.write(
                f'The language "{args.of}" is not supported, please use one of the following languages: Chinese, English, German, Italian, Polish, Portuguese, Russian, Spanish, Swedish, French.\n'
            )


def systemLanguage():
    '''Function to detect the system language'''
    
    try:
        locate = getdefaultlocale()
        locate = locate[0]
        locate = locate.split("_")
        return locate[0]

    except: # Error
        sys.stdout.write(
            "Unexpected error when trying to get your language from the operating system (to avoid this error put -t or --to 'your language'), please report this error.\n"
        )

# Check script main
if __name__ == "__main__":
    main()