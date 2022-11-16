def crossword(L):
    matrix = ([[0 for row in range(20)] for col in range(20)])
    hori_list = []
    vert_list = []
    mid_row = int(len(matrix)/2)
    if L:
        hori_list = L[0::2]
        vert_list = L[1::2]
    else:
        print("empty list")

    # for word in list
    for word in L:

        # check if first word and if it's length exceeds the length of matrix
        if word == hori_list[0]:
            word = list(str(word))
            if len(word) < len(matrix):
                matrix[mid_row] = word

        # place first word in the center of the grid
            x = 0
            while x < len(matrix) - len(matrix[mid_row]):
                matrix[mid_row].insert(x, 0)
                x += 1
            while len(matrix[mid_row]) < len(matrix):
                matrix[mid_row].append(0)
            else:
                print("reaches outside grid")

        elif word in vert_list:
            match_list = []
            word = list(str(word))

            # check horizontal and place vertical word
            if len(word) < len(matrix):
                for char in word:
                    row = 0
                    while row < len(matrix) - 1:
                        if char in matrix[row]:
                            col = matrix[row].index(char)
                            if matrix[row - 1][col + 1] == 0 and matrix[row + 1][col + 1] == 0 and matrix[row + 1][col] == 0 \
                                    and matrix[row + 1][col - 1] == 0 and matrix[row - 1][col - 1] == 0 \
                                    and matrix[row - 1][col] == 0:
                                match_list.append(char)
                                match_list.append(row)
                                match_list.append(word.index(char))
                                match_list.append(col)
                                row += 1
                        else:
                            print("no matching letter")
                        row += 1
            else:
                print("reaches outside grid")

            # place vertical word on grid
            if match_list:
                row = match_list[1] - match_list[2]
                col = match_list[3]
                total_length = len(word) + row
                if total_length <= len(matrix):
                    word_index = 0
                    while row < total_length:
                        while word_index < (len(word)):
                            if type(matrix[row][col]) == int:
                                matrix[row][col] = word[word_index]
                            word_index += 1
                            row += 1
                        break
                else:
                    print("reaches outside grid")
            else:
                print("illegal adjancencies")

        # next horizontal word in list
        elif word in hori_list[1:]:
            match_list = []
            word = list(str(word))
            if len(word) < len(matrix):
                for char in word:
                    row = 0
                    while row < len(matrix) - 1:
                        if char in matrix[row]:
                            col = matrix[row].index(char)
                            if matrix[row][col - 1] == 0 and matrix[row][col + 1] == 0 and matrix[row + 1][col + 1] == 0 and \
                                    matrix[row - 1][col + 1] == 0 and matrix[row - 1][col - 1] == 0:
                                # print("word can be added in row:{}".format(x))
                                match_list.append(char)
                                match_list.append(row)
                                match_list.append(word.index(char))
                                match_list.append(matrix[row].index(char))
                        row += 1
                    else:
                        print("no matching letter")

            # place horizontal word on grid
            if match_list:
                row = match_list[1]
                col = match_list[3] - match_list[2]
                total_length = len(word) + col

                if total_length <= len(matrix):
                    word_index = 0
                    while col < total_length:
                        while word_index < (len(word)):
                            if type(matrix[row][col]) == int:
                                matrix[row][col] = word[word_index]
                            word_index += 1
                            col += 1
                        break
                else:
                    print("reaches outside grid")
            else:
                print("no matching letter")

    # print the crossword
    for item in matrix:
        print(item)

    # write the crossword to file
    with open("output.txt", 'w') as file1:
        for item in matrix:
            c = ', '.join(str(x) for x in item)
            y = c.replace('0', ' ')
            z = y.replace(',', ' ')
            file1.writelines(z + '\n')


crossword(['addle', 'apple', 'clowning', 'incline', 'plan', 'go', 'prove', 'loon', 'nancy'])

