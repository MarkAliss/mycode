challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# eyes
a= challenge[2][1] 

# goggles
b= challenge[2][0]

# nothing
c= challenge[3]

print(f'My {a}! The {b} do {c}!')


# eyes
aa= trial[2]['goggles']

# goggles
bb= trial[2]['eyes']

# nothing
cc= trial[3]

print(f'My {aa}! The {bb} do {cc}!')



# eyes
aaa= nightmare[0]['user']['name']['first']

# goggles
bbb= nightmare[0]['kumquat']

# nothing
ccc= nightmare[0]['d']

print(f'My {aaa}! The {bbb} do {ccc}!')
