# Recursive function to solve Tower of Hanoi
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Main program
try:
    n = int(input("Enter the number of disks: "))

    if n <= 0:
        print("Error: Please enter a positive integer greater than zero.")
    else:
        print(f"\nThe sequence of moves for {n} disks:")
        tower_of_hanoi(n, 'A', 'C', 'B')

except ValueError:
    print("Error: Invalid input. Please enter an integer.")
