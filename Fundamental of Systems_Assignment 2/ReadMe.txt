To Zip Tar File

> tar -zcvf Kalban-Maahir-ert547-assignment02.tar.gz ./Kalban-Maahir-ert547-assignment02

To Unzip Tarr File

> tar -xzvf Kalban-Maahir-ert547-assignment02.tar.gz

PART 1
-Code Status: Program works as required.
-Could not determine some movl instructions.
- To convert code to Assembley code

> gcc -m32 -c -S cSum.c
> gcc -m32 -c -S cSwap.c  

PART 2 
-Code Status: Program works as required.
-Could not determine some movl and sarl instructions
- To compile the two functions separateley and execute the program

> gcc -c asmMagicSum.s -o asmMagicSum.o
> gcc -c asmMagicSwap.s -o asmMagicSwap.o
> gcc -c asmAssign2.c -o asmAssign2.o
> gcc asmAssign2.o asmMagicSum.o asmMagicSwap.o -o asmAssign2
> ./ asmAssign2

- Result: 
Before Swap. a: 1, b: 10
After Swap of modified values. a: 9, b: 2

Numbers to sum are: 5 and 6
Sum of num1*2 + num2/2 is: 13
