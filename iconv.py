# -*- coding: utf-8 -*-

# okay here we go
# command line arguments:
#   iconv files from to 
#   -e(--extension) '*' (all) by default
#   -f(--from) 
#   -t(--to)
#   -n(--new)
#   -r - recusrsive (true/false)

import os # useful library for working with paths
from optparse import OptionParser
import codecs

def main():
    parser = OptionParser()
    parser.add_option("-e", "--extension", action="store", type="string",dest="extension", default="*")
    parser.add_option("-f", "--from", action="store", type="string", dest="charset_from", default='utf-8')
    parser.add_option("-t", "--to", action="store", type="string", dest="charset_to", default='cp1251')
    parser.add_option("-n", "--new", action="store", dest="new", default='.new')
    parser.add_option("-r", action="store_true", dest="recursive", default=False)
    (options, args) = parser.parse_args()
    files_cou = 0
    for dirpath,dirnames,filenames in os.walk(os.getcwd()):
        for file in filenames:
            if os.path.splitext(file)[-1] == '.' + options.extension or options.extension == '*':
                filedata = open(file, 'r').read()
                try:
                    data = filedata.decode(options.charset_from)
                except Exception:
                    continue
                newfile = open(os.path.join(dirpath, file) + options.new, 'w')
                try:
                    newfile.write(data.encode(options.charset_to))
                except Exception:
                    continue
                finally:
                    newfile.close()
                    files_cou += 1
        if not options.recursive: break
    print '%d file(s) were converted' % files_cou
    return

if __name__ == '__main__':
    main()