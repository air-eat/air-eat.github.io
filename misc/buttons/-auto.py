# auto add buttons to button.html
import random
from os import listdir
html = '<html>\n<head><link rel="stylesheet" href="styles.css"></head>\n<body>\n'
buttons = listdir("./air-eat.github.io/misc/buttons")
blocked = ['rickroll.gif', '-auto.py', 'ssnow2.gif']
for block in blocked:
    buttons.remove(block)
ranitem = 0
items = len(buttons)

while buttons != []:
    items = len(buttons)
    ranitem = random.randint(1, items) - 1
    html += '<img src="misc/buttons/' + buttons[ranitem] + '" width=88px height=33px> \n'
    buttons.pop(ranitem)

# add link to source and end
html += '<a href="https://cyber.dabamos.de/88x31" style="background-color:rgb(22, 22, 22)">buttons from cyber.dabamos.de/88x31</a>\n</body>\n</head>'

file = open("./air-eat.github.io/button.html", "w")
file.write(html)
file.close()

# rickroll i manually add later
'<a target="_blank" href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="misc/buttons/rickroll.gif" width=88px height=33px></a>' 