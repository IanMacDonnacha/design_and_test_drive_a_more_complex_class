from lib.birthday_list import *
## TEST EXAMPLES

"""
test_initialiser()
notebook = BirthdayNotebook()
"""


"""
test_add_friends("ian", "1990-02-05")
assert dict == {"ian", "1990-02-05"}
"""

"""
test_update_date("ian", "1995-02-05")
assert dict == {"ian", "1995-02-05"}
"""

"""
test_change_name("john", "ian")
assert dict == {"john", "1990-02-05"}
"""

"""
test_birthday_card_checker()
assert upcomming dict == {"ian": "1995-02-05"}
"""


"""
test_age_checker("2025-04-15", ""1995-02-05"")
assert result == 30
"""

def test_for_initiliser():
    notebook = BirthdayNotebook()
    assert notebook.dict == {}

def test_add_friends():
    notebook = BirthdayNotebook()
    notebook.add_friends("Giulliano", "1991-11-28")
    assert notebook.dict == {"Giulliano": "1991-11-28"}

def test_update_date():
    notebook = BirthdayNotebook()
    notebook.add_friends("Giulliano", "1991-11-28")
    assert notebook.dict == {"Giulliano": "1991-11-28"}
    notebook.update_date("Giulliano", "1996-11-28")
    assert notebook.dict == {"Giulliano": "1996-11-28"}

def test_change_name():
    notebook = BirthdayNotebook()
    notebook.add_friends("Giulliano", "1991-11-28")
    assert notebook.dict == {"Giulliano": "1991-11-28"}
    notebook.change_name("borris", "Giulliano")
    assert notebook.dict == {"borris": "1991-11-28"}

