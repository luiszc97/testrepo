def import_and_crate_dictionary(filename):
    """This function is used to create an expense dictionary from a file
    Every line in the file should be in the format:
        key, value
    The key is a user's name and the value is an expense the user
    total expense with.
    The value should be anumber, however, it sis possible that there is no value,
    that the value is an invalid number, or that the entire line is blank."""

    #create empty dictionary
    expenses = {}

    #open file in read mode and read all lines into a list
    f = open(filename, 'r')
    lines = f.readlines()

    for line in lines:
        #strips whitespace from beginning and end of line
        #split into a list based on coma separator
        lst = line.strip().split(',')

        #skip line if mising value(expense amount)
        if len(lst) <= 1:
            continue

        #Get key(name) and value(expense amount) from list
        key = lst[0].strip()
        value = lst[1].strip()

        try:
            #cast value to float
            value = float(value)

            #add new expense amount to current total expense amount
            #associated with key (name), or
            #associate the new total expense amount with key(name)
            expenses[key] = expenses.get(key, 0) + value
        except:
            #otherwise go to of for loop, to next line in list of lines.
            continue

    f.close()

    return expenses

def main():
    expenses = import_and_crate_dictionary('expenses.txt')
    print('expenses:', expenses)

if __name__ == '__main__':
    main()

