# TODO: Write the functions for arithmetic operations here
# These functions should cover Task 2

# addition
def addition(a, b):
    return a+b

# subtraction
def subtraction(a, b):
    return a-b

# multiplication
def multiplication(a, b):
    return a*b

# division
def division(a, b):
    if b == 0:
        print("float division by zero")
        # reset
    elif choice == "$":
        return None
    else:
        return a/b

# power
def power(a, b):
    return a**b

# remainder
def remainder(a, b):
    return a % b

# -------------------------------------
# TODO: Write the select_op(choice) function here
# This function should cover Task 1 (Section 2) and Task 3
# terminate


def select_op(choice):
    if choice == '#':
        return -1
# reset
    elif choice == "$":
        return None
    try:
        NumA = input("Enter first number: ")
        print(NumA)
        if NumA == '#':
          print("Done. Terminating")
          exit()
        
        else:
          fl_NumA = float(NumA)
  
        NumB = input("Enter second number: ")
        print(NumB)
        if NumB == '#':
          print("Done. Terminating")
          exit()
        
        else:
          fl_NumB = float(NumB)
    except ValueError:
        return None

    if choice == "+":
        print(fl_NumA, '+', fl_NumB, '=', addition(fl_NumA, fl_NumB))

    elif choice == "-":
        print(fl_NumA, '-', fl_NumB, '=', subtraction(fl_NumA, fl_NumB))

    elif choice == "*":
        print(fl_NumA, '*', fl_NumB, '=', multiplication(fl_NumA, fl_NumB))

    elif choice == "/":
        print(fl_NumA, '/', fl_NumB, '=', division(fl_NumA, fl_NumB))

    elif choice == "**":
        print(fl_NumA, '**', fl_NumB, '=', power(fl_NumA, fl_NumB))

    elif choice == "%":
        print(fl_NumA, '%', fl_NumB, '=', remainder(fl_NumA, fl_NumB))


# End the select_op(choice) function here
# -------------------------------------
# This is the main loop. It covers Task 1 (Section 1)
# YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")

    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    if (select_op(choice) == -1):
        # program ends here
        print("Done. Terminating")
        exit()
