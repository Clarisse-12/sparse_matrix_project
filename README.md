Author: Clarisse Mukayiranga
Course: Data Structures and Algorithms for Engineers
Assignment: DSA HW01 - Sparse Matrix
Date: 24 may 2025 Language Used: Python

Project Structure: ├── /dsa/sparse_matrix/code/src/ → Python source code files
│ ├── SparseMatrix.py → Contains the SparseMatrix class and all matrix operations
│ └── main.py → Entry point script that allows user to choose matrix operation
├── /dsa/sparse_matrix/sample_inputs/ → Input matrix files (.txt format)

How to Run
Open a terminal and navigate to the code/src/ folder:

Run the program:

Follow the prompts:

Select the operation: addition, subtraction, or multiplication
Enter the paths to the two matrix input files (e.g., ../../sample_inputs/matrix1.txt and ../../sample_inputs/matrix2.txt)
The result will be printed to the console and optionally saved to a file.
Input File Format
Each input matrix file must follow this format: rows=8433 cols=3180 (0, 381, -694) (0, 128, -838)

First line: number of rows
Second line: number of columns
From the third line onward: non-zero entries in the format (row, col, value)
Lines with extra whitespaces are ignored
Invalid formats (wrong brackets, floating points, etc.) raise a ValueError and stop execution
Features
Efficient sparse matrix representation using dictionaries
Matrix operations: Addition, Subtraction, Multiplication
Caches matrices to avoid re-reading files unnecessarily
Exception handling for invalid dimensions and malformed files
No use of standard Python parsing libraries (e.g., no regex)
Fully custom logic for input parsing and error handling
Notes
Only integer values are supported
Zero entries are not stored in memory (implicit zeros)
All parsing and matrix logic is implemented manually without built-in helpers
Input validation strictly follows assignment rules
Contact
For any questions or issues, please contact [c.mukayiran@alustudent.com].
