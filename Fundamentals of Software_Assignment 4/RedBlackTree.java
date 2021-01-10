package binarytrees;

public class RedBlackTree<T extends Comparable<T>> extends Tree {
  
  /* creates a new empty Tree and returns a pointer to it */
  public RedBlackTree()
  {
    //Set the root to NULL using constructor of Tree
    super();
  }
  
   /* Returns the root node of this tree */
   @SuppressWarnings("unchecked") //Suppresses warning for this cast
  public RedBlackNode<T> getRoot()
  {
    return (RedBlackNode<T>)this.root;
  }
  
  /* Stores the passed String in the Tree */
  public void insertRedBlack( T info )
  {
    boolean flag = true;
    RedBlackNode<T> current = this.getRoot();
    RedBlackNode<T> newNode = new RedBlackNode<T>( info );
    
    if(current == null)
    {
      this.setRoot( newNode );
      flag = false;
    }
    
    // find the location to insert at
    while(flag)
    {
      if( newNode.compareTo( current )==0 )
      {
        return; // ignore insertion of duplicates
      }
      else if( newNode.compareTo( current )<0 )
      {
        if( current.getLeft() == null)
        {
          current.setLeft( newNode );
          flag = false;
        }
        else // still not at bottom of tree
        {
          current = current.getLeft();
        }
      }
      else
      {
        if (current.getRight() == null)
        {
          current.setRight( newNode );
          flag = false;
        }
        else // still not at bottom of tree
        {
          current = current.getRight();
        }
      }
    }
    rebalanceTree( newNode );
  }
  
  /* Checks if this Tree is correctly formatted.  Prints when errors occur. */
  public void checkRedBlackTree( ){
    /*int blackHeight =*/ this.getRoot().checkRedBlackStructure( );
    
    if( this.getRoot().color == Color.RED )
      System.out.println( "ERROR - root node is RED" );
  }
  
  /* TODO
   * rebalanceTree
   * input: node to start fixing the tree from (climbing up towards the root)
   * output: none
   * 
   * Modifies the tree to ensure it follows the 5 rules of red-black trees
   */
  
  
  void rebalanceTree( RedBlackNode<T> x )
  {
    
    RedBlackNode<T> p = x.getParent();

/* Check if x is the root and recolor it if it's RED */ 

if( p == null && x.color == Color.RED) {
x.color = Color.BLACK;

return;

}

// loop that rebalances up the tree until you reach the root

while ( p != null )
{
RedBlackNode<T> gp = p.getParent();
RedBlackNode<T> pibling = p.getSibling();

/* Check if parent is the root and recolor it if it's RED*/

if( gp == null && p.color = Color. RED ) { 
p.color = Color.BLACK; I
return;

}

// check if error still exists

if ( x.color == Color.RED && p.color == Color.RED )
{
 //case 1 - recolor parent and pibling node

if( pibling!=null && pibling.color == Color.RED )
{ 
pibling.color = Color.BLACK;
p.color - Color BLACK;
gp.color = color.RED;
}

//case 2 6 3 - fix the zigzag/straight cases

else{

if ( p.getLeft() == x & gp.getRight() == p ) {
super.rightRotate( p );
P = x;

else if( p.getRight() == x && gp.getLeft () == p ) {
super. leftRotate(p);
p = x;
}


if (gp.getLeft() == p )(

super.rightRotate ( gp);
gp.color = Color.RED:
p.color = Color.BLACK;
}
return;
}
}
x = p;
p = gp;
}
}
  
  
  /* Prints the tree starting at the root of this tree. */
  public void drawTree( ){
    RedBlackNode<T> root = this.getRoot();
    root.drawTree( 0 );
  } 
  
}