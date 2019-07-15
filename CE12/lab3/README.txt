Zachary Plante (zplante)
CE 12, Lab 3
Write-Up
PURPOSE
The purpose of thsi lab was to create a MIPS program that takes in a string, 
convert it to an integer, and printing that integer as a 2's compliment binary 
number. This was done in order to practice a few important concepts, such as 
Assembly Language and Bit Masking.
METHODS
This program utilizes 3 major algorithims, one to convert the string to an 
integer, one to convert the number to 2's comliment, and one to print it in 
binary. The first uses and adding loop, converting the ascii value into the 
integer it repersents by subtracting 48. It then multiplies the current value 
by 10 and adding the new value, resulting in the repersented integer. 
The next converts it to 2's compliment. It only does this when a negative flag 
is up, and it does this by XoR the value with the max possible value (ffffffff) 
repersented by "-1", and then adding 1. 
The final one print the number. It does this by ANDing it with a shifting bit 
mask to check each digit. If the value is 0 it prints 0, otherwise it prints 1.
RESULTS
The algorithims successfully worked and can print binary numbers. However, 
there are no checks for illegal (non-numerical) inputs.
ANALYSIS
This Lab assists in teaching several asemmbly language, such as register 
management, syscalls, and BitWise operations.