# Group Exercise - Revenge of the Contact Card

Given everything we've learned in python we've seen that there's many ways to write software.  We're going to revisit the contact card.  This time our requirements are a bit more strict.

## The model

1. You will use a `class` for your contact card.
2. You will use a `class` for storing multiple contact cards called `AddressBook`.
3. You will create methods to create, read, update and delete a contact card from an address book.
4. You must create a method to allow search on last name (starts with...)
5. You will create an `export_to_csv` and `export_to_json` method
6. You will create an `import_from_csv` and `import_from_json`.
7. You will receive a file with 1000 contacts.  You must load these and demonstrate search.

An example row of the input is:

```json
{"first_name":"Naoma","last_name":"Eidler","email":"neidlerrr@ted.com","phone":"228-805-9162","address":"922 Clyde Gallagher Plaza","city":"LAS VEGAS","state":"MS","zip":"39505"}
```

Note: Do not worry about menus.  Simply just either `assert` or  look at your output to validate the program works correctly.

