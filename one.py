#ONE

PLAYER, COMPUTER, EMPTY = "X", "O", " "
board = [EMPTY] * 9

def check_winner(p):
    return any(board[a] == board[b] == board[c] == p for a, b, c in [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)])

def dfs(turn):
    if check_winner(COMPUTER): return 10
    if check_winner(PLAYER): return -10
    if EMPTY not in board: return 0
    best = -1000 if turn else 1000
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = COMPUTER if turn else PLAYER
            best = max(best, dfs(not turn)) if turn else min(best, dfs(not turn))
            board[i] = EMPTY
    return best
    
def find_best_move():
    return max((i for i in range(9) if board[i] == EMPTY), 
              key = lambda i: (board.__setitem__(i, COMPUTER), v:=dfs(False),
              board.__setitem__(i, EMPTY), v) [3], default=-1)

def play_game():
    while True:
        print("\n".join(" | ".join(board[i:i+3]) for i in range(0, 9, 3)))
        p_move = int(input("Enter move (0-8): "))
        if board[p_move] != EMPTY: print("Invalid move! Try again."); continue
        board[p_move] = PLAYER
        if check_winner(PLAYER): print("Player wins!"); break
        if EMPTY not in board: print("Tie!"); break
        print("Computer's move...")
        board[find_best_move()] = COMPUTER
        if check_winner(COMPUTER): print("Computer wins!"); break
        if EMPTY not in board: print("Tie!"); break
            
play_game()