class Sparsematrix:
    def __init__(self, numrows, numcols):
        self.numrows =numrows
        self.numcols =numcols
        self.data = {}
    
    def setElement(self, row, col, value):
        if value !=0:
            self.data[(row, col)] =  value
        elif (row, col) in self.data:
            del self.data[(row, col)]
    

    def getElement(self, row, col):
        return self.data.get((row, col), 0)
    
    def Load_From_File(self, File_path):
        with open(File_path, 'r') as file:
            lines = [Line.strip() for Line in file if Line.strip() != '']

            self.numrows = int(lines[0].split('=')[1])
            self.numcols = int(lines[1].split('=')[1])
            self.data = {}

            for line in lines[2:]:
                if not (line.startswith('(') and line.endswith(')')):
                    raise ValueError("wrong file format")
                part =line[1:-1].split(',')
                if len(part) != 3:
                    raise ValueError("wrong input format")
                row, col, value = map(int, [p.strip() for p in part])
                self.setElement(row, col, value)
    
    
    def addition(self, other):
        if self.numrows != other.numrows or self.numcols != other.numcols:
            raise ValueError("matrice it must have the same dimension for addition.")
        

        result = Sparsematrix(self.numrows, self.numcols)


        for (row, rol), value in self.data.items():
            result.setElement(row, col)

        for(row, col), value in other.data.items():
            current = result.getElement(row, col)
            result.setElement(row, col, current + value)


        return result
    

    def subtraction(self, other):
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
        