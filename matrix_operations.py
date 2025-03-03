
import numpy as np

def get_matrix_input(name):
    """Gets matrix input from the user."""
    try:
        rows = int(input(f"Enter the number of rows for {name}: "))
        cols = int(input(f"Enter the number of columns for {name}: "))
        matrix = []
        print(f"Enter the elements of {name} row by row:")
        for _ in range(rows):
            row = list(map(float, input().split()))
            if len(row) != cols:
                print("Invalid row length. Try again.")
                return None
            matrix.append(row)
        return np.array(matrix)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return None

def matrix_operations():
    """Handles user interaction and performs matrix operations."""
    operation = input("Enter the operation (addition, multiplication, inverse): ").strip().lower()
    
    if operation == "addition":
        print("Matrix Addition Selected")
        A = get_matrix_input("Matrix A")
        B = get_matrix_input("Matrix B")
        if A is None or B is None or A.shape != B.shape:
            print("this operation cannot be done")
            return
        print("Result:")
        print(A + B)

    elif operation == "multiplication":
        print("Matrix Multiplication Selected")
        A = get_matrix_input("Matrix A")
        B = get_matrix_input("Matrix B")
        if A is None or B is None or A.shape[1] != B.shape[0]:
            print("this operation cannot be done")
            return
        print("Result:")
        print(np.dot(A, B))

    elif operation == "inverse":
        print("Matrix Inversion Selected")
        A = get_matrix_input("Matrix A")
        if A is None or A.shape[0] != A.shape[1]:
            print("this operation cannot be done")
            return
        try:
            print("Result:")
            print(np.linalg.inv(A))
        except np.linalg.LinAlgError:
            print("this operation cannot be done")
    else:
        print("Invalid operation. Please enter addition, multiplication, or inverse.")

if __name__ == "__main__":
    matrix_operations()
