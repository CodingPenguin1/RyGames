"""RyGames
Ryan J. Slater
"""

__title__ = 'rygames'
# version may have no more then numerical digits after decimal point.
# 1.11 is actually a higher release than 1.2 (confusing)
__version__ = '0.1a4'
__author__ = u'Ryan J. Slater'
__license__ = ''
__copyright__ = 'Copyright 2017 Ryan J. Slater'
"""__all__ = ['sdof', 'mdof', 'ema', 'vibesystem', 'continuous_systems',
           '__version__']"""

"""
If the __all__ above is commented out, this code will then execute to
completion, as the default behaviour of import * is to import all symbols
that do not begin with an underscore, from the given namespace.

Reference:
https://docs.python.org/3.5/tutorial/modules.html#importing-from-a-package
"""

import pygame
import random as rand
import numpy as np
import matplotlib.pyplot as plt
from PyDictionary import PyDictionary
from nltk.corpus import words
import names
import os
import time
from rygames import __AIFleets__
from rygames import __AIShots__
from rygames import CoinGame
from rygames import CountryGuessingGame
from rygames import Hangman
from rygames import TicTacToe1Player
from rygames import TicTacToe2Player
from rygames import TwentyFortyEight
from rygames import Warships
