# A Quick Study of Algorithmic Sudoku Solving
## Solving Sudoku - the Brute Force Approach
## Solving Sudoku with Stochastic Search
>The implementation here is in Python, using a beam search algorithm, which uses a heuristic for a best fit search but with a limited agenda size.

### Heuristic
The heuristic used is the number of collisions, a check for uniqueness within the row, the column, and the associated nxn subgrid for each cell in the sudoku grid

### Search Space
* **S** - The states are sets of filled configurations of the board
* **S0** - The initial state consists of 10 initial randomized configurations where the cells are randomized around the fixed cells that had already been given values in the original problem.
* **T** - The transitions are made with value swaps between nonfixed cells. To keep the constraint of unique values within a row (each row must have exactly 1 instance of 1, 2, 3, 4, etc), random swaps are done within the same row
* **F** - The goal states are states where at least one of the boards in the board set of the state has a heuristic value of 0 (no collisions)

### Algorithm
There is a boards agenda that initially has the boards of the initial state

Then, as long as the puzzle isn't solved (there are no built boards with 0 collisions), the following steps are taken:
1. The boards agenda is sorted in ascending order based on heuristic value
2. The boards agenda is truncated to the 10 boards with the lowest heuristic (the first 10 boards in the sorted agenda)
3. The first board in the agenda is checked

  * If the heuristic of this board is 0:
      This is a goal state, this board configuration is set as the solution and this board is returned
  * Otherwise:
      The next generation of boards are generated and added to the agenda. In this case, 4 successor boards are generated per board in the current generation
4. Loop!
