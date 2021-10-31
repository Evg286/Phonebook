import pandas as pd
import json
from time import sleep


class Contacts:
    def __init__(self):
        contacts = {}
        with open('contacts.json', 'a') as file:
            json.dumps(contacts)

    def display_contacts(self):
        with open('contacts.json') as file:
            df = pd.read_json(file)
            if df.empty:
                sleep(0.5)
                print("\nThe list is empty.")
            else:
                sleep(0.5)
                print('\nContacts list:\n\n', df)

            sleep(0.5)
            return

    def add_contacts(self):
        with open('contacts.json', 'r+') as file:

            df = pd.read_json(file)
            self.found = 0
            self.search_fname = input("\nEnter first name: ")
            self.search_lname = input("Enter last name: ")
            for i in range(len(df)):
                if df.iloc[i, 0] == self.search_fname:
                    if df.iloc[i, 1] == self.search_lname:
                        self.found += 1
                        sleep(0.5)
                        print("\nAlready in contacts...")
                        sleep(0.5)
                        return

            df.columns = ['First Name', 'Last Name', 'Phone Number']
            df = df.append({'First Name': self.search_fname,
                            'Last Name': self.search_lname,
                            'Phone Number': input("Enter phone number: ")},
                           ignore_index=True)

        with open('contacts.json', 'w+') as file:
            df.to_json(file)
            sleep(0.5)
            print('\nUpdated List: \n\n', df, '\n\n')
        sleep(0.5)
        return

    def search_contact(self):
        with open('contacts.json', 'r+') as file:
            df = pd.read_json(file)
            if df.empty:
                sleep(0.5)
                print("\nThe list is empty.")
                sleep(0.5)
                return
            else:
                self.found = False
                search_fname = input("\nEnter contact's first name: ")
                search_lname = input("Enter contact's last name: ")
                for i in range(len(df)):
                    if df.iloc[i, 0] == search_fname:
                        if df.iloc[i, 1] == search_lname:
                            self.found = True
                            print("\nContact found...\n")
                            sleep(1)
                            print("\n\nContact's Details:\n",
                                  "\nFull Name:", df.iloc[i][0], df.iloc[i][1],
                                  "\nPhone Number:", df.iloc[i][2])
                            sleep(0.5)
                            return menu()
                if not self.found:
                    print('\nContact not in list.')
                    sleep(0.5)
                    return

    def update_contact(self):
        with open('contacts.json', 'r+') as file:
            df = pd.read_json(file)
            if df.empty:
                sleep(0.5)
                print("\nThe list is empty.")
                sleep(0.5)
                return
            else:
                search_fname = input("Enter contact's first name: ")
                search_lname = input("Enter contact's last name: ")
                found = False
                for i in range(len(df)):
                    if df.iloc[i, 0] == search_fname:
                        if df.iloc[i, 1] == search_lname:
                            self.found = True
                            sleep(0.5)
                            print("\nContact found...\n")
                            select_edit = input("Select item to edit: "
                                                "\n\n'1' - First Name"
                                                "\n'2', Last Name"
                                                "\n'3' - Phone Number"
                                                "\n\nEnter your choice: ")
                            if select_edit == '1':
                                df.iloc[i, 0] = input("Update first name: ")
                            if select_edit == '2':
                                df.iloc[i, 1] = input("Update last name: ")
                            if select_edit == '3':
                                df.iloc[i, 2] = input("Update phone number: ")
                            sleep(0.5)
                            print("\n\nUpdated Details:",
                                  "\nFull Name:", df.iloc[i][0], df.iloc[i][1],
                                  "\nPhone Number:", df.iloc[i][2])
                            with open('contacts.json', 'w') as file:
                                df.to_json(file)
                                sleep(1)
                                return

                if not found:
                    sleep(0.5)
                    print("\nContact not in list.")
                    sleep(0.5)
                    return

    def delete_contact(self):

        with open('contacts.json', 'r+') as file:
            df = pd.read_json(file)
            search_fname = input("\nEnter contact's first name: ")
            search_lname = input("Enter contact's last name: ")
            found = False
            for i in range(len(df)):
                if df.iloc[i, 0] == search_fname:
                    if df.iloc[i, 1] == search_lname:
                        self.found = True
                        print("\nContact found...\n")
                        name = (df.iloc[i, 0], df.iloc[i, 1])
                        contact_index = df.index[df['First Name'] == df.iloc[i, 0]].values
                        delete = input('Are you sure you want to delete'
                                       +str(name)+"?\n'Y' - Detele\n'N' - Return"
                                                  "\nEnter your choice: ")
                        if delete == 'Y':
                            df.drop([int(contact_index)], axis=0, inplace=True)

                        with open('contacts.json', 'w') as file:
                            df.to_json(file)
                            print(df)
            if not found:
                sleep(0.5)
                print("\nContact not in list.")
                sleep(0.5)
                return

    def reset_contacts(self):
        self.contacts = {}
        with open('contacts.json', 'a') as file:
            json.dumps(self.contacts)
        with open('contacts.json', 'r+') as file:
            df = pd.read_json(file)
            df.columns = ['First Name', 'Last Name', 'Phone Number']
            df = pd.DataFrame(columns=df.columns)

        with open('contacts.json', 'w+') as file:
            df.to_json(file)
            if df.empty:
                sleep(0.5)
                print("\nThe list is clear.")
                sleep(0.5)

        return


def menu():
    select = input("\nWelcome!\n"
                   "\n'1' - Display contacts"
                   "\n'2' - Add Contact"
                   "\n'3' - Search Contact"
                   "\n'4' - Update Contact"
                   "\n'5' - Delete Contact"
                   "\n'6' - Reset Contact List"
                   "\n'7' - Exit Program"
                   "\n\nEnter your choice: ")
    if select == '1':
        Contacts.display_contacts()
    if select == '2':
        Contacts. add_contacts()
    if select == '3':
        Contacts.search_contact()
    if select == '4':
        Contacts.update_contact()
    if select == '5':
        Contacts.delete_contact()
    if select == '6':
        Contacts.reset_contacts()
    if select == '7':
        return False
    return True


Contacts = Contacts()
while menu():
    pass



