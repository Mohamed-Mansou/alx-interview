#!/usr/bin/python3
"""
Solution to the nqueens problem
"""
import sys

def is_valid(board, row, col):
   """Checks if placing a queen at (row, col) is valid."""
   for i in range(row):
       if board[i] == col or abs(row - i) == abs(board[i] - col):
           return False
   return True

def solve_n_queens(board, row, n):
   """Recursively solves the N queens problem."""
   if row == n:
       print(" ".join(str(x + 1) for x in board))  # Print solution in required format
       return

   for col in range(n):
       if is_valid(board, row, col):
           board[row] = col
           solve_n_queens(board, row + 1, n)

def main():
   if len(sys.argv) != 2:
       print("Usage: nqueens N", file=sys.stderr)
       sys.exit(1)

   try:
       n = int(sys.argv[1])
   except ValueError:
       print("N must be a number", file=sys.stderr)
       sys.exit(1)

   if n < 4:
       print("N must be at least 4", file=sys.stderr)
       sys.exit(1)

   board = [-1] * n  # Initialize board with -1 to indicate empty positions
   solve_n_queens(board, 0, n)

if __name__ == "__main__":
   main()
