
study =list()


while True:
    inp= input("Question :")
    if inp == "exit":
        break
    study.append(inp)

for key, value in enumerate(study,start=1):
    print(f"Question {key}: {value} ") 


