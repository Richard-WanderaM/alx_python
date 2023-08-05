def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg) 

test_var_args('yasoob','python','eggs','test')

# *args and **kwargs are mostly used in function definitions
# # *args and **kwargs allow you to pass a variable number of arguments to a function
# variable means here is that you do not know before hand that how many arguments can be passed;
# to your function by the user so in this case you use these two keywords. 
# # *args is used to send a non-keyworded variable length argument list to the function.
