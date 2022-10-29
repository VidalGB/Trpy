import threading
import sys
import argparse
from locale import getdefaultlocale
from tqdm import tqdm as tq
import time

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

def controlLanguage(args: argparse.Namespace, language: dict)-> bool:
    '''Control language suport'''

    of = bool([True for key, value in language.items() if args.of == key or args.of == value])
    to = bool([True for key, value in language.items() if args.to == key or args.to == value])
    return of and to

def systemLanguage()-> str:
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

def progressBar(traslator: ThreadWithReturnValue)-> str:
    progressBar = tq(total=50)
    while True:
        if not traslator.is_alive():
            progressBar.update(50)
            translation = traslator.join()
            progressBar._instances.pop().close()
            break
        time.sleep(0.1)
        progressBar.total += 10
        progressBar.update(10)
    return translation