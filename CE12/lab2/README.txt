CE Lab 2 Write Up
Zac Plante (zplante)

PURPOSE
The purpose of this lab was to create a running adder that could store data,
mostly to be able to practice using Data-Latches to create a memory register.

METHODS
To create this running adder, a 6 bit long Register was created, using the
assembeled Flip-Flop in Starting_Parts.lgi. A 2-1 Mux was also used to invert
the input from the keypad to allow for subtration. A single bit adder was 
created using logic gates, and repeated six times to do the arithmatic. With 
all these peices in place, they were put together and attached to a display to
create the adder.

RESULTS
The adder can succefully to addition and subtration to a saved value in 6 bits. 
It can display values 00-3F in hexidecimal on two 7-segment displays.

ANALYSIS
When a number bigger than the current running sum is subtratcted from it, the 
loops around to the max values. Likewise, when the sum exceeds the displays 
maximum of 3F, it loops around to 00. This is because the adder can only work 
in up to 6 bits, so when that is exceded to high values are truncated off, 
like how truncated the tens place from 11 makes it appear to be 1. The display 
is also unable to show negative numbers, so it shows the max values instead 
(a result of 2s compliment). The adder could be modified to increase its 
register to work with more bits, but this p[roblem will always occur with 
large enough numbers. It could also be modified to be able to display negative 
numbers, but depending on the work needed this could be trivial. 