import ComplexLibrary as cl

def finalMatrix(matrix):
    row, column = len(matrix), len(matrix[0])
    for i in range(row):
        nRow = []
        for j in range(column):
            nRow.append([(cl.complexMod(matrix[i][j]) ** 2), 0])

        matrix[i] = nRow
    return matrix


def sistemaprobabilisticoquantico(matrix, vectIni, clicks):
    if (clicks >= 0) and (type(clicks) is int):
        copyMatrix = matrix[:]

        for i in range(clicks):
            matrix = cl.matrixProduct(matrix, copyMatrix)
        return finalMatrix(matrix)
    return -1


def sistemaprobabilistico(matrix, vectIni, clicks):
    if (clicks >= 0) and (type(clicks) is int):
        for x in range(clicks):
            vectIni = cl.accionmatrizvector(matrix, vectIni)
        return vectIni
    return -1


def canicasbooleanas(clicks, booleanMatrix, vectIni):
    if (clicks >= 0 and type(clicks) is int):
        for c in range(clicks):
            vectIni = cl.accionvectormatrizboolean(booleanMatrix, vectIni)
        return vectIni


def multiplerendijaclasico(matrix, vectIni, clicks):
    return sistemaprobabilistico(matrix, vectIni, clicks)

def multiplerendijacuantico(matrix, vectIni, clicks):
    return sistemaprobabilisticoquantico(matrix, vectIni, clicks)
