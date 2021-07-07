from nltk.corpus import words
import nltk
# nltk.download('words') -> uncomment this if you need to download the word file.

# our set of dictionary words. Converting to a set allowed for quicker lookup time.
words = set(words.words())

# Board size. If changing to a bigger board, modify this.
BOARD_SIZE_WIDTH = 4
BOARD_SIZE_LENGTH = 4

# our grid of letters. Change to whatever is needed.
grid = [["r", "a", "e", "l"],
        ["m", "o", "f", "s"],
        ["t", "e", "o", "k"],
        ["n", "a", "t", "i"]]


# generates and returns array containing potential moves for a letter at index (i, j) of grid.
def determine_available_moves(i, j):
    available_moves = []
    horizontal_indices = [i-1, i, i+1]
    vertical_indices = [j-1, j, j+1]
    for horizontal_index in horizontal_indices:
        # remove out of bounds entries
        if horizontal_index < 0 or horizontal_index > (BOARD_SIZE_WIDTH - 1):
            continue
        for vertical_index in vertical_indices:
            # remove out-of-bounds entries and the same grid entry that was provided (i,j)
            if (vertical_index < 0 or vertical_index > (BOARD_SIZE_LENGTH - 1) or
                    (vertical_index == j and horizontal_index == i)):
                continue
            available_moves.append((horizontal_index, vertical_index))
    return available_moves


# translates a path on the grid to a string, and prints it if it's an English word of 3 letters or more.
def word_from_path(path):
    word = ""
    for item in path:
        word += grid[item[0]][item[1]]
    # our homework requirement.
    if len(word) >= 3 and word.lower() in words:
        print(word)


# generates a path from an index then sends the path to be converted into a word.
def generate_path(i, j, move_list):
    word_from_path(move_list)
    next_moves = determine_available_moves(i, j)
    for next_move in next_moves:
        new_path = move_list.copy()
        if next_move not in new_path:
            new_path.append(next_move)
            generate_path(next_move[0], next_move[1], new_path)


def main():
    for i in range(BOARD_SIZE_WIDTH):
        for j in range(BOARD_SIZE_LENGTH):
            generate_path(i, j, [(i, j)])


main()
