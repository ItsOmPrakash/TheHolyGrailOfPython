# In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
# See developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types for common types.

#--------------------------------------------------------------
# Taking user's file name as input
userInput = input("What do you want name your file ?? \n : ")
# To remove any whitespaces and to make code consistent
userInput = userInput.strip().lower()


match userInput :
    case name if userInput.endswith(".pdf"):
        print("application/pdf")
    case name if userInput.endswith(".gif"):
        print("image/gif")
    case name if userInput.endswith(".jpg"):
        print("image/jpeg")
    case name if userInput.endswith(".jpeg"):
        print("image/jpeg")
    case name if userInput.endswith(".png"):
        print("image/png")
    case name if userInput.endswith(".txt"):
        print("text/plain")
    case name if userInput.endswith(".zip"):
        print("application/zip")
    case _ :
        print("application/octet-stream")




