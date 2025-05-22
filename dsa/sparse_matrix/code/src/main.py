from sparse_matrix import sparsematrix

def Main():
    print("==sparsematrix operation==")
    print("choose operation you want:")
    print("1, addition")
    print("2, subtraction")
    print("3, multiplication")
    choice = input("enter the choice 1, 2, 3,:").strip()


    file1 = input("enter the path of  matrix file the first one").strip()
    file2 = input("enter the path of  matrix file the second one").strip()


    try:
        matrix1 = sparsematrix(matrixfilepath=file1)
        matrix2 = sparsematrix(matrixfilepath=file2)


        if choice == "1":
            result = matrix1.addition(matrix2)
            print("addition result:")
        elif choice == "2":
            result = matrix2.substraction(matrix2)
            print("substraction result")
        elif choice == "3":
            result = matrix1.multiplication(matrix2)
            print("multiplication result")
        else:
            print("wrong choice")
            return
        
        for (row. col), value in sorted(result.data.items()):
            print(f"({row}, {col}, {value})")

    except Exception as e:
        print(f"error: {e}")


if __name__ == "__main__":
    main()
