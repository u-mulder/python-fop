# -*- coding: utf-8 -*-

# okay here we go
# command line arguments:
#   -e(--extension) '*' (all) by default
#   -b(--bits) '755' by default
#   -r - recusrsive (true/false)

import os # useful library for working with paths
from optparse import OptionParser

def main():
    parser = OptionParser()
    parser.add_option("-e", "--extension", action="store", type="string",dest="extension", default="*")
    parser.add_option("-b", "--bits", action="store", type="string", dest="bits", default='755')
    parser.add_option("-r", action="store_true", dest="recursive", default=False)
    (options, args) = parser.parse_args()
    files_cou = 0
    for dirpath,dirnames,filenames in os.walk(os.getcwd()):
        for file in filenames:
            if os.path.splitext(file)[-1] == '.' + options.extension or options.extension == '*':
                os.chmod(os.path.join(dirpath, file), int(options.bits, 8))
                files_cou += 1
        if not options.recursive: break
    print 'chmod for %d file(s) were changed' % files_cou
    return

if __name__ == '__main__':
    main()