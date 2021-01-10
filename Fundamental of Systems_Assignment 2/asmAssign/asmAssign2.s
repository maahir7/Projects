	.file	"asmAssign2.c"
	.section	.rodata
.LC0:
	.string	"Before Swap. a: %d, b: %d\n"
	.align 4
.LC1:
	.string	"After Swap of modified values. a: %d, b: %d\n\n"
	.align 4
.LC2:
	.string	"Numbers to sum are: %d and %d\n"
	.align 4
.LC3:
	.string	"Sum of num1*2 + num2/2 is: %d\n"
	.text
.globl main
	.type	main, @function
main:
	leal	4(%esp), %ecx
	andl	$-16, %esp
	pushl	-4(%ecx)
	pushl	%ebp
	movl	%esp, %ebp
	pushl	%ecx
	subl	$52, %esp
	movl	$1, -8(%ebp)
	movl	$10, -12(%ebp)
	movl	$5, -16(%ebp)
	movl	$6, -20(%ebp)
	movl	-12(%ebp), %eax
	movl	-8(%ebp), %edx
	movl	%eax, 8(%esp)
	movl	%edx, 4(%esp)
	movl	$.LC0, (%esp)
	call	printf
	leal	-12(%ebp), %eax
	movl	%eax, 4(%esp)
	leal	-8(%ebp), %eax
	movl	%eax, (%esp)
	call	magicSwap
	movl	-12(%ebp), %eax
	movl	-8(%ebp), %edx
	movl	%eax, 8(%esp)
	movl	%edx, 4(%esp)
	movl	$.LC1, (%esp)
	call	printf
	movl	-20(%ebp), %eax
	movl	%eax, 8(%esp)
	movl	-16(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$.LC2, (%esp)
	call	printf
	movl	-20(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	-16(%ebp), %eax
	movl	%eax, (%esp)
	call	magicSum
	movl	%eax, -24(%ebp)
	movl	-24(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$.LC3, (%esp)
	call	printf
	movl	$0, %eax
	addl	$52, %esp
	popl	%ecx
	popl	%ebp
	leal	-4(%ecx), %esp
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu 4.3.3-5ubuntu4) 4.3.3"
	.section	.note.GNU-stack,"",@progbits
