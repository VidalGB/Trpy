# Python v3.9.2 more information and dependencies, read requirements.txt
# Syntax camelCase

# Imports
import argparse
from translate import Translator
from locale import getdefaultlocale
from requests.exceptions import ConnectionError
from deep_translator import (GoogleTranslator, MicrosoftTranslator, MyMemoryTranslator, DeeplTranslator)
import sys

# Main function
def main():
    langSystem = systemLanguage()
    language = {'zh': 'chinese', 'en': 'english', 'de': 'german', 'it': 'italian', 'pl': 'polish', 'pt': 'portuguese', 'ru': 'russian', 'es': 'spanish', 'sv': 'swedish', 'fr': 'french', None: None}

    parser = argparse.ArgumentParser(prog = 'Trpy', usage = '%(prog)s hola', formatter_class = argparse.RawDescriptionHelpFormatter, description = "Trpy is a command line translator, intended to be as practical and fast as possible.\n\nThe supported languages are: Chinese English German Italian Polish Portuguese Russian Spanish Swedish French.")

    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 0.1')

    parser.add_argument("-o","--of", type = str, default = None, help = "Language of the text to be translated (it can be shortened, example: 'en' or 'english'), by default it is automatic, but it is not recommended.")

    parser.add_argument("-t", "--to", type = str, default = f"{language[langSystem]}", help = "Language to translate the text (it can be shortened, example: 'en' or 'english'), by default it is the language of your operating system.")

    parser.add_argument("-m", "--message", type = str, required = True, help = 'Text to translate, in quotes "Example".')

    parser.add_argument("-d", action = 'store_true', help = 'Use the DeepL translator with auth key in version Free')

    parser.add_argument("-dp", action = 'store_true', help = 'Use the DeepL translator with auth key in version Pro')

    parser.add_argument("-mi", action = 'store_true', help = 'Use the Microsoft translator')

    parser.add_argument("-me", action = 'store_true', help = 'Use the MyMemory translator')

    parser.add_argument("-g", action = 'store_true', help = 'Use the Google translator')

    args = parser.parse_args()
    translator(args, language)

def translator(args, language):
    of = [True for key, value in language.items() if args.of == key or args.of == value]
    to = [True for key, value in language.items() if args.to == key or args.to == value]
    if to == [True] and of == [True]:
        if args.d:
            deeplTranslate(args)
        elif args.dp:
            deeplTranslate(args)
        elif args.g:
            googleTranslate(args)
        elif args.mi:
            microsoftTranslate(args)
        elif args.me:
            memoryTranslate(args)
        else:
            translate(args)
    else:
        if not to == [True]:
            sys.stdout.write(f'The language "{args.to}" is not supported, please use one of the following languages: Chinese, English, German, Italian, Polish, Portuguese, Russian, Spanish, Swedish, French.')
        if not of == [True]:
            sys.stdout.write(f'The language "{args.of}" is not supported, please use one of the following languages: Chinese, English, German, Italian, Polish, Portuguese, Russian, Spanish, Swedish, French.')

def deeplTranslate(args):
    try:
        if args.dp:
            authKey = str(input('Enter the DeepL auth key to continue: '))
            if args.of == None:
                translation = DeeplTranslator(api_key = authKey, source = "auto", target = args.to, use_free_api = False).translate(args.message)
            else:
                translation = DeeplTranslator(api_key = authKey, source = args.of, target = args.to, use_free_api = False).translate(args.message)
            sys.stdout.write(translation)
        else:
            authKey = str(input('Enter the DeepL auth key to continue: '))
            if args.of == None:
                translation = DeeplTranslator(api_key = authKey, source = "auto", target = args.to, use_free_api = True).translate(args.message)
            else:
                translation = DeeplTranslator(api_key = authKey, source = args.of, target = args.to, use_free_api = True).translate(args.message)
            sys.stdout.write(translation)
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.')

def googleTranslate(args):
    try:
        if args.of == None:
            translation = GoogleTranslator(source = 'auto', target = args.to).translate(text = args.message)
        else:
            translation = GoogleTranslator(source = args.of, target = args.to).translate(text = args.message)
        sys.stdout.write(translation)
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.')

def memoryTranslate(args):
    try:
        if args.of == None:
            sys.stdout.write("MyMemory translator does not have automatic language detection, please add a language with -o or --of (it can be shortened, example: 'en' or 'english'\n")
        else:
            translation = MyMemoryTranslator(source = args.of, target = args.to).translate(args.message)
            sys.stdout.write(translation)
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.')

def microsoftTranslate(args):
    try:
        authKey = str(input('Enter the DeepL auth key to continue: '))
        if args.of == None:
            translation = MicrosoftTranslator(api_key = authKey, source = "auto", target = args.to).translate(text = args.message)
        else:
            translation = MicrosoftTranslator(api_key = authKey, source = args.of, target = args.to).translate(text = args.message)
        sys.stdout.write(translation)
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.')

def translate(args):
    try:
        translator = Translator(to_lang = args.to)
        if not args.of == None:
            translator = Translator(from_lang = args.of,to_lang = args.to)
        translation = translator.translate(args.message)
        sys.stdout.write(translation)
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.')


def systemLanguage():
    try:
        locate = getdefaultlocale()
        locate = locate[0]
        locate = locate.split("_")
        locate = locate[0]
        return locate


    except:
        sys.stdout.write("Unexpected error when trying to get your language from the operating system (to avoid this error put -t or --to 'your language'), please report this error.\n")

# Check script main
if __name__ == '__main__':
    main()