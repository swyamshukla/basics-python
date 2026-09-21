options={
    "rock": "Rock crushes scissors",
    "paper": "Paper covers rock",
    "scissors": "Scissors cut paper" ,
    "rock" : "Rock crushes",
}

for key in options:
    print(key, ":", options[key])

for key in options.keys():
    print(key, ":", options[key])


for value in options.values():
    print(value)


for key, value in options.items():
    print(key, ":", value)

