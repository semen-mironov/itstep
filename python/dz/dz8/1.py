size = 3
char1 = "*"
char2 = "_"

for row in range(8):
    for i in range(size):
        for column in range(8):
            if (row + column) % 2 == 0:
                current_char = char1
            else:
                current_char = char2
            
            print(current_char * size, end="")
        print()