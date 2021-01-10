/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//package driver;

/**
 *
 * @author Maahir Kalban
 */
public class GraphAlgorithms {
    /* returns -1 if path not found from S to F and 1 if a path is found */
  public static int hasPath( char maze[][], int size ) {
         // Defining visited array to keep
        // track of already visited indexes
        boolean visited[][] = new boolean[size][size];
 
        // Flag to indicate whether the
        // path exists or not
       // boolean flag = false;
 
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                // if matrix[i][j] is source
                // and it is not visited
                if (maze[i][j] == 1 && !visited[i][j])
 
                    // Starting from i, j and
                    // then finding the path
                    if (hasPath(maze, i, j, visited)) {
                        // if path exists
                        return 1;
//                        flag = true;
//                        break;
                    }
            }   
        }
    return 0; /* Default value to signal it has not been completed yet*/
  }
  
  /* returns -1 if path not found from S to any F */
  /* otherwise returns distance to nearest F starting from S */
  public static int findNearestFinish( char maze[][], int size ) {
      
    return 0; /* Default value to signal it has not been completed yet*/
  }
  
  /* returns -1 if path not found from S to F */
  /* otherwise returns distance of longest simple (i.e. not self intersecting) path to F starting from S */
  public static int findLongestSimplePath( char maze[][], int size ) {
    return 0; /* Default value to signal it has not been completed yet*/
  }
     public static boolean hasPath(char maze[][], int i, int j, boolean visited[][])
    {
 
        // Checking the boundries, walls and
        // whether the cell is unvisited
        if (isSafe(i, j, maze) && maze[i][j] != 0 && !visited[i][j]) {
            // Make the cell visited
            visited[i][j] = true;
 
            // if the cell is the required
            // destination then return true
            if (maze[i][j] == 2)
                return true;
 
            // traverse up
            boolean up = hasPath(maze, i - 1, j, visited);
 
            // if path is found in up
            // direction return true
            if (up)
                return true;
 
            // traverse left
            boolean left
                = hasPath(maze, i, j - 1, visited);
 
            // if path is found in left
            // direction return true
            if (left)
                return true;
 
            // traverse down
            boolean down = hasPath(maze, i + 1, j, visited);
 
            // if path is found in down
            // direction return true
            if (down)
                return true;
 
            // traverse right
            boolean right
                = hasPath(maze, i, j + 1, visited);
 
            // if path is found in right
            // direction return true
            if (right)
                return true;
        }
        // no path has been found
        return false;
    }
      // Method for checking boundries
    public static boolean isSafe(int i, int j, char maze[][])
    {
 
        if (i >= 0 && i < maze.length && j >= 0 && j < maze[0].length)
            return true;
        return false;
    }
}
