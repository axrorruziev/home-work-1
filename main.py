print("ну что готовы-начинаем нашу игру")
player1 = input("player-1/введите-камень/ножницы/бумага/")
player2 = input("player-2/введите-камень/ножницы/бумага/")
if player1 == "камень" and player2 == "ножницы":
    print("поздравляем player1 вы выграли")
elif player1 == "камень" and player2 == "бумага":
    print("поздравляем player2 вы выграли")
elif player1 == "камень" and player2 == "камень":
    print("у вас ничья")
elif player1 == "ножницы" and player2 == "камень":
    print("поздравляем player2 вы выграли")
elif player1 == "бумага" and player2 == "камень":
    print("поздравляем player1 вы выграли")
elif player1 == "ножницы" and player2 == "бумага":
    print("поздравляем player1 вы выграли")
elif player1 == "бумага" and player2 == "ножницы":
    print("поздравляем player2 вы выграли")
elif player1 == "ножницы" and player2 == "ножницы":
    print("у вас ничья")
elif player1 == "бумага" and player2 == "бумага":
    print("у вас ничья")
else:
    print('не понял вас напишите камень либо ножницы или бумага')







