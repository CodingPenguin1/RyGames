"""The Vibration Toolbox, Python Edition.
Joseph C. Slater and Raphael Timbó

`import vibration_toolbox as vtb` will keep them tucked behind `vtb`

`import vibration_toolbox.sdof as sdof` will tuck the sdof functions in the
 `sdof` name space.
"""

__title__ = 'rygames'
# version may have no more then numerical digits after decimal point.
# 1.11 is actually a higher release than 1.2 (confusing)
__version__ = '0.1a1'
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
