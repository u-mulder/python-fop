# -*- coding: utf-8 -*-

import os

def main():
    cwd = os.getcwd()
    file_content = {
        'u': '<?php\nif(!defined("B_PROLOG_INCLUDED") || B_PROLOG_INCLUDED!==true) die();\n\n\n?>',
        'l': "<?php\n$MESS[''] = '';\n?>"
    }        
    file_paths = {'component.php':'u', '.description.php':'u', '.parameters.php':'u',
        'templates/.default/template.php':'u', 'lang/ru/component.php':'l', 'lang/ru/.parameters.php':'l',
        'lang/ru/.description.php':'l', 'templates/.default/lang/ru/template.php':'l'}
    for key in file_paths:
        if key.find('/') != -1:
            new_dir = os.path.dirname(key)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
        new_file = open(os.path.join(cwd, key), 'w')
        try:
            new_file.write(file_content[file_paths[key]])
        except Exception:
            continue
        finally:
            new_file.close()
    return
    
if __name__ == '__main__':
    main()

