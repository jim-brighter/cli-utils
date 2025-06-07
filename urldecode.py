#!/usr/bin/env python3

from urllib.parse import unquote
import sys

print(unquote(sys.argv[1]))
