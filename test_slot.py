from slot import deposit, get_number_of_lines, get_bet

def main():
    test_deposit()
    test_get_number_of_lines()
    test_get_bet()

    

def test_deposit():
    assert deposit() > 0
    # if deposit() <= 0:
    #     print("enter a value greater than 0")
        
        
def test_get_number_of_lines():
    assert get_number_of_lines() >= 1 or get_number_of_lines() <= 3
    # if get_number_of_lines() < 1 or get_number_of_lines() > 3:
    #     print("please enter a number between 1 and 3")
              
def test_get_bet():
    assert get_bet() >= 1 or get_bet() <= 100
    # if get_bet() < 1 or get_bet() > 100:
    #     print("Amount must be between 1 and 100")
    
 
    

        
     
if __name__ == "__main__":
    main()     