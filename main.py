from random import choice as randchoice
from os import name, system
import socket

hangman_drawings = [
    [
    "       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "...NO ERRORS..."],
    [
    "       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "       ",
    "============="],
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
    "============="],
    [
    "  +---+",
    "  |   |",
    "      |",
    "      |",
    "      |",
    "      |",
    "============="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    "      |",
    "      |",
    "      |",
    "============="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    "  |   |",
    "      |",
    "      |",
    "============="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|   |",
    "      |",
    "      |",
    "============="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    "      |",
    "      |",
    "============="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    " /    |",
    "      |",
    "============="],
    [
    "  +---+",
    "  |   |",
    "  O   |",
    " /|\\  |",
    " / \\  |",
    "      |",
    "============="]
]


def draw_hangman(mistakes):
    return hangman_drawings[mistakes]


def choose_word():
    words = ["casa", "impiccato", "ciao", "rana", "porta"]
    return randchoice(words)


def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)



def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 12345)

    server_socket.bind(server_address)
    server_socket.listen(1)

    print("In attesa di connessioni...")

    connection, client_address = server_socket.accept()
    print(f"Connessione accettata da {client_address}")

    print("Come vuoi scegliere la parola?")
    while True:
        word_options = input("1) Scelta manuale\n2) Parole default\n(1 o 2) --> ")
        if (word_options == "1"):
            word_to_guess = input("PAROLA SCELTA: ")
            break
        elif (word_options == "2"):
            word_to_guess = choose_word()
            break
        else:
            print("Inserire o 1 o 2...")
            continue

    guessed_letters = set()
    mistakes = 0 # count errori

    while True:
        current_state = display_word(word_to_guess, guessed_letters)
        connection.sendall(f"{current_state}:{mistakes}".encode('utf-8'))

        if '_' not in current_state:  # Non ci sono più lettere da indovinare: fine gioco
            print("Il giocatore ha vinto!")
            break

        guess = connection.recv(1024).decode('utf-8')
        guessed_letters.add(guess)

        if guess not in word_to_guess:
            mistakes += 1
            print(f"Lettera sbagliata!\nErrori: {mistakes}")

    connection.close()
    server_socket.close()


def display_current_word(current_state):
    letters_or_word = current_state.split(':')[0] # del formato lettere:errori prende solo la parola (prima di :)
    print(letters_or_word)


def display_hangman(current_state):
    number_of_errors = int(current_state.split(':')[-1]) # del formato lettere:errori prende solo gli errori (dopo di :)
    hangman_representation = hangman_drawings[number_of_errors]
    for line in hangman_representation: # rappresenta hangman (riga per riga)
        print(line)
    print(f"\nERRORI: {number_of_errors}")


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('127.0.0.1', 12345)
    try:
        client_socket.connect(server_address)
        print("Aspettare la parola scelta da parte del PC host...")
        while True:
            current_state = client_socket.recv(1024).decode('utf-8') # riceve nel formato lettere:errori (es: wor_ld:3)

            display_hangman(current_state) # mostra hangman + gli errori
            print(f"\nPAROLA: {display_current_word(current_state)}") # mostra avanzamento parola
            #display_current_word(current_state) # mostra avanzamento parola

            if '_' not in current_state:
                print("Hai vinto!")
                break

            guess = input("Indovina una lettera: ")
            client_socket.sendall(guess.encode('utf-8'))
    except ConnectionRefusedError:
        print("PC host non trovato...")

    client_socket.close()


def main():
    while True:
        print("Benvenuto al Gioco dell'Impiccato!")
        print("1. Hosta una partita")
        print("2. Unisciti a una partita")
        print("3. Esci")
        choice = input("Scelta: ")

        if choice == '1':
            system('cls' if name == 'nt' else 'clear') # os.system os.name
            start_server()
        elif choice == '2':
            system('cls' if name == 'nt' else 'clear') # os.system os.name
            start_client()
        elif choice == '3':
            break
        else:
            print("Scelta non valida.")
        continue


if __name__ == "__main__":
    main()