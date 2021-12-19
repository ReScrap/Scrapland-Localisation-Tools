# SCRAPLAND LOCALISATION TOOLS

The Scrapland localisation files are located in the `Scrapland\Language` folder. You can easily mod them, but only if lines are written with ASCII characters. 

The Problem starts when non-ASCII characters are used in your language. Characters are presented by their UTF-16BE (Big Endian) HEX value with a `0x01` byte at the start of every character.

To change these lines you need to decode them into human-readable format, then encode them back to the Scrapland format. 

This is what these tools are for.

### HOW TO SETUP
- Make sure you have Python 3 installed on your system [https://www.python.org/](https://www.python.org/)
- Checkout this Repository using [git](https://git-scm.com/downloads)
- **or** Download [functions.py](functions.py), then [decode.py](decode.py) and [encode.py](encode.py) separately  
*(Click on "Raw" and then use your browsers "Save Page as" function)*

### HOW TO USE

In your command line window, after navigating into the folder with the python scripts, use the following commands to decode & encode the language files:

* Decode: 
```bash
$ python3 decode.py <filename.txt>
```
This will output a human-readable version of the provided file with the name <filename_decoded.txt>


* Encode: 
```bash
$ python3 encode.py <filename.txt>
```
This will output a version of the provided file encoded for Scrapland with the name <filename_encoded.txt>

### HOW TO USE THE NEW TRANSLATION

Just replace the file `Scrapland\Language\<Your_language.txt>` and run the game.
