
def end_talk():
    game_start = input("게임을 시작하시겠습니까?(T/F) > ")
    
    def choice_turn():
        turn = input("선공(택 1) or 후공(택 2) > ")
        if turn == "1":
            print("선공")
            return True
        elif turn == "2":
            print("후공")
            return False
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            choice_turn()
    
    
    def my_turn(pre_word):
        word = input("단어를 입력하세요. > ")
        print(f"pre_word[len(pre_word)-1] == word[0] {len(pre_word)-1} , {word[0]}")
        if pre_word == "" or pre_word[len(pre_word)-1] == word[0]:
            print(f"word111111 : {word}")
            return word
        else:
            print("잘못된 입력입니다. 다시 입력해주세요.")
            my_turn(pre_word)
    
    

    if game_start == "T" :
        print("t")
        
        if choice_turn():
            word = my_turn("")
            print(f"word : {word}")
            
        else:
            print()
    elif game_start == "F" :
        print("f")
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        end_talk()
        

end_talk()