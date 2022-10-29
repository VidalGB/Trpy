from translate import Translator
from requests.exceptions import ConnectionError
import deep_translator
from deep_translator import (
    GoogleTranslator,
    MicrosoftTranslator,
    MyMemoryTranslator,
    DeeplTranslator,
)
import argparse

def deeplTranslate(args: argparse.Namespace, authKey: str)-> str:
    '''DeepL translator function'''
    
    try:
        if args.dp: # DeepL Pro
            if args.of == None:
                translation = DeeplTranslator(
                    api_key=authKey, source="auto", target=args.to, use_free_api=False
                ).translate(args.message)
            else:
                translation = DeeplTranslator(
                    api_key=authKey, source=args.of, target=args.to, use_free_api=False
                ).translate(args.message)
            return translation

        else: # DeepL Free
            if args.of == None:
                translation = DeeplTranslator(
                    api_key=authKey, source="auto", target=args.to, use_free_api=True
                ).translate(args.message)
            else:
                translation = DeeplTranslator(
                    api_key=authKey, source=args.of, target=args.to, use_free_api=True
                ).translate(args.message)
            return translation

    except ConnectionError: # Connection Error
        return "Connection error, please provide your connection and try again.\n"
    except deep_translator.exceptions.AuthorizationException as key:
        return key
    except Exception as e:
        return f"Unexpected error, please report this error.\nThe error[{e}]"


def googleTranslate(args: tuple)-> str:
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
        return translation

    except ConnectionError: # Connection Error
        return "Connection error, please provide your connection and try again.\n"
    except Exception as e:
        return f"Unexpected error, please report this error.\nThe error[{e}]"


def memoryTranslate(args: tuple)-> str:
    '''My Memory translator function'''
    try:
        if args.of == None:
            return "MyMemory translator does not have automatic language detection, please add a language with -o or --of (it can be shortened, example: 'en' or 'english'\n"
        else:
            translation = MyMemoryTranslator(source=args.of, target=args.to).translate(
                args.message
            )
            return translation

    except ConnectionError: # Connection Error
        return "Connection error, please provide your connection and try again.\n"
    except Exception as e:
        return f"Unexpected error, please report this error.\nThe error[{e}]"


def microsoftTranslate(args: tuple, authKey: str)-> str:
    '''Microsoft translator function'''

    try:
        if args.of == None:
            translation = MicrosoftTranslator(
                api_key=authKey, source="auto", target=args.to
            ).translate(text=args.message)
        else:
            translation = MicrosoftTranslator(
                api_key=authKey, source=args.of, target=args.to
            ).translate(text=args.message)
        return translation

    except ConnectionError: # Connection error
        return "Connection error, please provide your connection and try again.\n"
    except deep_translator.exceptions.MicrosoftAPIerror: # API key error
        return f"Unauthorized access with this api key {authKey}\n"
    except Exception as e: # Error undefined
        return f"Unexpected error, please report this error.\nThe error[{e}]"


def translate(args: argparse.Namespace)-> str:
    '''Translator function default'''

    try:
        translator = Translator(to_lang=args.to)
        if not args.of == None:
            translator = Translator(from_lang=args.of, to_lang=args.to)
        translation = translator.translate(args.message)
        return translation
    except ConnectionError: # Connection error
        return "Connection error, please provide your connection and try again.\n"
    except Exception as e: # Error undefined
        return f"Unexpected error, please report this error.\nThe error[{e}]"
