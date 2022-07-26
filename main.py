import argparse
from translate import Translator
from locale import getdefaultlocale

import sys # sys.stdout.write()

def main():
    parser = argparse.ArgumentParser(description = 'Process some integers.')

    parser.add_argument("-i", type = str, default = "english", help = "lenguaje del texto atraducir")
    parser.add_argument("-i", type = str, default = "english", help = "lenguaje del texto atraducir")

    args = parser.parse_args()
    print(args.accumulate(args.integers))

def translate():
    translator = Translator(from_lang="german",to_lang="spanish")
    translation = translator.translate("Guten Morgen")
    print(translation)

if __name__ == '__main__':
    main()