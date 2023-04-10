import os, sys

try:

    __import__("mw").o()

except Exception as e:

    exit(str(e))
