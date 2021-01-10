	.file	"cSwap.c"
	.text
.globl cSwap
	.type	cSwap, @function
cSwap:
	pushl	%ebp                 #Push content of ebp onto the program stack   
	movl	%esp, %ebp           #Create new frame pointer
	subl	$16, %esp            #Subtracting 16 from the stack pointer esp allocates that memory for your function's use 
	movl	8(%ebp), %eax        #Move first address (i) at ebp+8 offset and store in eax
	movl	(%eax), %eax         #Move first value (*i) into eax 
	movl	%eax, -4(%ebp)       #Move value (*i) into ebp-4 offset 
	movl	12(%ebp), %eax       #Move second address (j) at ebp+12 offset and store in eax
	movl	(%eax), %edx         #Move first value (*j) into edx 
	movl	%eax, -8(%ebp)       #Move value (*j) into ebp-4 offset 
	movl	8(%ebp), %edx        #Move first value (*i) into (t1) 
	movl	-8(%ebp), %eax
	movl	%eax, (%edx)
	movl	12(%ebp), %edx       #Move first value edx (*j) into (t0) 
	movl	-4(%ebp), %eax
	movl	%eax, (%edx)
	leave                        #Copy the frame pointer to the stack pointer and release the stack space
	ret
	.size	cSwap, .-cSwap
	.ident	"GCC: (Ubuntu 4.3.3-5ubuntu4) 4.3.3"
	.section	.note.GNU-stack,"",@progbits
