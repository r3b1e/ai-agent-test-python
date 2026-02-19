from src.validator import is_valid_email, is_positive

def test_is_valid_email():
    assert is_valid_email("test@example.com") == True
    assert is_valid_email("invalid") == False
    assert is_valid_email("no@domain") == False

def test_is_positive():
    assert is_positive(5) == True
    assert is_positive(-1) == False
    assert is_positive(0) == False