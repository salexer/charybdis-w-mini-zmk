import json,sys
layout=json.load(open('imp.vil'))['layout'][:16]
def conv(c):
    if c==-1: return '&none'
    if isinstance(c,str) and c.startswith('TD('): return f'&td_{c[3:-1]}'
    if isinstance(c,str) and c.startswith('MO('): return f'&mt {c[3:-1]}'
    if isinstance(c,str) and c.startswith('KC_'): return f'&kp {c}'
    if isinstance(c,str) and c.startswith('LCTL('): return f'&mt LCTRL {c[5:-1]}'
    if isinstance(c,str) and c.startswith('LALT('): return f'&mt LALT {c[5:-1]}'
    return f'&kp {c}'
for idx,layer in enumerate(layout):
    print(f'{idx} '+'{')
    print('    bindings = <')
    for row in layer:
        print('        '+' '.join(conv(c) for c in row))
    print('    >;')
    print('};')