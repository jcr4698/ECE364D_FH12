# Inline Test # 1
# Senior Design Project - FH12
# Author: Jan C. Rubio
# Date: 1/25/23

import sys
import re
from inline import Here

input_list = sys.argv[1:]

# String to "tokenize"
txt = "Have you anything ever had a dream that you, um, you had, your, you- you could, " \
    "you’ll do, you- you wants, you, you could do so, you- you’ll do, you could- " \
    "you, you want, you want him to do you so much you could do anything?"

# parse string
res = re.findall(r"[- ’A-Za-z]*,|[- ’A-Za-z]*\?", txt)
idx = 0
for tok in res:
	tok = tok.replace(",", "")
	res[idx] = tok
	idx += 1

# answer
ans = txt.split(",")

# verify
Here().given(input_list, txt).check_eq(res, ans)