Zachary Plante (zplante)
CE 12, Lab 5
Write-Up
PURPOSE
The purpose of this lab was to create a Vigenère cipher using a key and 
clear text from the program arguments. Two functions were used for this: one 
that encrypts the clear text and one that decrypts the the encrypted text from 
the frist function.
METHODS
The program utilizes the fact that ASCII characters are represented by integers 
to handle the cypher. the functions loop through the key and text, adding the 
values together for encrypting and subtracting them for decrypting. Wrap around 
is handled so the value is between 0 and 127, and value is added to the new 
string.
RESULTS
The functions work succesfully as described in the lab and results in the 
encrypted and decrypted strings being saved in the data segment. However, it 
cannot preform in a handful of edge cases. If the cypher results in the null 
character \0 then the string will terminate and not print properly. The cypher 
can also result in the new line character \n and some non-printiable characters 
that will cause the string to not print properly, even though in memory it is 
repersented as it should be.
ANALYSIS
This lab utilizes functions in MIPS. These funtion similar to the jump command, 
but use jal in stead to save the line to return to. This way, funtions can be 
used multiple times within a single main function. To do this, the strings must 
be moved to the argument registers. These functions work similarly, with encode 
adding the key and decode subtracting it. Encode uses modulo to handle wrap 
around while decode adds 128 to the value if it is negative. in retrospec, 
modulo could have also been used for this.