if __name__ == "__main__":

    print("PROGRAM TO GENERATE RANDOM NUMBERS")
    import random
    generate_numbers = int(input("Enter how many numbers do you want to generate: "))
    num_1= int(input("Enter the first number: "))
    num_2= int(input("Enter the second number: "))

    print(f"Numbers will be generated {num_1} and {num_2}")

    for x in range(generate_numbers):
        print(random.randint(num_1,num_2))