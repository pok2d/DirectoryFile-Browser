import os
# Just starting description, gives instructions to the user.
print("Welcome to the directory/file/folder lister! We start at your home.")
print("Put the number of a file/place to go there. You can't go to files, and you can always go back to a past "
      "directory with 'back'.")

# Starts at /home directory
currentdirectory = '/home'
currentitemline = ''

# Main program loop
while True:
    try:
        # This attempts to make a list with all the items in a directory.
        # If it was a file selected lastly, it will create an error.
        currentitems = os.listdir(currentdirectory)
    except:
        # This block runs if it was a file selected earlier, and will inform the user it was a file.
        # It will also delete the recent file of our directory path, so they go back to the directory
        # that they were just in.imp
        print('Hey! That aint a directory!')
        currentdirectory = currentdirectory[0:currentdirectory.rfind('/')]
    # This for loop creates the format with 5 (or less) files/directories on each line with a number
    # corresponding for each.
    for item in currentitems:
        # This adds on our current string (with the max 5 locations), by tacking on our new location's
        # location on the currenitems list (which is a number), then stick it between brackets and also
        # show which item this number is.
        currentitemline = currentitemline + ('[' + str((currentitems.index(item))+1) + '] ' + item + '   ')
        # This is the system so for every 5 locations added to our currentitemline, it will print it
        # and start a new one (reset it).
        if ((currentitems.index(item) + 1) % 5) == 0:
            print(currentitemline)
            currentitemline = ''
        # If we have a directory with less than 5 locations, this makes sure it will still print if it
        # sees there are no more actual locations to print, even if it doesn't reach 5 terms.
        elif (currentitems[-1]) == item:
            print(currentitemline)
    # Resets currentitemline, so when we go to a new directory we're not adding onto old terms.
    currentitemline = ''
    # Input for where user wants to go next.
    newplacenum = input('Where u wanna go: ')
    # Detection if user wants to go back.
    if newplacenum == 'back':
        # This statement checks if the current path is only one term, which would be /home. If it is, it denies
        # the back statement, as there is no place to go back to.
        if currentdirectory.count('/') == 1:
            print('ya cant go back!')
            continue
        # Otherwise, if it is okay to go back, it will make the new path starting from the first character
        # to the last slash, essentially cutting of the last term of our path.
        currentdirectory = currentdirectory[0:currentdirectory.rfind('/')]
    # This is the else statement if the user doesn't want to go back. This hopefully means they have
    # inputed a number to a directory.
    elif newplacenum == 'TicTacToe':
        os.chdir('/home/pok/PycharmProjects/TicTacToe/TicTacToe-Version1-Pygame/')
        os.system('python3 main.py')
    elif newplacenum == 'Pyraph':
        os.chdir('/home/pok/PycharmProjects/Pyraph/PyraphCalculator/')
        os.system('python3 main.py')
    elif newplacenum == 'Inception':
        os.chdir('/home/pok/PycharmProjects/FileBrowser/DirectoryFile-Browser/')
        os.system('python3 FileBrowser.py')
    else:
        # Here it will try to take their input and make it as an integer, and then use it to get the
        # item corresponding to that number with the currentitems list.
        try:
            # It takes this new place, from the currentitems list, and adds it onto the end of our
            # current path.
            newplace = currentitems[int(newplacenum) - 1]
            currentdirectory = currentdirectory + '/' + newplace
        # If this fails, due to them not putting in a valid integer or maybe not even an integer at all,
        # it will then just go back to the beginning print the path options and again and do a new input.
        except:
            print('Not a valid number bro')
            print(currentdirectory)
