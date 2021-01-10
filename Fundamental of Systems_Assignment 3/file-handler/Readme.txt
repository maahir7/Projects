-Status of program is that it works as required with the child processor. 
-Ecxept Parent processor doesnt work
-Did not have a total number of words or number of different words counter.
   
	
To extract and unzip use comand

	tar -xzvf assign3-ert547.tar.gz

To Run Program:

gcc -Wall -g -std=c99 -Werror file-handler.c wordsProcessorLL.c wordsProcessorLL.h -o file-handler

./file-handler file-1.txt file-2.txt file-3.txt



	
Then the output will be in a output.txt.