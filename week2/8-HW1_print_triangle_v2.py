
def my_print(n, mychar="x"):
    for i in range(n):
        print(mychar, end="")
    print("")

end = int(input())
for i in range(end):
    my_print(i+1)


end = int(input())
for i in range(end):
    for j in range(i+1):
        print("x", end="")
    print("")

def main():
    pass

if __name__ == "__main__":
    main()