from calculator import Calculator

def main() -> None:
    calculator = Calculator()

    print("Addition:", calculator.add(5, 3))
    print("Subtraction:", calculator.subtract(10, 4))
    print("Multiplication:", calculator.multiply(2, 6))
    print("Division:", calculator.divide(8, 2))

    try:
        print("Division by zero:", calculator.divide(5, 0))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
