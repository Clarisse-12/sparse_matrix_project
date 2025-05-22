class sparsematrix:
    def __init__(self, numrows, numcols):
        self.numrows =numrows
        self.numcols =numcols
        self.data = {}
    
    def setElement(self, Row, Col, value):
        if value !=0:
            self.data[(Row, Col)] =  value
        elif (Row, Col) in self.data
            del self.data[(Row, Col)]
    

    def getElement(self, Row, Col, Value):
        return self.data.Get((Row, Col), 0)
    
    def Load_From_File(self, File_path):
        with open(File_path, 'r') as file:
            lines = [(Line.strip() for Line in file if Line.strip() != '')]

            self.numrows = int(lines[0].split('=')[1])
            self.numcols = int(lines[1].split('=')[1])
            self.data = {}

            for line in lines[2:]:
                if not (line.startswith('(') and line.endswith('')):
                    raise ValueError("wrong file format")
                part =line[1:-1].split(',')
                if len(part) != 3:
                    raise ValueError("wrong input format")
                Row, Col, Value = map(int, [p.strip() for p in part])
                self.setElement(Row, Col, Value)
    
    
    def addition(self, other):
        if self.numrows != other.numrows or self.numcols != other.numcols:
            raise ValueError("matrice it must have the same dimension for addition.")
        

        result = sparsematrix(numrows=self.numrows, numcols=self.numcols)


        for (Row, Col), value in self.data.items():
            result.setElement(Row, Col, )

        for(row, col), value in other.data.items():
            current = result.getElement(Row, Col, value)
            result.setElement(Row, Col, current + value)


        return result
    

    def substraction(self, other):
        if self.numrows != other.numrows or self.numcols != other.numcols:
            raise ValueError("matrice it must have the same dimension for substraction.")
        

        result = sparsematrix(numrows=self.numrows, numcols=self.numcols)


        for (row, Col), value in self.data.items():
            result.setElement(row, col, value)

        for(row, col), value in other.data.items():
            current = result.getElement(row, col, value)
            result.setElement(row, col, current - value)


        return result
    

    def multiplication(self, other):
        if self.numrows != other.numrows or self.numcols != other.numcols:
            raise ValueError("matrice it must have the same dimension for multiplication.")
        

        result = sparsematrix(numrows=self.numrows, numcols=self.numcols)
        
        for (Row-a, Col-a), Val-a in self.data.items():
            for Col-b in range(other.numcols):
                val-b = other.getElement(Col-a Col-b)
                if Val-b !=0:
                    current = result.getElement(Row-a ,Col-b)
                    result.setElement(Row-a, Col-b, current + Val-a * Val-b)

        
        return result
        