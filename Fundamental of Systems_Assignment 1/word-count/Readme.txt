a) -Status of program is that it works as required. 
   -Ecxept that there is an extra character counted as a word. Unable to debug at the moment.
   -Did not have a total number of words or number of different words counter.
   
b) - Main Program did not call (countWordsWithLinkedList( ) function. Instead implementaion is in main method.

	-User-defined header  (wordsProcessorLL.h), and the actual implementation of the function wordsProcessorLL.c was created.
	
c) Linked List was used in the following struct to store the words:

typedef struct s_words {
    char *str;                  //word
    int count;                  //number of times word occurs
    struct s_words *next;       //pointer to next word
} words;

d) No help was given from classmates

e) To improve my code i would debug the reason why the special character "\n" was counted as a word.

To extract and unzip use comand

	tar -xzvf assign1-ert547.tar.gz

To Run Program use comand "make" in the ert-547 directory.

	
Then the output will be in a assign-01-test-output.txt.