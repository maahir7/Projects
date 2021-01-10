/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package driver;
import java.util.*;

/**
 *
 * @author maahir
 */
public class ComputePostfixFormula {
    /*
   * Method for processing a postfix boolean formula. See assignment description for an overview for how to evaluate a postfix formula.
   */
        
       
  public static String processPostfixBooleanFormula( Queue<String> symbolQueue ) throws IllegalArgumentException
  {

    /* Use the following to through an exception when the postfix string is formatted incorrectly */
  //  throw new IllegalArgumentException( "Postfix String is formatted incorrectly" );
         
       Stack<String> stack = new Stack<String>();   
     
       
       while (symbolQueue != null) {
           
            
       String op1 = null,op2 = null;
          
       
          if (symbolQueue.equals("True")||symbolQueue.equals("False")) {
             stack.push(op1);
             stack.push(op2);
          }
          else if (symbolQueue.equals("NOT")){
             stack.pop();
                 if  (op1.equals("true"));
                   stack.push(op1);  
          }
          else if (symbolQueue.equals("AND")){
              stack.pop();
              stack.pop();
             
                if (op1.equals("true") && op2.equals("true"))
                   stack.push(op1);
              }
          else if (symbolQueue.equals("NAND")){
             stack.pop();
             stack.pop();
             if (!((op1.equals("true") && op2.equals("true"))))
                   stack.push(op1); 
              }
          else if (symbolQueue.equals("OR")){
             stack.pop();
             stack.pop();
             if (op1.equals("true") || op2.equals("true"))
                   stack.push(op1); 
              }
          else if (symbolQueue.equals("NOR")){
             stack.pop();
             stack.pop();
             if (!((op1.equals("true") || op2.equals("true"))))
                   stack.push(op1); 
              }
          else if (symbolQueue.equals("XOR")){
             stack.pop();
             stack.pop();
             if (op1.equals("true") != op2.equals("true"))
                   stack.push(op1); 
              }
            else if (symbolQueue.equals("COND")){
             stack.pop();
             stack.pop();
             if (!(op1.equals("true") || op2.equals("true")))
                   stack.push(op1); 
              }
          else if (symbolQueue.equals("BICOND")){
             stack.pop();
             stack.pop();
             if (op1.equals("true") == op2.equals("true"))
                   stack.push(op1); 
             }
       }
       /* Return the top element of the stack after processing the postfix string */
       //return "";
       return stack.pop();
   }
    
  }
    

