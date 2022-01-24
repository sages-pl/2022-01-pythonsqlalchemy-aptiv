"""
>>> sys.tracebacklimit = 0
>>> assert sys.version_info > (3, 8, 0), \
'Python 3.8+ is required'
"""

import sys

current = sys.version[:6]
print('Your Python version: {current}')
