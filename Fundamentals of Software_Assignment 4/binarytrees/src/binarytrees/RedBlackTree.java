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
        RedBlackNode<T> node = x;
        RedBlackNode<T> parent = (RedBlackNode<T>) node.getParent();
        RedBlackNode<T> uncle = (RedBlackNode<T>) node.getSibling();
        RedBlackNode<T> lchild = (RedBlackNode<T>) node.getLeft();
        RedBlackNode<T> rchild = (RedBlackNode<T>) node.getRight();

        if (parent == null) {
            // Case 1 - The current node is at the root of the tree.
            node.color = Color.BLACK;
            return;
        }

        if (parent.color == Color.BLACK) {
            // Case 2 - The current node's parent is black, so property 4 (both
            // children of every red node are black) is not invalidated.
            return;
        }
        if (lchild != null && parent.color == Color.RED && lchild.color == Color.RED) {
            // Case 3 - If both the parent and the uncle are red, then both of
            // them can be repainted black and the grandparent becomes
            // red (to maintain property 5 (all paths from any given node to its
            // leaf nodes contain the same number of black nodes)).
            parent.color = Color.BLACK;
            lchild.color = Color.RED;
            return;
        }
         if (rchild != null && parent.color == Color.RED && rchild.color == Color.RED) {
            // Case 3 - If both the parent and the uncle are red, then both of
            // them can be repainted black and the grandparent becomes
            // red (to maintain property 5 (all paths from any given node to its
            // leaf nodes contain the same number of black nodes)).
            //rightRotate(parent);
            parent.color = Color.BLACK;
            rchild.color = Color.RED;
            
            return;
        }
       // RedBlackNode<T> grandParent = node.getParent();
        
        if (uncle != null && parent.color == Color.RED && uncle.color == Color.RED) {
            // Case 3 - If both the parent and the uncle are red, then both of
            // them can be repainted black and the grandparent becomes
            // red (to maintain property 5 (all paths from any given node to its
            // leaf nodes contain the same number of black nodes)).
            parent.color = Color.BLACK;
            uncle.color = Color.BLACK;
            if (parent != null) {
                parent.color = Color.RED;
                rebalanceTree(parent);
            }
            return;
        }

        if (uncle != null && parent.color == Color.RED && uncle.color == Color.BLACK) {
            // Case 4 - The parent is red but the uncle is black; also, the
            // current node is the right child of parent, and parent in turn
            // is the left child of its parent grandparent.
            if (node == parent.getRight() && parent == parent.getLeft()) {
                // right-left
                leftRotate(parent);
 
                node = (RedBlackNode<T>) node.getLeft();
                parent = (RedBlackNode<T>) node.getParent();
                parent = node.getParent();
                uncle = node.getSibling();
            } else if (node == parent.getLeft() && parent == parent.getRight()) {
                // left-right
                rightRotate(parent);

                node = (RedBlackNode<T>) node.getRight();
                parent = (RedBlackNode<T>) node.getParent();
                parent = node.getParent();
                uncle = node.getSibling();
            }
        }

        if (uncle != null && parent.color == Color.RED && uncle.color == Color.BLACK) {
            // Case 5 - The parent is red but the uncle is black, the
            // current node is the left child of parent, and parent is the
            // left child of its parent G.
            parent.color = Color.BLACK;
            parent.color = Color.RED;
            if (node == parent.getLeft() && parent == parent.getLeft()) {
                // left-left
                rightRotate(parent);
            } else if (node == parent.getRight() && parent == parent.getRight()) {
                // right-right
                leftRotate(parent);
            }
        }
  }
  
  
  /* Prints the tree starting at the root of this tree. */
  public void drawTree( ){
    RedBlackNode<T> root = this.getRoot();
    root.drawTree( 0 );
  } 
  
}