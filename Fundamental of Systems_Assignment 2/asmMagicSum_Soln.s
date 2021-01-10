.globl asmMagicSum
	.type	asmMagicSum, @function
asmMagicSum:               # label, makes it avialabe to asmAssign2
    pushl   %ebp
    movl    %esp, %ebp     # stack frame set up
    movl    8(%ebp), %edx  # fetch first parameter (v1) and store to %edx
    imull   $2, %edx, %edx # multiply 2 to value in %edx (v1) and store in %edx
    movl    12(%ebp), %eax # fetch second parameter (v2) and store to %eax
    sarl    $1, %eax       # arithmetic right shift %eax by 1 to divide by 2
    addl    %edx, %eax     # add values stored in %edx and %eax, store in %eax
    popl    %ebp           # pop %ebp
    ret                    # return
