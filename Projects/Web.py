import webbrowser, sys

query = "".join(sys.argv[1:])
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(query)