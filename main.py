from sum_mod import add
from diff_mod import subtract
from prod_mod import multiply

def menu():
    print("Arithmetic Project")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    print("1) Add  2) Subtract  3) Multiply")
    choice = input("Choose: ").strip()
    if choice == "1":
        print("Result:", add(a,b))
    elif choice == "2":
        print("Result:", subtract(a,b))
    elif choice == "3":
        print("Result:", multiply(a,b))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    menu()