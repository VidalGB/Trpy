# Python v3.9.2 more information and dependencies, read requirements.txt
# Syntax camelCase

# Imports
import argparse
from translate import Translator
from locale import getdefaultlocale
from deep_translator import (GoogleTranslator, MicrosoftTranslator, MyMemoryTranslator, DeeplTranslator)
import sys

# Main function
def main():
    language = {'zh': 'chinese', 'en': 'english', 'de': 'german', 'is': 'icelandic', 'it': 'italian', 'ku': 'kurdish', 'nb': 'norwegian', 'pl': 'polish', 'pt': 'portuguese', 'ru': 'russian', 'sr': 'serbian', 'es': 'spanish', 'sv': 'swedish', 'tr': 'turkish', 'cy': 'welsh', 'ca': 'catalan', 'fr': 'french'}
    langSystem = systemLanguage()

    parser = argparse.ArgumentParser(prog = 'Trpy', usage = '%(prog)s hola', formatter_class = argparse.RawDescriptionHelpFormatter, description = "Trpy is a command line translator, intended to be as practical and fast as possible.\n----------------------------------\nThe supported languages are: English, Chinese, German, Italian, Icelandic, Kurdish, Norwegian, Polish, Portuguese, Russian, Serbian, Spanish, Swedish, Turkish, French, Catalan, Welsh.")

    parser.add_argument('-v', '--version', action = 'version', version = '%(prog)s 0.1')

    parser.add_argument("-o","--of", type = str, default = None, help = "Language of the text to be translated (it can be shortened, example: 'en' or 'english'), by default it is automatic, but it is not recommended.")

    parser.add_argument("-t", "--to", type = str, default = f"{language[langSystem]}", help = "Language to translate the text (it can be shortened, example: 'en' or 'english'), by default it is the language of your operating system.")

    parser.add_argument("-m", "--message", type = str, default = "", help = 'Text to translate, in quotes "Example".')

    parser.add_argument("-d", action = 'store_true', help = 'Use the DeepL translator with auth key in version Free')

    parser.add_argument("-dp", action = 'store_true', help = 'Use the DeepL translator with auth key in version Pro')

    parser.add_argument("-mi", action = 'store_true', help = 'Use the Microsoft translator')

    parser.add_argument("-me", action = 'store_true', help = 'Use the MyMemory translator')

    parser.add_argument("-g", action = 'store_true', help = 'Use the Google translator')

    args = parser.parse_args()
    print(args)
    if args.message == '':
        sys.stdout.write('There is no message to translate, please use -m or --message, to write a message (this must be in quotes).\n')
    else:
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

def deeplTranslate(args):
    try:
        if args.dp:
            print('DeepL Pro')
            authKey = str(input('Enter the DeepL auth key to continue: '))
            if args.of == None:
                print('Auto')
                translation = DeeplTranslator(api_key = authKey, source = "auto", target = args.to, use_free_api = False).translate(args.message)
            else:
                translation = DeeplTranslator(api_key = authKey, source = args.of, target = args.to, use_free_api = False).translate(args.message)
            sys.stdout.write(translation)
        else:
            print('DeepL Free')
            authKey = str(input('Enter the DeepL auth key to continue: '))
            if args.of == None:
                print('Auto')
                translation = DeeplTranslator(api_key = authKey, source = "auto", target = args.to, use_free_api = True).translate(args.message)
            else:
                translation = DeeplTranslator(api_key = authKey, source = args.of, target = args.to, use_free_api = True).translate(args.message)
            sys.stdout.write(translation)
    except Exception as e:
        print(e)

def googleTranslate(args):
    try:
        print('Google')
        if args.of == None:
            print('Auto')
            translation = GoogleTranslator(source = 'auto', target = args.to).translate(text = args.message)
        else:
            translation = GoogleTranslator(source = args.of, target = args.to).translate(text = args.message)
        sys.stdout.write(translation)
    except Exception as e:
        print(e)

def memoryTranslate(args):
    try:
        print('Memory')
        if args.of == None:
            sys.stdout.write("MyMemory translator does not have automatic language detection, please add a language with -o or --of (it can be shortened, example: 'en' or 'english'\n")
        else:
            translation = MyMemoryTranslator(source = args.of, target = args.to).translate(args.message)
            sys.stdout.write(translation)
    except Exception as e:
        print(e)

def microsoftTranslate(args):
    try:
        print('Microsoft')
        authKey = str(input('Enter the DeepL auth key to continue: '))
        if args.of == None:
            print('Auto')
            translation = MicrosoftTranslator(api_key = authKey, source = "auto", target = args.to).translate(text = args.message)
        else:
            translation = MicrosoftTranslator(api_key = authKey, source = args.of, target = args.to).translate(text = args.message)
        sys.stdout.write(translation)
    except Exception as e:
        print(e)

def translate(args):
    try:
        print('translate')
        translator = Translator(to_lang = args.to)
        if not args.of == None:
            print('Auto')
            translator = Translator(from_lang = args.of,to_lang = args.to)
        translation = translator.translate(args.message)
        sys.stdout.write(translation)
    except Exception as e:
        print(e)

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