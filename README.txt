1. chmod.py - this is my beginners python script for chmod files by extension.
Usage: python chmod.php [ARGUMENTS]
-r - if set - recursive
-b (--bits) - new chmod for file without leading zero, e.g. 755 or 644
-e (--extension) - extension of the files which should be changed without . (e.g. php or html). Multiple extensions not supperted.
Or use standard --help (-h) to get help text.

2. iconv.py - this is my beginners python script for iconv files by extension.
Usage: python iconv.php [ARGUMENTS]
-r - if set - recursive
-e (--extension) - extension of the files which should be changed without . (e.g. php or html). Multiple extensions not supperted.
-n (--new) extension added for changed files (.new by default, file.php will be file.php.new)
-f (--from) encoding from (by default utf-8)
-t (--to) encoding to (by default cp1251)
Or use standard --help (-h) to get help text.

3. component_generator.py - script for creating 1c-bitrix components structure main files 
- component.php (with lang file for RU-language)
- .description.php (with lang file for RU-language)
- .parameters.php (with lang file for RU-language)
- template folder and default template file (with lang file for RU-language)

Use files or fork'em if U like.