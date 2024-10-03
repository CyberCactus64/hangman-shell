hangman_drawings = [
    [
    "       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "========="],
    [
    "       ",
    "      |",
    "      |",
    "      |",
    "      |",
    "      |",
    "============="],
    [
    "  +---+",
    "      |",
    "      |",
    "      |",
    "      |",
    "      |",
    "========="],
    [
    "  +---+",
    "  |   |",
    "      |",
    "      |",
    "      |",
    "      |",
    "========="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    "      |",
    "      |",
    "      |",
    "========="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    "  |   |",
    "      |",
    "      |",
    "========="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|   |",
    "      |",
    "      |",
    "========="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    "      |",
    "      |",
    "========="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    " /    |",
    "      |",
    "========="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    " / \\  |",
    "      |",
    "============="],
]

def draw_hangman(mistakes):
    return hangman_drawings[mistakes]

mistakes = int(input("Mistakes test: (insert numbers): "))
hangman_representation = hangman_drawings[mistakes]
for line in hangman_representation:
    print(line)
