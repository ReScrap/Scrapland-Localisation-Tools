# SCRAPLAND LOCALISATION TOOLS

Scrapland localisation files are located in Scrapland\Language foler. You can esaly mod them, but only if lines are written with ASCII characters. 

Problem starts when in your language non-ASCII characters are used. Characters are presented by their UTF-16BE (Big Endian) HEX value with 0x01 byte at start of every character.

To change these lines you need to decode them to human-readble format, then encode them back to scrapland-readble format. 

That what this tools do.

### HOW TO USE TOOLS

* Decode: 
```bash
$ python3 decode.py <filename.txt>
```
This will output human-readble version of provided file with <filename_decoded.txt> name


* Encode: 
```bash
$ python3 encode.py <filename.txt>
```
This will output scrapland-readble version of provided file with <filename_encoded.txt> name

### HOW TO USE NEW TRANSLATION

Just replace file Scrapland\Language\<Your_language.txt> and run the game.
