	.file	"dot_product.c"
	.text
	.globl	dot_product
	.type	dot_product, @function
dot_product:
.LFB264:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$252, %esp
	xorps	%xmm0, %xmm0
	movaps	%xmm0, -216(%ebp)
	movl	$0, -232(%ebp)
	jmp	.L3
.L9:
	movl	-232(%ebp), %eax
	leal	0(,%eax,4), %edx
	movl	8(%ebp), %eax
	addl	%edx, %eax
	movl	%eax, -228(%ebp)
	movl	-228(%ebp), %eax
	movaps	(%eax), %xmm0
	movaps	%xmm0, -200(%ebp)
	movl	-232(%ebp), %eax
	leal	0(,%eax,4), %edx
	movl	12(%ebp), %eax
	addl	%edx, %eax
	movl	%eax, -224(%ebp)
	movl	-224(%ebp), %eax
	movaps	(%eax), %xmm0
	movaps	%xmm0, -184(%ebp)
	movaps	-200(%ebp), %xmm0
	movaps	%xmm0, -152(%ebp)
	movaps	-184(%ebp), %xmm0
	movaps	%xmm0, -136(%ebp)
	movaps	-136(%ebp), %xmm0
	movaps	-152(%ebp), %xmm1
	mulps	%xmm1, %xmm0
	movaps	%xmm0, -168(%ebp)
	movaps	-168(%ebp), %xmm0
	movaps	%xmm0, -120(%ebp)
	movaps	-168(%ebp), %xmm0
	movaps	%xmm0, -104(%ebp)
	movaps	-104(%ebp), %xmm0
	movaps	-120(%ebp), %xmm1
	addps	%xmm1, %xmm0
	movaps	%xmm0, -168(%ebp)
	movaps	-216(%ebp), %xmm0
	movaps	%xmm0, -88(%ebp)
	movaps	-168(%ebp), %xmm0
	movaps	%xmm0, -72(%ebp)
	movaps	-72(%ebp), %xmm0
	movaps	-88(%ebp), %xmm1
	addps	%xmm1, %xmm0
	movaps	%xmm0, -216(%ebp)
	addl	$4, -232(%ebp)
.L3:
	cmpl	$199, -232(%ebp)
	jle	.L9
	movaps	-216(%ebp), %xmm0
	movaps	%xmm0, -56(%ebp)
	movaps	-216(%ebp), %xmm0
	movaps	%xmm0, -40(%ebp)
	movaps	-40(%ebp), %xmm0
	movaps	-56(%ebp), %xmm1
	addps	%xmm1, %xmm0
	movaps	%xmm0, -216(%ebp)
	leal	-236(%ebp), %eax
	movl	%eax, -220(%ebp)
	movaps	-216(%ebp), %xmm0
	movaps	%xmm0, -24(%ebp)
	movaps	-24(%ebp), %xmm0
	movaps	%xmm0, %xmm0
	movl	-220(%ebp), %eax
	movss	%xmm0, (%eax)
	movl	-236(%ebp), %eax
	movl	%eax, -252(%ebp)
	flds	-252(%ebp)
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE264:
	.size	dot_product, .-dot_product
	.ident	"GCC: (Ubuntu 4.8.4-2ubuntu1~14.04.4) 4.8.4"
	.section	.note.GNU-stack,"",@progbits
