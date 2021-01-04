
"""
# You do not want your test case to stop
# and you can print the failure as well!
"""


try:
    with open("test1.txt", 'r') as file:
        file.readlines()
   
except:
    print("Some how there is a failure in try long !")
    