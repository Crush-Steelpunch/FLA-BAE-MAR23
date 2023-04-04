import module_instruction

# example of function and testing in the same file.
def ret_tru():
    return True

def test_ret_tru():
    assert ret_tru() == True

    # testing functions imported from another file

def test_function_name():
    assert module_instruction.function_name() == "My function"
    assert module_instruction.function_name() != "My function is awesome"

def test_return_my_score():
    assert module_instruction.return_my_score(90) == "band b1"
    assert module_instruction.return_my_score(0) == "band b1"
    assert module_instruction.return_my_score(-50) == "band b1"
    assert module_instruction.return_my_score(120) == "band b2"
    assert module_instruction.return_my_score(240) == "band b3"
    assert module_instruction.return_my_score(350) == "band b4"
    for b1test  in range(100):
        assert module_instruction.return_my_score(b1test) == "band b1"
    
    for b2test  in range(100,200):
        assert module_instruction.return_my_score(b2test) == "band b2"

def test_polymo():
    test_instance = module_instruction.polymo()
    assert test_instance.trim("spleleodot") == "spleleodo"


    # writing the test, then making the code pass the test

def test_palindrome():
    assert module_instruction.palindrom_function("racecar") == True
    assert module_instruction.palindrom_function("abcdef") == False
    assert module_instruction.palindrom_function("tree") == False
    assert module_instruction.palindrom_function("amanaplanacanalpanama") == True