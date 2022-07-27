import argparse
from translate import Translator
from locale import getdefaultlocale
import sys

def main():
    language = {'zh': 'chinese', 'en': 'english', 'de': 'german', 'is': 'icelandic', 'it': 'italian', 'ja': 'japanese', 'ko': 'korea', 'ku': 'kurdish', 'nb': 'norwegian', 'pl': 'polish', 'pt': 'portuguese', 'ru': 'russian', 'sr': 'serbian', 'es': 'spanish', 'sv': 'swedish', 'tr': 'turkish', 'cy': 'welsh'}
    parser = argparse.ArgumentParser(description = "Trpy is a command line translator, intended to be as practical and fast as possible. The supported languages are: English, Chinese, German, Italian, Icelandic, Japanese, Korea, Kurdish, Norwegian, Polish, Portuguese, Russian, Serbian, Spanish, Swedish, Turkish, Welsh.")
    langSystem = systemLanguage()
    parser.add_argument("-o","--of", type = str, default = None, help = "Language of the text to be translated (it can be shortened, example: 'en' or 'english'), by default it is automatic, but it is not recommended.")
    parser.add_argument("-t", "--to", type = str, default = f"{language[langSystem]}", help = "Language to translate the text (it can be shortened, example: 'en' or 'english'), by default it is the language of your operating system.")
    parser.add_argument("-m", "--message", type = str, default = "", help = 'Text to translate, in quotes "Example".')

    args = parser.parse_args()

def systemLanguage():
    locate = getdefaultlocale()
    locate = locate[0]
    locate = locate.split("_")
    locate = locate[0]
    return locate

if __name__ == '__main__':
    main()