from importlib.resources import contents


text=input()

with open("output.txt","w") as file:
    file.write(text)
    file.close()
print(file)
