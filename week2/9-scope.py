
# scope
# the outside is global area
# x is global variable
x = 10

def main():
    # per function have its own private area, so called "local area"
    # it is legal to be a nested structure
    #
    # ex:
    # main()
    # --> inner()
    # --> --> inner_again()
    #
    # x, y are local variable here
    x = 100
    y = 100

    # it is legal to define a function inside a function
    # from the perspective of main function, inner() is a function
    # but it is invisivle from global area
    def inner():
        z = 100

if __name__ == "__main__":
    main()