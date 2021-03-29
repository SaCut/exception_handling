# try:
#     file = open("orders.txt")
#     print("File opened")
# except FileNotFoundError as err:
#     raise(f"the above block of code was not executed {err}")
# finally:
# 	print("thank you for your cohoperation")

# # second iteration
# # your task is to read the data and display as a list
# try:
# 	with open("orders.txt", 'r') as file: # we try to open the file in readonly mode
# 		for i in file: # for each line in the file
# 			print(i) # print the line
# except Exception as e: # in case any error happens
# 	print(e) # print the error
# finally:
# 	print("\nthe code run fine\n") # then let the user know that the execution is done

# third iteration
try:
	with open("orders.txt", 'w') as file: # we open the file in write mode

		file.write("\ncheescake") # we write a new line in the file

		for i in file: # we print the contents to check if everything worked fine
			print(i)

except Exception as e: # in case any error happens
	print(e) # print the error
finally:
	print("\nthe code run fine\n") # then let the user know that the execution is done