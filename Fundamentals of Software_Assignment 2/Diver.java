import java.io.*;
import java.util.*;

public class Driver 
{
  public static void main(String[] args) throws FileNotFoundException 
  {
    Queue<String> symbolQueue = new LinkedList<String>();
    
    File myFile = new File("postfixTestData.txt");
    Scanner myReader = new Scanner(myFile);
    
    //Read boolean formulas from file and check whether student algorithm returns the correct result 
    while (myReader.hasNextLine()) {
      String expectedResult = myReader.nextLine();
      String booleanFormula = myReader.nextLine();
      String tokens[] = booleanFormula.split(" ");
      
      symbolQueue.clear();
      for( String token : tokens )
        symbolQueue.add( token );
      
      String computedResult;
      System.out.println("Testing boolean formula: " + booleanFormula);
      try {
        computedResult = ComputePostfixFormula.processPostfixBooleanFormula( symbolQueue );  
        if( expectedResult.equals(computedResult) ){
          System.out.println("Your algorithms correctly returned: " + expectedResult);
          System.out.println("");
        }
        else{
          System.out.println("The correct result is: " + expectedResult + "\nBut your algorithm returned: " + computedResult);
          System.out.println("");
        }
      }
      catch(IllegalArgumentException e) {
        if( expectedResult.equals("error") ){
          System.out.println("Your algorithms correctly returned: error");
          System.out.println("");
        }
        else{
          System.out.println("The correct result is: " + expectedResult + "\nBut your algorithm returned: error");
          System.out.println("");
        }
      }
      
    }
    myReader.close();
    
  }
}