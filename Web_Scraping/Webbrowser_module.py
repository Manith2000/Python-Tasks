import webbrowser, sys, pyperclip

#Launch google map for a particular address on website

sys.argv #[''] all CLI arguments are in a list

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:]) #joins to singled string value
else:
    #this assumes user gets address from clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

#this needs to be in form of a BAT file to be launched within cmd
