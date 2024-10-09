def goo():
    return "this is return string from goo() in test module"

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("this print statement came from test module")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__": #false if this file imported as module
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("this CONDITIONAL print statement came from test module")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#"this CONDITIONAL print statement came from test module" will not be displayed because this is being imported as module (so _name_=="main" will be false)
# "this print statement came from test module" will always print