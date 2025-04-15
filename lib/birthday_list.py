class BirthdayNotebook:

    def __init__(self):
        self.dict = {}

        #side effect - initilising a dict

     #notebook = BirthdayNotebook()
     #no side effects

    def add_friends(self, name, birth_date):
        #adds name and birth_date into dict as key: value pair
        #side effect - manipulating dictionary
        self.dict[name] = birth_date

    def update_date(self, name, new_date):
        self.dict[name] = new_date

        #update 
        #side effects - manipulating dict

    def change_name(self, new_name, old_name):
        date = self.dict[old_name]
        self.dict[new_name] = date
        del self.dict[old_name]

    #     #add new name, attach old value and delete old name
    #     #side effects - manipulating dict

    # def birthday_card_checker(self)

    #     #returning dates of any name within 30 days of current date
    #     #no side effects, only returning dict list

    # def age_checker(self, current_date, birth_date)
    #     #comparing the current date to birth date and returning age.
    #     #no side effects