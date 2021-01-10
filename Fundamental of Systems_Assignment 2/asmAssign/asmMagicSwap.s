        .file   "asmMagicSwap.c"
        .text
.globl magicSwap
        .type   magicSwap, @function
magicSwap:
        pushl   %ebp                  #Push content of ebp onto the program stack     
        movl    %esp, %ebp            #Create new frame pointer
        subl    $16, %esp             #Subtracting 16 from the stack pointer esp allocates that memory for your function's use 
        movl    8(%ebp), %eax         #Move first address (p1) at ebp+8 offset and store in eax
        movl    (%eax), %eax          #Move first value (*p1) into eax 
        addl    $1, %eax              #add 1 + eax (value (*p1))
        movl    %eax, -4(%ebp)        #move eax to ebp - 4 offset 
        movl    12(%ebp), %eax        #Move second address (p2) at ebp+12 offset and store in eax 
        movl    (%eax), %eax          #Move first value (*p2) into eax 
        subl    $1, %eax              #subtract 1 + eax (value (*p2)) 
        movl    %eax, -8(%ebp)        #move eax to ebp - 8 offset 
        movl    8(%ebp), %edx         #Move value t1 to first address into (*p1) 
        movl    -8(%ebp), %eax
        movl    %eax, (%edx)
        movl    12(%ebp), %edx        #Move value t0 to first address into (*p2) 
        movl    -4(%ebp), %eax
        movl    %eax, (%edx)
        leave
        ret
        .size   magicSwap, .-magicSwap
        .ident  "GCC: (Ubuntu 4.3.3-5ubuntu4) 4.3.3"
        .section        .note.GNU-stack,"",@progbits
