phone=input('Phone: ')
dig={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output=""
for ch in phone:
    output+=dig.get(ch,"!")+" "
print(output)

message=input(">")
words=message.split(' ')
print(words)
