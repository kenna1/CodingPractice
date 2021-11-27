import webbrowser

# Search through on google
query = input("Input your query: ")
webbrowser.open("https://google.com/search?q=%s" % query)

# Open a search result 