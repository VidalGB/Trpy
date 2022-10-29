''' Python v3.9.2 more information and dependencies, read requirements.txt'''

# Imports
import argparse as arg
from src import translators as tr
from src import tools
import sys

def main():
    '''Main function'''

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
    app = arg.ArgumentParser(
        prog="Trpy",
        formatter_class=arg.RawDescriptionHelpFormatter,
        description="Trpy is a command line translator and open source, intended to be as practical and fast as possible.\nThe supported languages are: Chinese, English, German, Italian, Polish, Portuguese, Russian, Spanish, Swedish, French.\n\nThis Translator was developed by @VidalGB.\nYou can find the source code at: https://github.com/VidalGB/Trpy",
    )

    # Version argument
    app.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 1.1.0",
        help="show program's version number and exit.",
    )

    # Of language argument
    app.add_argument(
        "-o",
        "--of",
        type=str,
        default=None,
        help="Language of the text to be translated (it can be abbreviated, example: 'en' or 'english'), by default it is automatic, but it is not recommended.",
    )

    # To language argument
    app.add_argument(
        "-t",
        "--to",
        type=str,
        default=tools.systemLanguage(),
        help="Language to translate the text (it can be abbreviated, example: 'en' or 'english'), by default it is the language of your operating system.",
    )

    # Message argument
    app.add_argument(
        "-m",
        "--message",
        type=str,
        required=True,
        help='Text to translate, in quotes "Example".',
    )

    # DeepL translator argument (free)
    app.add_argument(
        "-d",
        action="store_true",
        help="Use the DeepL translator with auth key in version Free.",
    )

    # DeepL translator argument (pro)
    app.add_argument(
        "-dp",
        action="store_true",
        help="Use the DeepL translator with auth key in version Pro.",
    )

    # Microsoft translator argument
    app.add_argument(
        "-mi", action="store_true", help="Use the Microsoft translator."
    )

    # My memory translator argument
    app.add_argument("-me", action="store_true", help="Use the MyMemory translator.")

    # Google translator argument
    app.add_argument("-g", action="store_true", help="Use the Google translator.")
    
    args = app.parse_args()

    if tools.controlLanguage(args, language): # Controlling language
        
        # Referring translators
        if args.d:
            authKey = str(input("Enter the DeepL auth key to continue: "))
            traslator = tools.ThreadWithReturnValue(target=tr.deeplTranslate, args=(args,authKey))
        elif args.dp:
            authKey = str(input("Enter the DeepL auth key to continue: "))
            traslator = tools.ThreadWithReturnValue(target=tr.deeplTranslate, args=(args,authKey))
        elif args.g:
            traslator = tools.ThreadWithReturnValue(target=tr.googleTranslate, args=(args,))
        elif args.mi:
            authKey = str(input("Enter the DeepL auth key to continue: "))
            traslator = tools.ThreadWithReturnValue(target=tr.microsoftTranslate, args=(args,authKey))
        elif args.me:
            traslator = tools.ThreadWithReturnValue(target=tr.memoryTranslate, args=(args,))
        else:
            traslator = tools.ThreadWithReturnValue(target=tr.translate, args=(args,))
        traslator.start()

        translation = tools.progressBar(traslator)

        sys.stdout.write(' ' + translation + '\n')
    else:
        sys.stdout.write('A language is not supported, please use one of the following languages: Chinese, English, German, Italian, Polish, Portuguese, Russian, Spanish, Swedish, French.\n')

# Check script main
if __name__ == "__main__":
    main()