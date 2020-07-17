//declare data
.data

//declare start of text
.text

//allow printintegers to be seen by compilers
.global printinteger

//start defining printintegers
printinteger:
	
	push {r4-r9, lr}	//move lr to stack

	mov r5, r0		//move integer to r5 so that it doesn't mess up
	cmp r1, #0		//see if it's in integers or hex (0 = int, 1 = hex)
	beq integers		//branch to integers if second parameter = 0
	b hex			//branch to hex otherwise

.magic_number: .word 0xcccccccd	//set magic number for division by 10

integers:
	
	cmp r5, #0		//compare with 0 to see things
	beq zero_integer	//if it is zero branch to zero_integer 
	blt negative_integer	//branch to negative_integer if it is < 0 
	bgt positive_integer	//branch to positive_integer otherwise

zero_integer:

	mov r0, #48		//load in ascii for '0'
	bl putchar		//print out 0
	b end			//end program

negative_integer:
	mov r0, #45		//load in ascii for '-'
	bl putchar		//print out -

	mov r6, #-1		//load -1 in r6
	mul r5, r5, r6		//make the number positive

	b positive_integer	//branch to positive number

positive_integer:
	mov r9, #0		//move 0 in r9 (counter)
	mov r6, r5		//make a copy in r6 of the number

	loop_integer:		//loop for magic number 
		ldr r1, .magic_number	//load magic number
		umull r1, r2, r1, r6	//r1 ? Lower32Bits(r1*r6).r2 ? Upper32Bits(r1*r0)
		mov r8, r2, LSR #3	//r8 ? r2 >>3

		mov r7, #10		//move in 10 for multiplication
		MUL r7, r7, r8		//multiply quotient by 10 (stored in r7)
		SUB r7, r6, r7		//remainder = number - quotient*10 (stored in r7)

		ADD r7, r7, #48		//add ascii value of '0' to remainder
		push {r7}		//push the value onto a stack

		mov r6, r8		//move quotient in r6
		ADD r9, r9, #1		//increment counter by 1

		cmp r6, #0		//see if quotient is 0
		beq print		//if quotient == 0, goto print
		b loop_integer		//else loop
	b end				//by some accident if it is here, goto end

hex:
	
	cmp r5,#0		//same logic as integers (but now branch to hex fns)

	beq zero_hex
	blt negative_hex
	bgt positive_hex

	b end

negative_hex:				//branch to positive hex
	b positive_hex			

	NEG r5, r5 //if need to debug 2s complement comment out prev line, otherwise neever gonna reach here
	ADD r5, r5, #1
	b positive_hex

zero_hex:
	b zero_integer	//there was code here but now removed as we don't need to print '0x'


positive_hex:
	mov r6, r5			//make a copy
	mov r9, #0			//set counter

	//mov r0, #48			//uncomment the block for printing '0x'
	//bl putchar
	//mov r0, #120
	//bl putchar

	loop_hex:			//loop
		mov r7, #15		//move 15 (1111 in binary) to r7

		AND r8, r6, r7		//get last 4 bits of number and store in r8 (r8 % 16)
		ADD r8, r8, #48		//add ascii value of '0' to the remainder

		cmp r8, #58		//if number is less than 10
		blt smaller		//go to smaller:

		SUB r8, #58		//subtract 58 to get remainder - 10
		ADD r8, #97		//add ascii value of 'a' to it

		smaller:		
		PUSH {r8}		//push the character onto stack
		LSR r6, #4		//left shift the number by 4 by shifting in 0's
		ADD r9, r9, #1		//increment counter

		cmp r6, #0		//see if number is 0, then goto print else goto loop_hex
		beq print		
		b loop_hex
	b end				//just as safety

print:
	loop_print:
		pop {r0}		//pop from stack into r0
		bl putchar		//branch to putchar

		sub r9, #1		//decrement counter
		cmp r9, #0		//see if counter is 0

		beq end			//if counter = 0, goto end, else goto loop
		b loop_print
	b end


end:
	pop {r4-r9,pc}			//end execution
