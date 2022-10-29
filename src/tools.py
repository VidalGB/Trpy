import threading
import sys
from locale import getdefaultlocale

class ThreadWithReturnValue(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        threading.Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        threading.Thread.join(self, *args)
        return self._return

def controlLanguage(args, language):
    '''Control language suport'''

    of = bool([True for key, value in language.items() if args.of == key or args.of == value])
    to = bool([True for key, value in language.items() if args.to == key or args.to == value])
    return of and to

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
        sys.exit()