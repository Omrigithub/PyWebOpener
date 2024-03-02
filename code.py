import webbrowser

# link amount
link_amount = int(input("Enter amount of links to open: "))

for i in range(link_amount):
    web_links = input(f'enter link number #{i+1}: ')
    webbrowser.open(web_links)
