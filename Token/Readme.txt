__init__.py
Contains a decorator wrapper
Ensures that a user's JWT is valid
Ensures they have the required permissions to perform any requested functions
If permitted, returns the user id for calling functions to use

jwt.py
make_jwt() creates the token using the user id, with a 2 hour expiration
check_jwt() confirms a token is valid

perms.py
Uses the user id to check if that user has the required permissions to perform any requested actions