
"""
# You do not want your test case to stop
# and you can print the failure as well!
"""

try:
    with open("test1.txt", 'r') as file:
        file.readlines()
   
except Exception as e:
    print(e)
    # print("here is a failure here!")

finally:
    print("running whenever it passes or error!")
