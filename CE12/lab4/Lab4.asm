.text 
main:
#t0 is n, t1 is index, t2 is divider, t3 is n/2, t4 is remander
	li $v0,5
	syscall		#asks for input
	move $t0,$v0
	blt $t0,2,BIGEXIT
	nop
	li $v0,1
	li $t1,2
	move $a0,$t1	
	syscall	#prints 2 first for formating reasons	
	move $t1,$a0 
	div $t3,$t0,2 #sets n/2
	blt $t0,3,BIGEXIT
	nop
	addi $t1,$t1,1
	
BIGLOOP:			#loop of all numbers smaller than n
	bgt  $t1,$t0,BIGEXIT
	nop
	
	li $t2,2	#sets dividing number for loop
LITTLELOOP:
	bgt $t2,$t3,LITTLEEXITP	#exits if dividing number is larger than n/2 or the index
	nop
	bge $t2,$t1,LITTLEEXITP
	nop
	div $t1,$t2
	mfhi $t4
	beqz $t4,LITTLEEXIT #exits if number is not prime
	nop
	addi $t2,$t2,1
	b LITTLELOOP
	nop
LITTLEEXITP:			#prints prime
	la $a0,comma
	li $v0,4
	syscall
	move $a0,$t1
	li $v0,1
	syscall
	move $t1,$a0
LITTLEEXIT:
	addi $t1,$t1,1
	b BIGLOOP 
BIGEXIT: 
	li	 $v0, 10 # 10 is the exit syscall.
	syscall 	# do the syscall.
	
.data
comma: .asciiz ", "
