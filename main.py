import random

quotes = ["je serai le roi des pirates", "Je deviendrai le meilleur sabreur du monde","je serai un grand guerriers des mers"]
characters = ["luffy", "zoro","shanks","doflamingo","sabo","barbe Blanche"]


def show_randow_quote(my_list):
    random_number = random.randint(0,  len(my_list) - 1)
    key = my_list[random_number]
    return key


user_answer = input("Tapez entrée pour connaitre une autre citation ou 'B' pour quitter le programme : ")


while user_answer != "B":
    print(show_randow_quote(characters) + " a dit : ", show_randow_quote(quotes))
    user_answer = input("Tapez entrée pour connaitre une autre citation ou 'B' pour quitter le programme : ")
