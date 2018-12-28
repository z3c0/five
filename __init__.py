from .propublica import *
from .twitter.twitter import *

def main():
    """the required actions upon initialization"""
    import os
    import sys
    modules = ['core', 'propublica', 'twitter']
    module_path = [os.path.join(os.path.dirname(__file__), module)
                   for module in modules]

    sys.path.append(module_path)


main()
