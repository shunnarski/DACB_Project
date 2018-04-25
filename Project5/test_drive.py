







def Get_PSSM(blast_output):
    lin_reg_matrix = []

    gnb_matrix = []
    gnb_matrix.append(["-1" for _ in range(20)])
    gnb_matrix.append(["-1" for _ in range(20)])

    with open(blast_output, 'r') as pssm_file:
        start_read = False
        for line in pssm_file:
            if "Lambda" in line:
                break
            line = line.strip()
            if line == "":
                continue
            line = line.split()
            if line[0] == "1":
                start_read = True
            if start_read:
                scores = line[2:22]
                gnb_matrix.append(scores)

                lin_reg_vals = line[22:42]
                lin_reg_matrix.append(lin_reg_vals)

        gnb_matrix.append(["-1" for _ in range(20)])
        gnb_matrix.append(["-1" for _ in range(20)])

        lin_reg_matrix = average_PSSM_Weights(lin_reg_matrix)

    return gnb_matrix, lin_reg_matrix

def average_PSSM_Weights(matrix):

    average_weights = []

    row_length = len(matrix[0])
    matrix_length = len(matrix)

    for column in range(row_length):
        vals = []
        for row in range(matrix_length):
            val = matrix[row][column]
            vals.append(int(val))
        avg = sum(vals) / len(vals)
        avg = avg / float(100)
        average_weights.append(avg)

    return average_weights


gnb, lin_reg = Get_PSSM("test.pssm")

print lin_reg

print

print gnb


