import os
import sys
import unittest

# Add the parent directory to the system path to import the main code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ContactsManager import (
    Table_nom, Table_prenom, Table_tele, Table_gmail,
    sauvegard_contacts, output_file_path
)

class TestContactsManager(unittest.TestCase):

    def setUp(self):
        # Clear all tables before each test
        Table_nom.clear()
        Table_prenom.clear()
        Table_tele.clear()
        Table_gmail.clear()

        # Insert a sample contact
        self.sample_contact = {
            "last_name": "DOE",
            "first_name": "John",
            "phone": "0612345678",
            "email": "john.doe@gmail.com"
        }

        Table_nom.append(self.sample_contact["last_name"])
        Table_prenom.append(self.sample_contact["first_name"])
        Table_tele.append(self.sample_contact["phone"])
        Table_gmail.append(self.sample_contact["email"])
        global profil_num
        profil_num = 0

    def test_contact_saved_to_file(self):
        # Save contacts to the output file
        sauvegard_contacts()

        # Check if the file was created
        self.assertTrue(os.path.exists(output_file_path))

        # Check if the file contains the contact
        with open(output_file_path, "r") as file:
            content = file.read()
            for value in self.sample_contact.values():
                self.assertIn(value, content)

    def tearDown(self):
        # Clean up the output file
        if os.path.exists(output_file_path):
            os.remove(output_file_path)

if __name__ == '__main__':
    unittest.main()