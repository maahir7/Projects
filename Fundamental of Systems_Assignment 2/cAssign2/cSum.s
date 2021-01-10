	.file	"cSum.c"
	.text
.globl cSum
	.type	cSum, @function
cSum:
	pushl	%ebp                  #Push content of ebp onto the program stack
	movl	%esp, %ebp			  #Create new frame pointer	
	subl	$16, %esp             #Subtracting 16 from the stack pointer esp allocates that memory for your function's use
	movl	12(%ebp), %edx        #Retrieve n at ebp+12 offset and store in edx
	movl	8(%ebp), %eax         #Retrieve m at ebp+8 offset and store in eax 
	addl	%edx, %eax            #Add m and n and store in eax 
	movl	%eax, -4(%ebp)        #Retrieve eax and store in ebp-4 offset 
	movl	-4(%ebp), %eax        #Retrieve ebp and store in eax-4 offset 
	leave                         #Copy the frame pointer to the stack pointer and release the stack space
	ret                           #Return t stored in eax
	.size	cSum, .-cSum
	.ident	"GCC: (Ubuntu 4.3.3-5ubuntu4) 4.3.3"
	.section	.note.GNU-stack,"",@progbits
