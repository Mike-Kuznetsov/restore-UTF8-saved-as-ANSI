# Restore-UTF8-saved-as-ANSI
This python program restores UTF-8 txt file saved as ANSI txt file

If the language of the document isn't russian you may need to tweak the number ("848")

How does it work:
- When you save a UTF-8 txt file as ANSI txt file text editor saves only the last byte of a symbol
- It happens because the size of a character in ANSI is 1 byte and the text editor can't save more information than 1 byte
- 1 byte equals to 8 bits, or 256 characters
- All the symbols of an alphabet (for example cyrillic/russian) in UTF-8 or ANSI go together
- So if you have found the code for "A" than the code for "B" will be the code for the "A" symbol plus one
- The smallest number (higher than 127) in my text was 192 so i decided that it's the code for the "A" symbol
- Russian A symbol's code in UTF-8 is 1040.
- 1040-192=848
- So i added 848 to the code of every symbol and restored the document

# Восстановить UTF-8 txt-файл сохраненный как ANSI txt-файл

Эта программа на Python восстанавливает txt-файл в кодировке UTF-8, сохраненный как файл в кодировке ANSI
Если язык документа не русский, вам может потребоваться изменить число 848

Как это работает:
- Когда вы сохраняете txt-файл UTF-8 как txt-файл ANSI, текстовый редактор сохраняет только последний байт символа
- Это происходит потому, что размер символа в ANSI составляет 1 байт, и текстовый редактор не может сохранить больше информации, чем 1 байт
- 1 байт равен 8 битам или 256 символам
- Все символы алфавита (например, кириллицы/русского) в UTF-8 или ANSI идут вместе
- Так что если вы нашли код для «A», то код для «B» будет кодом символа «A» плюс один
- Наименьшее число (выше 127) в моем тексте было 192, поэтому я решил, что это код символа "A"
- Код русского символа A в кодировке UTF-8 - 1040.
- 1040-192=848
- Поэтому я добавил 848 к коду каждого символа и восстановил документ
