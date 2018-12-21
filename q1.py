# Determines whether a Sudoku solution is valid.

def valid_rows(soln):
    ''' Returns True if each row is valid 
        and False otherwise.
    ''' 
    key = {1,2,3,4,5,6,7,8,9}
    checker = 0
    for row in soln:
        rnums = set()
        for val in row:
            rnums.add(val)
        if key.issubset(rnums):
            checker += 1
    
    if checker == 9:
        return True
    else:
        return False

def valid_cols(soln):
    ''' Returns True if each column
        is valid and False otherwise.
    '''
    key = {1,2,3,4,5,6,7,8,9}
    checker = 0
    for c in range(9):
        cnums = set()                
        for row in soln:
            cnums.add(row[c])
        if key.issubset(cnums):
            checker += 1
    if checker == 9:
        return True
    else:
        return False
    
def valid_blocks(soln):
    ''' Checks each 3 x 3 block in the puzzle. 
        Returns True if each block is valid 
        and False otherwise.
    '''
    key = {1,2,3,4,5,6,7,8,9}
    checker = 0
    
    for c in range(0,7,3):
        bnums = set()
        k = 0
        while k <= 2:
            bnums.add(soln[k][c])
            bnums.add(soln[k][c+1])
            bnums.add(soln[k][c+2])
            k += 1
        if key.issubset(bnums):
            checker += 1
            
    for c in range(0,7,3):
        bnums = set()
        k = 3
        while k <= 5:
            bnums.add(soln[k][c])
            bnums.add(soln[k][c+1])
            bnums.add(soln[k][c+2])
            k += 1
        if key.issubset(bnums):
            checker += 1
        
    for c in range(0,7,3):
        bnums = set()
        k = 6
        while k <= 8:
            bnums.add(soln[k][c])
            bnums.add(soln[k][c+1])
            bnums.add(soln[k][c+2])
            k += 1
        if key.issubset(bnums):
            checker += 1
    
    if checker == 9:
        return True
    else:
        return False
    
def valid_soln(soln):
    ''' Returns True if a Sudoku solution is valid and False
        otherwise.
    '''
    
    # Check if rows are valid. 
    if not valid_rows(soln):
        return False

    # Check if columns are valid.
    if not valid_cols(soln):
        return False

    # Check if 3x3 submatrices (or blocks) are valid.
    if not valid_blocks(soln):
        return False        
    
    # If all checks pass, then the solution is valid.
    return True


def main():
    
    ''' The checking process begins here. '''
   
    # Get file name.
    file_name = input('Enter filename: ')
    
    # Open file and read its data.
    input_file = open(file_name)
    file_data = input_file.readlines()
   
    # Close file since the information from the file is
    # stored in the list file_data. While not necessary,
    # it is a good habit to close a file once you are 
    # done with it.  
    input_file.close()
    
    # sudoku_soln is populated with the data
    # from the solution file. sudoku_soln is a
    # tuple of tuples, where each tuple is of size
    # 9. Draw a picture of sudoku_soln before you
    # try to write the remaining code.
    
    # Also, when adding values to a tuple, if we
    # are only add one tuple, we must use a comma
    # at the end (see Lines A & B).
    # sudoku_soln= ((5, 4, 6, 8, 9, 3, 2, 1, 7), (3, 9, 2, 1, 7, 4, 6, 8, 5), etc
    sudoku_soln = ()
    for line in file_data:
        row = ()
        for value in line.strip():
            row += (int(value),)     # Line A
        sudoku_soln += (row,)        # Line B
     
    # Check and print results. 
    print()
    if valid_soln(sudoku_soln):
        print('Valid solution')
    else:
        print('Invalid solution')


main()