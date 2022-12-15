# https://www.youtube.com/shorts/iT1jhA-Y6uU
# sort inventory based on rarity dictionary
inventory = ['Axe', 'Great Sword', 'Stick']

rarity = {
    'Great Sword': 98,
    'Golden Bow': 97,
    'Iron Sword': 80,
    'Axe': 34,
    'Stick': 1
}

sort_inv = sorted(inventory,
                  key=rarity.__getitem__,
                  reverse=True)
print(sort_inv)
print(rarity.__getitem__('Stick'))