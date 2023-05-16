""" Searches for a number input by the user among the decimals of pi. """

with open("pi-million.txt", "r") as pi_file:
    pi = pi_file.read()

number_to_search = input("What number would you like to search for? ")

# Check if input number doesn't have more digits than the decimals of the pi from the file.
if len(number_to_search) > len(pi)-2:   
    print("The number you chose is too big\n")
    exit()

found = 0   # Boolean that stores if the number has been found.
for i in range(2,len(pi)-(len(number_to_search)-1)):
    if number_to_search == pi[i : i + len(number_to_search)]:
        print("The number has been found from the decimal {} to the decimal {}".format(i, i+len(number_to_search)-1))
        found = 1

if found == 0:
    print("The input number hasn't been found.")

print("The program has finished")   
