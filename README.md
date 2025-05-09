# restore-UTF8-saved-as-ANSI
This python program restores UTF-8 txt file saved as ANSI txt file

If the language of the document isn't russian you may need to tweak the number ("848")

How does it work:
- When you save a UTF-8 txt file as ANSI txt file text editor saves only the last byte of a symbol
- It happens because the size of a character in ANSI is 1 byte and the text editor can't save more information than 1 byte
- 1 byte equals to 8 bits, or 256 characters
- All the symbols of an alphabet (for example cyrillic/russian) in UTF-8 or ANSI go together
- So if you have found the code for "A" than the code for "B" will be the code for an "A" symbol plus one
- The smallest number (higher than 127) in my text was 192 so i decided that it's an "A" symbol
- Russian A symbol's code in UTF-8 is 1040.
- 1040-192=848
- So i added 848 to the code of every symbol and restored the document
