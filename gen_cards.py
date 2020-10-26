#!/usr/bin/env python3

import json
import re


t = c = b = ''
alts = []
fn = 1

def w():
    global fn
    with open('%s.json'%fn, 'w') as f:
        print('{"t": "%s",'%t, file=f)
        print(' "c": "%s",'%c, file=f)
        print(' "b": "%s",'%b, file=f)
        print(' "f": %s  }'%str(alts).replace("'",'"'), file=f)
    fn += 1


for line in open('cards.txt'):
    line = line.strip()
    if (not t or b) and not line:
        continue
    if '-----' in line:
        w()
        t = c = b = ''
        alts = []
    elif line.startswith('-'):
        alts += [line]
    elif not t:
        t = line
    elif not c:
        c = line or ' '
    elif not b:
        b = line or ' '
    else:
        assert False, line

if t:
    w()

max_cards = fn-1
s = ''.join([re.sub(r'(maxStep =) (\d+)', r'\1 %s'%max_cards, line) for line in open('index.html')])
print(s, end='', file=open('index.html','w'))
