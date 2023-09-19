ls = [" " for _ in range(9)]  # Updated to store symbols ("X", "O", or " ") instead of numbers
player_num = 1
sym = "X"
round1 = 1
winner_found = False


def check_winner():
    if ls[0] == ls[1] and ls[1] == ls[2]:
        return True
    elif ls[3] == ls[4] and ls[4] == ls[5]:
        return True
    elif ls[6] == ls[7] and ls[7] == ls[8]:
        return True
    elif ls[0] == ls[3] and ls[3] == ls[6]:
        return True
    elif ls[1] == ls[4] and ls[4] == ls[7]:
        return True
    elif ls[2] == ls[5] and ls[5] == ls[8]:
        return True
    elif ls[0] == ls[4] and ls[4] == ls[8]:
        return True
    elif ls[2] == ls[4] and ls[4] == ls[6]:
        return True
    else:
        return False


def check_hint():
    # Check for horizontal hints
    for i in range(0, 9, 3):
        if ls[i] == ls[i + 1] and ls[i] == sym and ls[i + 2] == " ":
            return i + 3  # Returning the position of the hint
        elif ls[i + 1] == ls[i + 2] and ls[i + 1] == sym and ls[i] == " ":
            return i + 1
        elif ls[i] == ls[i + 2] and ls[i] == sym and ls[i + 1] == " ":
            return i + 2

    # Check for vertical hints
    for i in range(3):
        if ls[i] == ls[i + 3] and ls[i] == sym and ls[i + 6] == " ":
            return i + 6
        elif ls[i + 3] == ls[i + 6] and ls[i + 3] == sym and ls[i] == " ":
            return i
        elif ls[i] == ls[i + 6] and ls[i] == sym and ls[i + 3] == " ":
            return i + 3

    # Check for diagonal hints (top-left to bottom-right)
    if ls[0] == ls[4] and ls[0] == sym and ls[8] == " ":
        return 8
    elif ls[4] == ls[8] and ls[4] == sym and ls[0] == " ":
        return 0
    elif ls[0] == ls[8] and ls[0] == sym and ls[4] == " ":
        return 4

    # Check for diagonal hints (top-right to bottom-left)
    if ls[2] == ls[4] and ls[2] == sym and ls[6] == " ":
        return 6
    elif ls[4] == ls[6] and ls[4] == sym and ls[2] == " ":
        return 2
    elif ls[2] == ls[6] and ls[2] == sym and ls[4] == " ":
        return 4

    return None  # No hint found


def show_matrix():
    i = 1
    while i <= 9:
        print(ls[i - 1], end="  ")
        if i % 3 == 0:
            print()
        i = i + 1


while round1 <= 9:
    show_matrix()
    print("Player", player_num, "select your box")
    h = check_hint()
    if h is None:
        print("Hint not found")
    else:
        print("You have to go for", h)

    a = int(input())
    if ls[a - 1] != "X" and ls[a - 1] != "O":
        ls[a - 1] = sym
        winner_found = check_winner()
        if winner_found:
            show_matrix()
            print("Player", player_num, "Wins...!")
            break
        else:
            round1 = round1 + 1
            if player_num == 1:
                player_num = 2
                sym = "O"
            elif player_num == 2:
                player_num = 1
                sym = "X"

if round1 == 9 and not winner_found:
    show_matrix()
    print("Match Draw...")
