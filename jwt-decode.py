#!/usr/bin/env python3

import base64
import json
import sys

def format(data):
  decoded = str(base64.b64decode(data + '=='), 'utf-8')
  parsed = json.loads(decoded)
  return json.dumps(parsed, indent=2)

token = sys.argv[1]
token = token.strip().replace('\n', '')

header, payload, signature = token.split('.')

print()
print('Header:', format(header))
print('Payload:', format(payload))
print('Signature:', signature)
