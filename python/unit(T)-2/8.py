# Global variable
x = 10

def outer():
    # Enclosing variable
    y = 20

    def inner():
        # Local variable
        z = 30
        nonlocal y
        y = 25
        print("Local variable z =", z)
        print("Nonlocal variable y =", y)

    inner()
    print("Enclosing variable y =", y)

def display():
    global x
    x = 15
    print("Global variable x =", x)

outer()
display()
