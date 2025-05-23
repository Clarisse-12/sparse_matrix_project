class Sparsematrix:
    """ 

     sparsematrix class using dictionary to keep non-zero elements. 
     support matrix operation like addition, subtraction, and multiplication.
     and allow data to laod from formated files.
     """
    def __init__(self, numrows, numcols):
        """
        initializing sparse marix with number of cols and rows that given.
        args:
        numrows(int)=number of rows in matrix.
        numcols(int)=number of colomns in matrix.
        """
        self.numrows =numrows
        self.numcols =numcols
        self.data = {}
    
    def setElement(self, row, col, value):

        """
        set value at specific position in matrix.
        store non-zero values only.
        args:
        row(int)=row index.
        cols(int)=cols index.
        value(int)=value to set.
        """
        if value !=0:
            self.data[(row, col)] =  value
        elif (row, col) in self.data:
            del self.data[(row, col)]
    

    def getElement(self, row, col):

        """
        retrieves value at specific position in matrix.
        args:
        row(int)=row index.
        cols(int)=cols index.

        return:
        int: value of given position or 0 if not set.
        """
        return self.data.get((row, col), 0)
    @classmethod
    def Load_From_File(cls, File_path):

        """
        creat sparsematrix instance for loading data from foemat files.
         
        expected format of files:
        rows=number
        cols=number
        (rows, cols, values)

        args:
        file_path= path of files

        return:
        sparsematrix: sparsematrix loaded from given values.
        """
        with open(File_path, 'r') as file:
            lines = [Line.strip() for Line in file if Line.strip() != '']

            numrows = int(lines[0].split('=')[1])
            numcols = int(lines[1].split('=')[1])
            matrix = cls(numrows, numcols)

            for line in lines[2:]:
                if not (line.startswith('(') and line.endswith(')')):
                    raise ValueError("wrong file format")
                line =line[1:-1].split(',')
                if len(line) != 3:
                    raise ValueError("wrong input format")
                row, col, value = line
                row, col, value = int(row), int(col), int(value)
                matrix.setElement(row, col, value)

            return matrix
    
    
    def addition(self, other):

        """
        add other sparse matrix to this matrix.

        args:
        Sparsematrix=other matrix of same dimension.

        return:
        returning matrix results after  addition.

        or raise:
        valueError=matrice it must have the same dimension for addition if dimension doesn't match.
        """
        if self.numrows != other.numrows or self.numcols != other.numcols:
            raise ValueError("matrice it must have the same dimension for addition.")
        

        result = Sparsematrix(self.numrows, self.numcols)


        for (row, col), value in self.data.items():
            result.setElement(row, col, value)

        for(row, col), value in other.data.items():
            current = result.getElement(row, col)
            result.setElement(row, col, current + value)


        return result
    

    def subtraction(self, other):
        
        """
        subtract other sparse matrix to this matrix.

        args:
        Sparsematrix=other matrix of same dimension.

        return:
        returning  matrix results after substraction.

        or raise:
        valueError=matrice it must have the same dimension for subtraction if dimension doesn't match.
        """
        if self.numrows != other.numrows or self.numcols != other.numcols:
            raise ValueError("matrice it must have the same dimension for subtraction.")
        

        result = Sparsematrix(numrows=self.numrows, numcols=self.numcols)


        for (row, col), value in self.data.items():
            result.setElement(row, col, value)

        for(row, col), value in other.data.items():
            current = result.getElement(row, col)
            result.setElement(row, col, current - value)


        return result
    

    def multiplication(self, other):

        """
        multiply one matrix by other sparse matrix.

        args:
        Sparsematrix=other matrix where elf.numcols ==other.numrows.
        
        retrun:
        returning  matrix results after multiplication.

        or raise:
        valueError:matrice it must have the same dimension for multiplication ,if dimension is not correct for multiplication.
        """
        if self.numcols != other.numrows:
            raise ValueError("matrice it must have the same dimension for multiplication.")
        

        result = Sparsematrix(self.numrows, other.numcols)
        
        for (row_a, col_a), val_a in self.data.items():
            for col_b in range(other.numcols):
                val_b = other.getElement(col_a, col_b)
                if val_b !=0:
                    current = result.getElement(row_a, col_b)
                    result.setElement(row_a, col_b, current + val_a * val_b)

        
        return result
    
        