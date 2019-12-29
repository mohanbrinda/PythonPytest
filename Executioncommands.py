# Execute the test.py file

pytest test.py

#USING OPTIONS WITH PYTEST

#Execute the test.py file with -v(verbose option)

pytest test.py -v

#Change the name of the test.py file to tes.py and execute the program

pytest tes.py

#Execute test_add() function from the test.py file USING ::add option

pytest test.py::test.add()

#Execute only the functions in test.py file using -k option containing the word "add"

pytest -v -k "add"

#Execute only the functions in test.py file with -k option containing the word "add" or "string"

pytest -v -k "add or string"

#Execute only the functions in test.py file with -k option containing the word "add" and "string"

pytest -v -k "add and string"

#Mark the number functions and string function in test.py file with the following code before usig option "m"
@pytest.mark.number

#Execute only the functions in test.py file with -m option number
pytest -v -m number # will display number functions in test.py file

#Mark the number functions and string function in test.py file with the following code before usig option "m"
@pytest.mark.strings

#Execute only the functions in test.py file with -m option strings
pytest -v -m strings # will display strings functions in test.py file

#Execute test.py file with -x option
#the program will exit when it encounters first failure
pytest -v -x

#Execute test.py file with -tb=no option without the error option without stack trace
#the program will exit when it encounters first failure
pytest -v -x --tb=no

#Execute test.py file with --maxfile=2 option
pytest -v --maxfail=2

#Execute test.py file with skip option in order to skip a function in te test.py file
#add the following code to the test file 
@pytest.mark.skip(reason="skipping the test_add function")

pytest -v