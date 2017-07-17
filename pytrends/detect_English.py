# -*- coding: utf-8 -*-
def isEnglish(s):
    try:
        s.decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

print isEnglish('::M∆DE::IN::HEIGHTS::')
print isEnglish('10:32')
print isEnglish('(həd) p.e.')
