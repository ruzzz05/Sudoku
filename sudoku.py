def buscarHueco(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return i, j  # Retorna la posición del primer hueco encontrado
    return None, None # Si no hay huecos, retorna None


def esValido(puzzle, row, col, num):
    

    #FILA
    row_num = puzzle[row]

    if num in row_num:
        return False
    

    #COLUMNA
    cols_num = []

    for i in range(9):
        cols_num.append(puzzle[i][col])

    if num in cols_num:
        return False
    
    num_row = row // 3 * 3
    num_col = col // 3 * 3

    for i in range(num_row, num_row + 3):
        for j in range(num_col, num_col + 3):
            if num == puzzle[i][j]:
                return False
            
    return True


def solucion(puzzle):

    row, col =  buscarHueco(puzzle)
    if row is None:  # Si no hay huecos, el puzzle está resuelto
        return True
    
    for num in range(1, 10):  # Prueba números del 1 al 9
        if  esValido(puzzle, row, col, num):
            puzzle[row][col] = num

            if solucion(puzzle):
                return True
            
        puzzle[row][col] = -1
    

    return False




