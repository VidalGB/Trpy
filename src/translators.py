from translate import Translator
from requests.exceptions import ConnectionError
from deep_translator import (
    GoogleTranslator,
    MicrosoftTranslator,
    MyMemoryTranslator,
    DeeplTranslator,
)
import sys

def deeplTranslate(args: tuple):
    '''DeepL translator function'''
    
    try:
        if args.dp: # DeepL Pro
            authKey = str(input("Enter the DeepL auth key to continue: "))
            if args.of == None:
                translation = DeeplTranslator(
                    api_key=authKey, source="auto", target=args.to, use_free_api=False
                ).translate(args.message)
            else:
                translation = DeeplTranslator(
                    api_key=authKey, source=args.of, target=args.to, use_free_api=False
                ).translate(args.message)
            sys.stdout.write(f"{translation}\n")

        else: # DeepL Free
            authKey = str(input("Enter the DeepL auth key to continue: "))
            if args.of == None:
                translation = DeeplTranslator(
                    api_key=authKey, source="auto", target=args.to, use_free_api=True
                ).translate(args.message)
            else:
                translation = DeeplTranslator(
                    api_key=authKey, source=args.of, target=args.to, use_free_api=True
                ).translate(args.message)
            sys.stdout.write(f"{translation}\n")

    except ConnectionError: # Connection Error
        sys.stdout.write(
            "Connection error, please provide your connection and try again.\n"
        )
    except deep_translator.exceptions.AuthorizationException as key:
        sys.stdout.write(f"{key}\n")
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")


def googleTranslate(args: tuple):
    '''Google translator function'''
    
    try:
        if args.of == None:
            translation = GoogleTranslator(source="auto", target=args.to).translate(
                text=args.message
            )
        else:
            translation = GoogleTranslator(source=args.of, target=args.to).translate(
                text=args.message
            )
        sys.stdout.write(f"{translation}\n")

    except ConnectionError: # Connection Error
        sys.stdout.write(
            "Connection error, please provide your connection and try again.\n"
        )
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")


def memoryTranslate(args: tuple):
    '''My Memory translator function'''
    try:
        if args.of == None:
            sys.stdout.write(
                "MyMemory translator does not have automatic language detection, please add a language with -o or --of (it can be shortened, example: 'en' or 'english'\n"
            )
        else:
            translation = MyMemoryTranslator(source=args.of, target=args.to).translate(
                args.message
            )
            sys.stdout.write(f"{translation}\n")

    except ConnectionError: # Connection Error
        sys.stdout.write(
            "Connection error, please provide your connection and try again.\n"
        )
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")


def microsoftTranslate(args: tuple):
    '''Microsoft translator function'''
    try:
        authKey = str(input("Enter the DeepL auth key to continue: "))
        if args.of == None:
            translation = MicrosoftTranslator(
                api_key=authKey, source="auto", target=args.to
            ).translate(text=args.message)
        else:
            translation = MicrosoftTranslator(
                api_key=authKey, source=args.of, target=args.to
            ).translate(text=args.message)
        sys.stdout.write(f"{translation}\n")

    except ConnectionError: # Connection Error
        sys.stdout.write(
            "Connection error, please provide your connection and try again.\n"
        )
    except deep_translator.exceptions.MicrosoftAPIerror as key:
        sys.stdout.write(f"Unauthorized access with this api key\n")
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")


def translate(args: tuple):
    '''Translator function'''
    
    try:
        translator = Translator(to_lang=args.to)
        if not args.of == None:
            translator = Translator(from_lang=args.of, to_lang=args.to)
        translation = translator.translate(args.message)
        sys.stdout.write(f"{translation}\n")

    except ConnectionError: # Connection Error
        sys.stdout.write(
            "Connection error, please provide your connection and try again.\n"
        )
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")
