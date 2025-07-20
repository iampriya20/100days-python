# day26_square_cube_calculator.py

def calculate_square_cube(number):
    square = number ** 2
    cube = number ** 3
    return square, cube

if __name__ == "__main__":
    try:
        num = float(input("Enter a number: "))
        square, cube = calculate_square_cube(num)
        print(f"🟦 Square of {num} is: {square}")
        print(f"🟥 Cube of {num} is: {cube}")
    except ValueError:
        print("❌ Please enter a valid number.")
