from src.utils import format_list, get_timestamp

def test_format_list():
    assert format_list(["a", "b", "c"]) == "a, b, c"
    assert format_list([]) == ""

def test_get_timestamp():
    result = get_timestamp()
    assert "T" in result  # ISO format includes T