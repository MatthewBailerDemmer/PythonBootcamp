import os
with open("/my_file.txt") as file:
    contents = file.read()
    print(contents)
    # That way it closes directly
    #file.close() # We have to close it because it takes computer resources
    # And it can close unexpectedly

with open("/my_file.txt", mode="a") as file:
    file.write("\nNew text.")

with open("new_file.txt", mode="a") as file:
    file.write("\nNew text.")

#if you try to open a file that does´nt exist
#pyhton will create a new one for you if the mode is "a" and "w"

#It doesn´t work if the directory changes

#to get it from a different drive
with open("../../my_file.txt", "a") as file:
    file.write("\nGot it")