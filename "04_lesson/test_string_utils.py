utils = StringUtils()

utils.trim("skypro")
Позитивный тест
def test_trim_positive(): 
    assert utils.trim("skypro") == "Skypro"
Негативный тест 
def test_trim_empty(): 
    assert utils.capitalize("") == ""
 
utils.contains("true" "false")
Позмтивный тест 
def test_contains_positive(): 
    assert utils.contains(""true" "false") == "true" "false
Неагтивный тест
def test__containsempty(): 
    assert utils.contains("") == ""

utils.delete_symbol("skypro")
Позитивный тест 
def test_delete_symbol_positive(): 
 assert utils.delete_symbol("skypro") == "Skypro"
 
Негативный тест 
def testdelete_symbol__empty(): 
    assert utils.delete_symbol("") == ""
