/*
Author: Maahir Kalban
Assignment Number: Assignment 1 
File Name: MaahirKalbanAssignment1
Course/Section: CS 5463-002
Due Date: 09/10/2020
Instructor: Jessica Sherette
*/

import java.io.*;
import java.util.Random;


public class MysteryRuntime 
{
  public static final String DATA_FILE_NAME = "TestData.txt";
  public static void main(String[] args) throws IOException 
  {
    functionRuntimes fRT;
    int[] sizes1= { 1000, 2000, 4000, 8000, 16000};
    int[] sizes2= { 5000, 10000, 20000, 40000};
    
    fRT = timeAlgorithm("Insertion Sort", 10, 5, sizes1, new ArrayAlgs("insertionSortInitial") ); //unprinted run
    
    fRT = timeAlgorithm("Insertion Sort", 10, 5, sizes1, new ArrayAlgs("insertionSortInitial") );
    printRuntimeTable(fRT);
    
    fRT = timeAlgorithm("quicksort (uses insertion sort when sorting <30 numbers)", 10, 5, sizes1, new ArrayAlgs("quickSortOptInitial") );
    printRuntimeTable(fRT);
    
    fRT = timeAlgorithm("Mystery 1", 8, 4, sizes2, new ArrayAlgs("mysteryRuntime1") );
    printRuntimeTable(fRT);
    
    fRT = timeAlgorithm("Mystery 2", 8, 4, sizes2, new ArrayAlgs("mysteryRuntime2") );
    printRuntimeTable(fRT);
    
    fRT = timeAlgorithm("Mystery 3", 8, 4, sizes2, new ArrayAlgs("mysteryRuntime3") );
    printRuntimeTable(fRT);
    
  }
  
  /* TO BE COMPLETED BY YOU
   * Fill in the missing parts of the code (see TODOs below)
   */
  
  public static functionRuntimes timeAlgorithm(String name, int numRepeats, int numTestCaseSizes, int[] testCaseSizes, ArrayAlgs sortingAlgorithm) throws IOException
  {
    /* Call and calculate the runtime of the provided function */
    long start = 0, end = 0;
    int i, j;
    File testData;
    
    // create functionRuntimes variable to return
    functionRuntimes fRT = new functionRuntimes();
    
    // TODO: copy passed data into the functionRuntimes variable
    /* fill name in fRT with the variable name */
    fRT.name = name;
    /* fill numRepeats in fRT with the variable numRepeats */
    fRT.numRepeats = numRepeats;
    /* fill numTestCaseSizes in fRT with the variable numTestCaseSizes */
    fRT.numTestCaseSizes = numTestCaseSizes;
    /* set testCaseSizes in fRT to hold numTestCaseSizes number of ints */
    fRT.testCaseSizes = new int[numTestCaseSizes];
    /* fill testCaseSizes in fRT with the variable testCaseSizes (hint: use a loop) */
    for(i = 0; i < numTestCaseSizes; i++)
    {
        fRT.testCaseSizes[i] = testCaseSizes[i];
    }
    // TODO: set fRT.runtimes to a new double 2D array of with numTestCaseSizes rows and numRepeats columns
        /* fRT.runtimes = */
    fRT.runtimes = new double[numTestCaseSizes][numRepeats] ; 
    for(i = 0; i < numTestCaseSizes; i++)
    {
    fRT.runtimes[i] = new double[numRepeats];
      for(j = 0; j < numRepeats; j++)
      {
        //Generate test data for the function f
        testData = generateTestInput(0, testCaseSizes[i], testCaseSizes[i]);
        
        //Run f on the generated test data
        start = System.currentTimeMillis();
        sortingAlgorithm.executeAlg(testData);
        end = System.currentTimeMillis();
        
        //Enter the elapsed number of seconds into the arrRuntimes array for fRT
        
        //TODO: uncomment the next line line after you've set a value for fRT.runtimes
        fRT.runtimes[i][j] = (double)(end - start) / 1000;
      }
    }
     //TODO: Calculate the average runtimes (create space for fRT.avg and call computeAvg here)
    fRT.avg = new double [numTestCaseSizes];
    computeAvg(fRT);
    return fRT;      
  }
  
  /*
   * Provided code - DO NOT CHANGE THIS METHOD 
   */ 
  public static File generateTestInput(int min, int max, int size) throws IOException
  {
    int i;
    File data = new File(DATA_FILE_NAME);
    data.createNewFile();
    //try (FileWriter writer = new FileWriter(data)) {
      FileWriter writer = new FileWriter(data);
      writer.write(String.valueOf(size));
      writer.write(" ");
      for (i = 0; i < size; i++)
      {
        Random rand = new Random();
        writer.write(String.valueOf(rand.nextInt(max - min + 1) + min));
        writer.write(" ");
      }
      writer.flush();
      writer.close();
    //}
    return data;
  }
  
  /* TODO: TO BE COMPLETED BY YOU
   * Calculate and insert the average runtime for each set of test data into fRT
   */
  public static void computeAvg(functionRuntimes fRT)
  {
int i, j;
    double averageTimes;

    for(i = 0; i < fRT.numTestCaseSizes; i++)
    {
        averageTimes = 0.0;
        for(j = 0; j < fRT.numRepeats; j++)
        {
            averageTimes += fRT.runtimes[i][j];
        }
        averageTimes /= fRT.numRepeats;

        fRT.avg[i] = averageTimes;
    }
  }
  
  /* TODO: TO BE COMPLETED BY YOU
   * Print the information in fRT as a 2d table. Display 3 digits after the decimal point. You can assume all of the runtimes are <= 99.999 seconds. 
   */
  public static void printRuntimeTable(functionRuntimes fRT)
  {
int i, j;
    int testNumber = 0;
    String tableHeader= "Test Size";

    System.out.println(fRT.name);
    System.out.format( "%-12s",tableHeader);
    for(i = 0; i < fRT.numRepeats; i++)
    {
        System.out.format("Test #%-4d",testNumber++);
    }
    System.out.println("Average");

    for(i = 0; i < fRT.numTestCaseSizes; i++)
    {
        System.out.format("%-12d", fRT.testCaseSizes[i]);
        for(j = 0; j < fRT.numRepeats; j++)
        {
            System.out.format("%-10.3f",fRT.runtimes[i][j]);
        }
        System.out.format("%.3f\n", fRT.avg[i]);
    }
    System.out.format("\n");
  }
}