def minion_game(string):
    
    vowles = "AEIOU"
    consonents = "BCDGHJKLMNPQRSTVWXYZ"
    
    stuart = input("Stuart's Word")
    stuart_word = stuart.upper()
    
    kevin = input("Kevin's Word")
    kevin_word = kevin.upper()
    
    while stuart_word[0] not in vowles:
        stuart = input("Stuart's Word")
        stuart_word = stuart.upper()
        
    while kevin_word[0] not in consonents:
        kevin = input("Kevin's Word")
        kevin_word = kevin.upper()
    
    count_kevin = string.count(kevin) 
    count_stuart = string.count(stuart)

    if count_kevin > count_stuart:
        print(f"Kevin {count_kevin}") 
    else:
        print(f"Stuart {count_stuart}") 

s = input()
minion_game(s)
