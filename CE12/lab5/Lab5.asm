#Zachary Plante (zplante)
#CS 12 Lab 5
#Takes in a Key and Phrase and encodes the phrase using the key and a cypher
#Some code based on code from Lab 3, written by myself, 
#mostly concerning reading in program arguments and looing through strings
.text
#prints and calls funtions
main:
	lw	$s0,0($a1)
	lw	$s1,4($a1)
	la	$s2,encoded
	la	$s3,decoded
	li	$v0,4
	la	$a0,givK
	syscall
	la	$a0,($s0)
	la	$a1,($s0)
	syscall
	la	$a0,givT
	syscall
	la	$a0,($s1)
	la	$a2,($s1)
	syscall
	jal	ENCODE
	la	$a0,enT
	syscall
	la	$a0,encoded
	la	$a2,encoded
	syscall
	jal	DECODE
	la	$a0,deT
	syscall
	la	$a0,decoded
	syscall
	j FULLEXIT
	
#Encoding Function	
ENCODE:
	li $t0,0
	li $t1,0
	li $t5,128
ENCODELOOP:
	add $t2,$a1,$t0
	add $t3,$a2,$t1
	lb $t2,($t2)
	lb $t3, ($t3)
	beq $t3,$zero,EXITENCODE
	bne $t2,$zero,KEYSAFEE
	li $t0,0
	add $t2,$a1,$t0
	lb $t2, ($t2)
KEYSAFEE:
	add $t4,$t2,$t3
	div $t4,$t5
	mfhi $t4
	sb $t4,($s2)
	addi $s2,$s2,1
	add $t0,$t0,1
	add $t1,$t1,1
	j ENCODELOOP
EXITENCODE:
	sb $zero,($s2)
	jr $ra

#Decodeing function
DECODE:
	li $t0,0
	li $t1,0
DECODELOOP:
	add $t2,$a1,$t0
	add $t3,$a2,$t1
	lb $t2,($t2)
	lb $t3, ($t3)
	beq $t3,$zero,EXITDECODE
	bne $t2,$zero,KEYSAFED
	li $t0,0
	add $t2,$a1,$t0
	lb $t2, ($t2)
KEYSAFED:
	bge  $t3,$t2,LENGTHSAFE
	addi $t3,$t3,128
LENGTHSAFE:
	sub $t3,$t3,$t2
	sb $t3,($s3)
	addi $s3,$s3,1
	add $t0,$t0,1
	add $t1,$t1,1
	j DECODELOOP
EXITDECODE:
	sb $zero,($s3)
	jr $ra
FULLEXIT:
	li	 $v0, 10 # 10 is the exit syscall.
	syscall 	# do the syscall.
.data
encoded: .space 101
decoded: .space 101
givT: .asciiz "\nThe given text is: "
givK: .asciiz "The given key is: "
enT: .asciiz "\nThe encrypted text is: "
deT: .asciiz "\nThe decrypted text is: "
