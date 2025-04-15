As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

## Dictionary name - keys and bday - values

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

## Dictionary value update using key as ref

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

## pop value to get rid of and add new one

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

## Iterate over values dictname.values() 

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

## calculate age using current date 



class BirthdayNotebook:

    def __init__(self):
        self.dict = {}

        side effect - initilising a dict

     notebook = BirthdayNotebook()
     no side effects

    def add_friends(self, name, birth_date):
        adds name and birth_date into dict as key: value pair
        side effect - manipulating dictionary


    def update_date(self, name, new_date):
        self.dict[name] = new_date

        update 
        side effects - manipulating dict

    def change_name(self, new_name, old_name):
        date = self.dict[old_name]
        self.dict[new_name] = date

        add new name, attach old value and delete old name
        side effects - manipulating dict

    def birthday_card_checker(self)

        returning dates of any name within 30 days of current date
        no side effects, only returning dict list

    def age_checker(self, current_date, birth_date)
        comparing the current date to birth date and returning age.
        no side effects


    
    


