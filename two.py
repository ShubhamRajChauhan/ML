#TWO

def count_inversions(puzzle):
    tiles=[tile for tile in puzzle if tile != 0]
    inversions = sum(1 for i in range(len(tiles)) for j in range(i+1, len(tiles)) if tiles[i] > tiles[j])
    return inversions

def is_solvable(puzzle):
    return count_inversions(puzzle) % 2 == 0

def get_user_puzzle():
    print("\nEnter the 8-puzzle configuration as 9 space-separated numbers (0 represents the empty space).")
    user_input = input("Example: 1 2 3 4 5 6 7 8 0\nYour puzzle: ")
    puzzle = list(map(int, user_input.split()))
    if len(puzzle) != 9 or set(puzzle) != set(range(9)):
        print("Invalid input! Please enter numbers 0-8 exactly once.")
        return get_user_puzzle()
    return puzzle

def main():
    while True:
        puzzle = get_user_puzzle()
        result = "Solvable" if is_solvable(puzzle) else "Not Solvable"
        print(f"Puzzle: {puzzle} -> {result}")
        again = input("\n Do you want to test another puzzle ? (yes/no): ").strip().lower()
        if again != 'yes' :
              print("Existing program. Goodbye!")
              break
              
main()
