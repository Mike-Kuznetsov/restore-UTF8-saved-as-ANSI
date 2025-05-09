# This program restores UTF-8 txt file that was saved as ANSI file
# If the language of the document isn't russian you may need to tweak the number
#
# github.com/Mike-Kuznetsov
# youtube.com/@ESPdev
# youtube.com/c/MautozTech

f = open("ReadMe.txt", "r") # Here write path or name to the "damaged" file
res_file = open("result.txt", "w", encoding="utf-8") # Here write the name of a new file

for line in f.readlines():
    result_line = ""
    for i in line:
        if ord(i)<128:
            result_line += i    
        else:
            result_line += chr(ord(i)+848) # "848" is the number you need to tweak to fit your language
                                           # "ord(i)" gets ANSI code of a symbol and "+848" converts it back into UTF-8 
    res_file.write(result_line)

f.close()
res_file.close()
