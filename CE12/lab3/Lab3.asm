#Zachary Plante (zplante)
#CS 12 Lab 3
#Convert an Integer from a string and print in 2's Compliment Binary
#Some code borrowed from BaseFile.asm by Max Dunne
.text
main:
	move	 $s0,$a1
	lw	 $s0,($s0)
	la	 $a0, hello_msg # load the addr of hello_msg into $a0.
	li	 $v0, 4 # 4 is the print_string syscall.
	syscall 	# do the syscall.
	la	$a0, ($s0)
	syscall
	li 	$t2,0
	li	$t0, 1	# creates negative flag	
	lb 	$t1,0($s0)
	bne 	$t1,45,IFPOS
	nop
	add	$t2,$t2,1
	mul 	$t0,$t0,-1
IFPOS: 	
	nop
	nop
	li	$t3,0
ADDINGLOOP:		#loop taht converts ascii string into int
	add	$t5, $s0, $t2			#pulls char
	lb	$t4,0($t5)			#stores char
	beq 	$t4,$zero,EXITONE
	sub 	$t4,$t4,48
	mul 	$t3,$t3,10
	add 	$t3,$t3,$t4
	add	$t2,$t2,1			#incraeses index
	j 	ADDINGLOOP
	
EXITONE:
	bne 	$t0,-1,POSFLAG
	XOr 	$t3,$t0,$t3			#converts to 2's compliment
	add	$t3,$t3,1
	
POSFLAG:
	nop
	

	la	$a0, goodbye_msg
	syscall 
	li 	$v0,11				#load syscall 11
	li	$t5,0x80000000
	li 	$t2,0
PRINTINGLOOP:
	beq	$t2,32,EXITTWO
	
	add	$t2,$t2,1
EXITTWO:
	li	 $v0, 4
	la	 $a0, newline
	syscall
	li	 $v0, 10 # 10 is the exit syscall.
	syscall 	# do the syscall.
# Data for the program:
.data
hello_msg: .asciiz 	"Welcome to Conversion\nInput Number: "
goodbye_msg: .asciiz 	"\nOutput Number: "
newline:     .asciiz 	"\n"

# end Lab3.asm