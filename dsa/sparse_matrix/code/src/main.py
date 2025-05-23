from sparse_matrix import Sparsematrix

def main():

    """
    main functionof performing operation on sparse matrices.

    this funtion help user to :
    -select opertion of matrix like addition, subtraction, and multiplication.
    -provide file where the two sparse matrices locate and formated correctly.
    and then after it load matrices from file provided and perform the choosen operation and display the results in sparse format.


    matrix format look like this:
    rows=numbers
    cols=numbers
    (row, col, value)
    """
    print("==sparsematrix operation==")
    print("choose operation you want:")
    print("1, addition")
    print("2, subtraction")
    print("3, multiplication")
    choice = input("enter the choice 1, 2, 3,=").strip()

   # help user to input the path of matrices
    file1 = input("enter the path of  matrix file the first one=   ").strip()
    file2 = input("enter the path of  matrix file the second one=   ").strip()


    try:
       #load matrice from file the user provide
        matrix1 = Sparsematrix.Load_From_File(file1)
        
        matrix2 = Sparsematrix.Load_From_File(file2)

      #perform selected operation
        if choice == "1":
            result = matrix1.addition(matrix2)
            print("addition result:")
        elif choice == "2":
            result = matrix1.subtraction(matrix2)
            print("substraction result")
        elif choice == "3":
            result = matrix1.multiplication(matrix2)
            print("multiplication result")
        else:
            print("wrong choice")
            return
        
        #print matrix dimension result
        print(f"rows={result.numrows}")
        print(f"cols={result.numcols}")
        
        #print non-zero element in matrix result
        for (row, col), value in sorted(result.data.items()):
            print(f"({row}, {col}, {value})")
        
        


    except Exception as e:
        #handle errors like invalid file format or incompatible matrice
        print(f"error: {e}")

#entry script points
if __name__ == "__main__":
    main()
