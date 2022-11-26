import webbrowser, sys, pyperclip

if len(sys.argv)>2:
    webbrowser.open("https://www.google.com/maps/place/"+sys.argv[1])
else:
    place = pyperclip.paste()
    webbrowser.open("https://www.google.com/maps/place/"+place)