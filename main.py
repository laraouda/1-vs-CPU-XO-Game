# final project
# 1 vs computer
import pickle
import random
def play_game(resume):
    board = resume["board"]
    player_character = resume["X"]
    computer_character = resume["O"]
    board = {"1": " ", "2": " ", "3": " ",
             "4": " ", "5": " ", "6": " ",
             "7": " ", "8": " ", "9": " "}

    board_keys = []
    for key in board:
        board_keys.append(key)

    # setting up the board display
    def print_board(board):
        print(board["1"] + "|" + board["2"] + "|" + board["3"])
        print("-+-+-")
        print(board["4"] + "|" + board["5"] + "|" + board["6"])
        print("-+-+-")
        print(board["7"] + "|" + board["8"] + "|" + board["9"])

    print("welcome to tic tac toe")
    start_or_resume = input("do you want to start a new game or resume game?[s/r]")
    if start_or_resume == "s":


        def game():
            turn = "X"
            counter = 0
            i = 0
            while True:
                pcmove = random.randint(1, 9)
                print_board(board)
                print("your turn" + turn + ",chose your move ")
                if i % 2 == 0:
                    move = input()
                # else:
                while True:
                    ask = input("do you want to continue?")
                    if ask == "no":
                        game_dict = {"board": board, "player_character": "X", "computer_character": "O"}
                        pickle.dump(game_dict, open('test.pkl', "wb"))
                        exit()

                    pcmove = random.randint(1, 9)
                    move = str(pcmove)
                    if board[move] == " ":
                        board[move] = turn
                        counter += 1
                        break
                    else:
                        print("that place is taken already.")
                        break

                if counter >= 5:
                    # horizontal
                    if board["1"] == board["2"] == board["3"] != " ":
                        print("Game over")
                        print(turn + " " + "won, congrats!")
                        break
                    elif board["4"] == board["5"] == board["6"] != " ":
                        print("Game over")
                        print(turn + " " + "won, congrats!")
                        break
                    elif board["7"] == board["8"] == board["9"] != " ":
                        print("Game over")
                        print(turn + " " + "won, congrats!")
                        break
                        # vertical
                    elif board["1"] == board["4"] == board["7"] != " ":
                        print("Game over")
                        print(turn + " " + "won, congrats!")
                        break
                    elif board["2"] == board["5"] == board["8"] != " ":
                        print("Game over")
                        print(turn + " " + "won, congrats!")
                        break
                    elif board["3"] == board["6"] == board["9"] != " ":
                        print("Game over")
                        print(turn + " " + "won, congrats!")
                        break
                        # diagonal
                    elif board["1"] == board["5"] == board["9"] != " ":
                        print("Game over")
                        print(turn + " " + "won, congrats!")
                        break
                    elif board["3"] == board["5"] == board["7"] != " ":
                        print("Game over")
                        print(turn + " " + "won, congrats!")
                        break
                # if counter == 9:

                # print("game over")
                # print("it's a tie")

                if turn == "X":
                    turn = "O"
                    pcmove = str(pcmove)
                else:
                    turn = "X"
                i += 1
            restart = input("would you like to play again? (y/n)")
            if restart == "y" or restart == "Y":
                for key in board_keys:
                    board[key] = " "

                    game()
    elif start_or_resume == "r":
        resume = pickle.load(open('test.pkl', "rb"))

    if __name__ == "__main__":
        game()













board = {"1": " ", "2": " ", "3": " ",
         "4": " ", "5": " ", "6": " ",
         "7": " ", "8": " ", "9": " "}

board_keys = []
for key in board:
    board_keys.append(key)


# setting up the board display
def print_board(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["7"] + "|" + board["8"] + "|" + board["9"])




def game() :
    turn = "X"
    counter = 0
    i = 0
    while True:
        pcmove = random.randint(1, 9)
        print_board(board)
        print("your turn" + turn + ",chose your move ")
        if i % 2 == 0:
            move = input()
        # else:
        while True:
            ask=input("do you want to continue?")
            if ask == "no":
                game_dict = {"board":board,"player_character":"X","computer_character":"O"}
                pickle.dump(game_dict, open('test.pkl', "wb"))
                exit()

            pcmove = random.randint(1, 9)
            move =str(pcmove)
            if board[move] == " ":
                board[move] = turn
                counter += 1
                break
            else:
                print("that place is taken already.")
                break

        if counter >= 5:
            # horizontal
            if board["1"] == board["2"] == board["3"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["4"] == board["5"] == board["6"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["7"] == board["8"] == board["9"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
                # vertical
            elif board["1"] == board["4"] == board["7"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["2"] == board["5"] == board["8"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["3"] == board["6"] == board["9"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
                # diagonal
            elif board["1"] == board["5"] == board["9"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
            elif board["3"] == board["5"] == board["7"] != " ":
                print("Game over")
                print(turn + " " + "won, congrats!")
                break
        # if counter == 9:

            # print("game over")
            # print("it's a tie")

        if turn == "X":
            turn = "O"
            pcmove= str(pcmove)
        else:
            turn = "X"
        i+=1
    restart = input("would you like to play again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            board[key] = " "

            game()

print("welcome to tic tac toe")
start_or_resume= input("do you want to start a new game or resume game?[s/r]")
if start_or_resume == "s":
    game()
elif start_or_resume == "r":
    resume = pickle.load(open('test.pkl', "rb"))
    board = resume["board"]

if __name__ == "__main__":
    game()
