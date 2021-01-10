.globl asmMagicSwap
	.type	asmMagicSwap, @function
asmMagicSwap:              # label
    pushl   %ebp
    movl    %esp, %ebp     # stack frame set up
    movl    8(%ebp), %edx  # fetch first parameter (*v1) and store to %edx
    movl    (%edx), %edx   # fetch the value at the address *v1
    addl    $1, %edx       # add 1 immediately to %edx value (v1)
    movl    12(%ebp), %eax # fetch second parameter (v2) and store to %eax
    movl    (%eax), %eax   # fetch the value at the address *v2
    subl    $1, %eax       # subtract 1 immediately from %eax value (v2)
    movl    8(%ebp), %ecx  # fetch &v1 to %ecx
    movl    %eax, (%ecx)   # store %eax (v2-1) directly to memory address pointed by &v1
    movl    12(%ebp), %ecx # fetch &v2 to %ecx
    movl    %edx, (%ecx)   # store %edx (v1+1) directly to &v2
    popl    %ebp           # pop %ebp to restore stack frame
    ret                    # return
