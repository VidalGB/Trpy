import argparse
from translate import Translator
from locale import getdefaultlocale
import sys

def main():
    language = {'zh': 'chinese', 'en': 'english', 'de': 'german', 'is': 'icelandic', 'it': 'italian', 'ja': 'japanese', 'ko': 'korea', 'ku': 'kurdish', 'nb': 'norwegian', 'pl': 'polish', 'pt': 'portuguese', 'ru': 'russian', 'sr': 'serbian', 'es': 'spanish', 'sv': 'swedish', 'tr': 'turkish', 'cy': 'welsh'}
    langSystem = systemLanguage()

    parser = argparse.ArgumentParser(description = "Trpy is a command line translator, intended to be as practical and fast as possible. The supported languages are: English, Chinese, German, Italian, Icelandic, Japanese, Korea, Kurdish, Norwegian, Polish, Portuguese, Russian, Serbian, Spanish, Swedish, Turkish, Welsh.")

    parser.add_argument("-o","--of", type = str, default = None, help = "Language of the text to be translated (it can be shortened, example: 'en' or 'english'), by default it is automatic, but it is not recommended.")

    parser.add_argument("-t", "--to", type = str, default = f"{language[langSystem]}", help = "Language to translate the text (it can be shortened, example: 'en' or 'english'), by default it is the language of your operating system.")
    
    parser.add_argument("-m", "--message", type = str, default = "", help = 'Text to translate, in quotes "Example".')

    args = parser.parse_args()
    print('args: ', args)
    if args.message == '':
        sys.stdout.write('There is no message to translate, please use -m or --message, to write a message (this must be in quotes)')
    else:
        sys.stdout.write(translate(args))

def translate(args):
    translator = Translator(to_lang = args.to)
    if not args.of == None:
        translator = Translator(from_lang = args.of,to_lang = args.to)
    translation = translator.translate(args.message)
    return translation

def systemLanguage():
    locate = getdefaultlocale()
    locate = locate[0]
    locate = locate.split("_")
    locate = locate[0]
    return locate

if __name__ == '__main__':
    main()