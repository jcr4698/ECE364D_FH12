import re

txt = "Have you anything ever had a dream that you, um, you had, your, you- you could, " \
        "you’ll do, you- you wants, you, you could do so, you- you’ll do, you could- " \
        "you, you want, you want him to do you so much you could do anything?"

x = re.findall(".*,", txt)
print(x)