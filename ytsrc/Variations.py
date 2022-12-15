# https://www.youtube.com/shorts/lhj4VD96Jg0
# https://vimsky.com/zh-tw/examples/usage/python-math-comb-method.html
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.comb.html

# Player must select 3 skills
# pip install scipy
import math
from scipy.special import comb


skills = [
    'Farming',
    'Mining',
    'Crafting',
    'Healing',
    'Melee',
    'Archery',
    'Alchemy',
    'Stealth',
    'Persuasion',
    'Mobility'
]
# Total number of character variations?
num_skills = len(skills)
# variations = math.comb(num_skills, 3)  # Python 3.8
variations = comb(num_skills, 3)
print(variations)