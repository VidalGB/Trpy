from deep_translator import GoogleTranslator, MicrosoftTranslator, MyMemoryTranslator, DeeplTranslator
from translate import Translator
from requests.exceptions import ConnectionError
import sys

# DeepL translator function
def deeplTranslate(args):
    try:

# DeepL Pro
        if args.dp:
            authKey = str(input('Enter the DeepL auth key to continue: '))
            if args.of == None:
                translation = DeeplTranslator(api_key = authKey, source = "auto", target = args.to, use_free_api = False).translate(args.message)
            else:
                translation = DeeplTranslator(api_key = authKey, source = args.of, target = args.to, use_free_api = False).translate(args.message)
            sys.stdout.write(f'{translation}\n')

# DeepL Free
        else:
            authKey = str(input('Enter the DeepL auth key to continue: '))
            if args.of == None:
                translation = DeeplTranslator(api_key = authKey, source = "auto", target = args.to, use_free_api = True).translate(args.message)
            else:
                translation = DeeplTranslator(api_key = authKey, source = args.of, target = args.to, use_free_api = True).translate(args.message)
            sys.stdout.write(f'{translation}\n')

# Connection Error
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.\n')
    except deep_translator.exceptions.AuthorizationException as key:
        sys.stdout.write(f'{key}\n')
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")

# Google translator function
def googleTranslate(args):
    try:
        if args.of == None:
            translation = GoogleTranslator(source = 'auto', target = args.to).translate(text = args.message)
        else:
            translation = GoogleTranslator(source = args.of, target = args.to).translate(text = args.message)
        sys.stdout.write(f'{translation}\n')

# Connection Error
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.\n')
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")

# My Memory translator function
def memoryTranslate(args):
    try:
        if args.of == None:
            sys.stdout.write("MyMemory translator does not have automatic language detection, please add a language with -o or --of (it can be shortened, example: 'en' or 'english'\n")
        else:
            translation = MyMemoryTranslator(source = args.of, target = args.to).translate(args.message)
            sys.stdout.write(f'{translation}\n')

# Connection Error
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.\n')
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")

# Microsoft translator function
def microsoftTranslate(args):
    try:
        authKey = str(input('Enter the DeepL auth key to continue: '))
        if args.of == None:
            translation = MicrosoftTranslator(api_key = authKey, source = "auto", target = args.to).translate(text = args.message)
        else:
            translation = MicrosoftTranslator(api_key = authKey, source = args.of, target = args.to).translate(text = args.message)
        sys.stdout.write(f'{translation}\n')

# Connection Error
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.\n')
    except deep_translator.exceptions.MicrosoftAPIerror as key:
        sys.stdout.write(f'Unauthorized access with this api key\n')
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")


# Translator function
def translate(args):
    try:
        translator = Translator(to_lang = args.to)
        if not args.of == None:
            translator = Translator(from_lang = args.of,to_lang = args.to)
        translation = translator.translate(args.message)
        sys.stdout.write(f'{translation}\n')

# Connection Error
    except ConnectionError:
        sys.stdout.write('Connection error, please provide your connection and try again.\n')
    except:
        sys.stdout.write("Unexpected error, please report this error.\n")
