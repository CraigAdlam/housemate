# ![Travis CI Build Stamp](https://app.travis-ci.com/CraigAdlam/housemate.svg?branch=main "Travis CI Build Stamp") [![PyPi Link](img/pypi_logo_small3.png)](https://pypi.org/project/housemate/2.5/) [![Coverage Report](img/coverage_slim4.png)](#coverage-report)

# HouseMate
### The HouseMate app shows users different properties to rent or purchase based on their specific needs.

## Housemate Video  
[![HouseMate Video](img/housemate_picture.png)](https://drive.google.com/file/d/12ogu1G4d1A6hkvmxftLqHi-QRhryyvsX/view?usp=drive_link "HouseMate Video") 
## Commands from the Video:
- `pip install housemate` - installs housemate package to local python directories (e.g., c:\users\user1\anaconda3\lib\site-packages\)
- `pip show housemate` - shows the application name, current version installed, summary, authors, and installation location
- `python -m housemate_app.housemate_main` - executes the main file in the housemate package to guide you through the menus

The HouseMate package has 2 sub-packages, which are user and property. The user sub-package contains 3 modules; userprofile.py, userlogin.py and security.py, while the property sub-package also contains 3 modules; property.py, purchase.py and rental.py. Finally, there is a standalone module called housemate.py which imports all the modules and houses the logic to make the various menus and functions flow correctly. 

```
housemate/
├── __init__.py
├── housemate_test_suite.py
├── src/
│   ├── __init__.py
│   └── housemate_app/
│       ├── __init__.py
│       ├── housemate_main.py
│       ├── user/
│       │   ├── __init__.py
│       │   ├── userprofile.py
│       │   ├── userlogin.py
│       │   └── security.py
│       └── my_property/
│           ├── __init__.py
│           ├── property.py
│           ├── purchase.py
│           └── rental.py
└── tests/
    ├── __init__.py
    ├── test_housemate.py
    ├── test_userprofile.py
    ├── test_userlogin.py
    ├── test_security.py
    ├── test_purchase.py
    └── test_rental.py   
```

## Sub-Package: Property
#### property.py 
Contains the superclass Property, which instantiates various attributes for all inherited property types. 
Attributes include: 
- sqft (the amount of square footage)
- num_beds (number of bedrooms)
- num_baths (the number of bathrooms)

#### purchase.py
Contains the subclass Purchase, which inherits from Property. Purchase functions to instantiate additional attributes that pertain to all Purchase-type objects. 
Attributes include: 
- price (the cost of acquiring the property)
- mortgage_term (the number of years on the mortgage)
- interest (the interest rate factored into the mortgage calculation)

Purchase contains 2 methods:
- `calculate_mortgage` -- uses Purchase-type attributes and user input to calculate a suitable mortgage for any type of Purchase property.
- `display` -- An overview of the object's attributes with informative print statements and all calculations in one place

Purchase contains 3 functions: 
- `gen_purchase` -- generates n amount (user controlled) of Purchase-type properties in a list
- `purchase_recommendation` -- considers user parameters, such as downpayment, income and home preferences in order to match the user with Purchase properties that fit their specifications
- `view_purchase_list` -- backgruond function that facilitates easy viewing of the recommendation list, along with some quality-of-life display enhancements for user satisfaction. 

Finally, purchase.py also contains 6 subclasses, all of which inherit from Purchase. These subclasses each align with a different type of Purchase-property, which are differentiated by randomly generating their attributes within finely-tuned numerical ranges. This is done by setting their attribute values to random.randint(x, y) in each subclass __init__ call, so the objects are automatically randomized (within a range) as they are created. 
Subclasses of Purchase: 
- Condo
- TownHome
- Duplex
- Bungalow
- TwoStory
- Mansion

#### rental.py
Contains the subclass Rental, which inherits from Property. Rental functions to instantiate additional attributes that pertain to all Rental-type objects. 
Attributes include: 
- rent (the base cost per month for this property)
- utilities (expenses often required for renting individuals by landlords) 
- lease_term (the length of months that the lease agreenment is good for)
- pet (whether or not a pet is present in the Rental unit, which will require a pet deposit)

Rental contains 2 methods: 
- `calc_total_rent` -- calculates total rent based on rent, utilities and lease term
- `display_rental` -- an overview of the object's attributes with informative print statements and all calculations in one place

Rental contains 3 functions:
- `gen_rental` -- generates n amount (user controlled) of Rental-type properties in a list
- `rental_recommendation` -- considers user parameters, such as income and home preferences in order to match the user with Rental properties that fit their specifications
- `view_rental_list` -- backgruond function that facilitates easy viewing of the recommendation list, along with some quality-of-life display enhancements for user satisfaction. 

Finally, rental.py also contains 6 subclasses, all of which inherit from Rental. These subclasses each align with a different type of Rental-property, which are differentiated by randomly generating their attributes within finely-tuned numerical ranges. This is done by setting their attribute values to random.randint(x, y) in each subclass __init__ call, so the objects are automatically randomized (within a range) as they are created. 
Subclasses of Rental: 
- RentalCondo
- RentalTownHome
- RentalDuplex
- RentalBungalow
- RentalTwoStory
- RentalMansion

## Sub-Package: User
#### userprofile.py
The userprofile.py module allows the user to create their profile by entering their name, age and email, as well as their chosen username and password. The username and password are encrypted using a hash function (from security.py) in order to be stored as a hash value for privacy and security reasons. There is a class UserProfile that instantiates each of the attributes (i.e, name, age etc.) and allows for retrieval from secure storage in the .csv file. 
 
- `load_user_profiles` -- loads the user profiles - stored in the `user_profiles.csv` file locally - if there is no `file_path` to the file, none will be returned
- `create_profile_from_input` -- creates a profile for the user based on user input with the following restrictions:
    - name -- must be between 11 and 133 characters and contain no spaces
    - age_input -- must be between 11 and 133 and an integer only
    - email -- must be alphanumeric characters before the @ symbol as well as in between @ and .com
    - username -- must be between 8 and 33 characters and contain no spaces
    - password -- must be between 8 and 133 characters and contain no spaces
- `append_to_dataframe` -- adds the user's profile information into a dataframe - if there is no dataframe, one is created
- `save_dataframe_to_csv` -- saves the dataframe into the `user_profiles.csv` file located in the current working directory
 
#### userlogin.py
This module allows the user to login with their created credentials by entering their username and password. These credentials are then encrypted with a hash function to be matched with the hash values that were stored after creating the profile. 
 
- `login_get_file_path` -- determines the `file_path` to save the `user_profiles.csv` file for storage
- `view_profile` -- allows the user to view their profile information - username and password are displayed as hash values
- `edit_profile` -- allows the user to edit their profile - must re-login if the username or password are changed
- `delete_profile` -- allows the user to delete their profile completely - exited from the profile menu to the main menu

#### security.py
The security.py module ensures that the sensitive user attributes, such as username and password, are encrypted using a hash function for storage and validating credentials when logging in.
 
- `string_hash` -- converts username and password into hash values with the use of a custom hash function for encryption
- `reverse_hash` -- converts hashed values for username and password back into the original string - for forgotten usernames or passwords
- `check_credentials` -- validates login credentials with the hash values stored in the `user_profiles.csv` file

## Standalone Module: 
#### housemate.py
This module imports from both Property and User sub-packages, and acts as a staging ground for the HouseMate application as a whole. This module mainly does this through housing the multitude of menus required, gathering functions and allowing them to work in concert. 
Main functionalities include: 
- Menu management and control of flow, applies to: 
  - user profile functionalities
  - authentication 
  - property viewing
  - property recommendations
 
There are many functions within housemate.py that control the flow including: 
- Menu functions: allow for users to select options based on prompts
   - `main_menu`, `profile_menu`, `housemate_menu`
- Mapping functions: allows for user-friendly input 
   - `purchase_main`, `rental_main`, `purchase_recommendation_main`, `rental_recommendation_main`

## Coverage Report <a name="coverage-report"></a> 
![Coverage Screenshot](img/coverage_full.png)
