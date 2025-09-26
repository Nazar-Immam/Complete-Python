#FILE HANDLING IN PYTHON

#To open any file, we just write open(), by this we can also create files,


# file = open("order.txt", "w")
# try:
#     file.write("This is a file made from another file using open keyword, and text is written using w ")
# finally:
#     file.close()


#whenever we'll run the above code , a file would be created of name order.txt

# but in modern python, we can handle files with just one keyword, that automatically wraps it in try except,
# ie, with

with open("order.txt","w") as file:
    file.write("New way of writing in file")


# with keyword used everywhere also , 
#with - is a context manager ,its something that sets things up, lets you use them, 
# and then automatically cleans them up (like closing files, sessions, or network connections).
# By using with, you don't care about opened sessions or opened files, after the work is done
# 'with' closses the file, end the session automatically, no need for manual closing, and it's very great