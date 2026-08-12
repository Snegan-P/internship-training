def main():
    message = "Hello from the debugger!"
    print(message)

    breakpoint()

    number = 10
    result = number * 2
    print("Result:", result)


if __name__ == "__main__":
    main()
