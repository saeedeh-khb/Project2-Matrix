#Receive a 3×3 matrix from the user
def get_matrix():
    matrix = []

    for i in range(3):
        while True:
            row = input(f"Enter row {i + 1} (3 numbers): ").split()

            if len(row) != 3:
                print("Please enter exactly 3 numbers.")
                continue
            try:
                row = [int(num) for num in row]
                matrix.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

    return matrix


#Calculate the sum of each row
def calculate_row_sums(matrix):
   
    return [sum(row) for row in matrix]


#Calculate the sum of each column
def calculate_column_sums(matrix):
    
    column_sums = []

    for col in range(3):
        column_sum = 0
        for row in range(3):
            column_sum += matrix[row][col]
        column_sums.append(column_sum)

    return column_sums


#run the application
def main():
    matrix = get_matrix()
    row_sums = calculate_row_sums(matrix)
    column_sums = calculate_column_sums(matrix)

    print("\nRow sums:")
    for i, total in enumerate(row_sums, start=1):
        print(f"Row {i}: {total}")

    print("\nColumn sums:")
    for i, total in enumerate(column_sums, start=1):
        print(f"Column {i}: {total}")



if __name__ == "__main__":
    main()