"""Generate sales report showing total melons each salesperson sold."""

# create two list to store salesperson's name and the quantity of melons sold.
salespeople = []
melons_sold = []

# variable to open the file
f = open('sales-report.txt')
#  a for loop to iterate through the file
for line in f:
    # rstrip() to remove any white space at the end of the string
    line = line.rstrip()
    # split the words at "|" and save it to a new list called entries
    entries = line.split('|')

    salesperson = entries[0] # get a name of salesperson (first index)
    melons = int(entries[2]) # the number of melons they have sold.


    # if the salesperson is in the list (salespeople) then increment the number of melons
    if salesperson in salespeople:
        # find the index position stored in salesperson
        position = salespeople.index(salesperson)
        melons_sold[position] += melons

        # if not, add salesperson to salespeople
        # and melons to melons_sold
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# loop through the list salespeople and use the index into salespeople and melons_sold
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')