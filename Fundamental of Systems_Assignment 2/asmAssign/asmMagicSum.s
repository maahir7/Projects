	.file	"asmMagicSum.c"
	.text
.globl magicSum
	.type	magicSum, @function
magicSum:
	pushl	%ebp                     #Push content of ebp onto the program stack
	movl	%esp, %ebp               #Create new frame pointer
	movl	8(%ebp), %eax            #Retrieve v1 at ebp+8 offset and store in eax
	leal	(%eax,%eax), %ecx        #ecx = eax + eax 
	movl	12(%ebp), %edx           #Retrieve v2 at ebp+12 offset and store in edx
	movl	%edx, %eax               #Move edx to eax
	shrl	$31, %eax                #Shifting %eax right 31 bits
	addl	%edx, %eax               #Add (2*v1 + v2/2) and store in eax 
	sarl	%eax
	leal	(%ecx,%eax), %eax        #eax = ecx + eax  
	popl	%ebp                     #restore %ebp
	ret
	.size	magicSum, .-magicSum
	.ident	"GCC: (Ubuntu 4.3.3-5ubuntu4) 4.3.3"
	.section	.note.GNU-stack,"",@progbits
