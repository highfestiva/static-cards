#!/usr/bin/env python3

import json
import re


t = c = b = ''
alts = []
fn = 1

def w():
    global fn, c
    with open('%s.json'%fn, 'w') as f:
        c = r'<img src=\"%s\"/>'%c if c.strip() else ''
        a = []
        for alt in alts:
            alt = [w.strip() for w in alt.split('|')]
            a.append(r'"<a href=\"%s\">%s<img src=\"cards/%s\"/></a>"' % (alt[2],alt[0].strip(' -'),alt[1]))
        a = '[' + ',\n       '.join(a) + ']'
        print('{"t": "%s",'%t, file=f)
        print(' "c": "%s",'%c, file=f)
        print(' "b": "%s",'%b, file=f)
        print(' "f": %s  }'%a, file=f)
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
orig_s = open('../index.html').read()
s = ''.join([re.sub(r'(maxStep =) (\d+)', r'\1 %s'%max_cards, line) for line in open('../index.html')])
if s != orig_s:
    print(s, end='', file=open('../index.html','w'))
    print('rewrote index.html')
