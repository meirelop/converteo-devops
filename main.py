from operations import add, subtract

def main():
    print("Math Operations")
    x, y = 10, 5

    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")

if __name__ == "__main__":
    main()
