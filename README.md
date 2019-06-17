# Password_Locker

## Built By [gkarumba](https://github.com/gkarumba/)

## Description
Password_Locker is an amazing terminal run python application that will help users manage their passwords and even generate new passwords for their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account
* find my Credentials account by name

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display welcome message | **In terminal: $./run.py** | Welcome to the app |
| Display prompt for creating an account | Enter: Username & password | Enter your Username and password |
| Display codes for navigation | Successful login | Choose an option: ca - Create Credential Account, da - Display Credentials Account, fa - Find Credential Account, cc -copy the password, ex - exit | 
| Display prompt for creating a credential | **Enter: ca** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: da** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: cc** | Enter the site name of the credential you wish to copy. |
| Display prompt for which credential to find | **Enter: fa** | Enter the site name of the credential you wish to find. | 
| Exit application | **Enter: ex** | Exit the current navigation stage |

## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip


### Cloning
* In your terminal:
        
        $ git clone  https://github.com/gkarumba/Password_Locker.git
        $ cd Password-Locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x run.py
        $ ./run.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 user_tests.py
        
## Technologies Used
* Python3.6

## License
MIT &copy;2019 [gkarumba](https://github.com/gkarumba/Password_Locker/blob/master/LICENSE)

