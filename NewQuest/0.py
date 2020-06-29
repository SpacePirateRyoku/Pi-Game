list = ['kumar','satheesh','rajan']    
BOLD = '\033[1m'

for i, item in enumerate(list):
   list[i] = BOLD + item

print (list)
