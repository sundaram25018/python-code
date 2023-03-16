# f = open('file.txt')
# t = f.read()
# if 'Twinkle' in t:
#     print("Twinkle is present")
# else:
#     print("Twinkle is not present")
# f.close()

# for i in range(2,21):
#     with  open(f"/Multiplication_table_of_{i}", 'w') as f:
#         for j in range(1,11):
#             f.write(f"{i}X{j}={i*j}\n")
#     break 

# with open("file.txt") as f:
#     content = f.read()


# content = content.replace("Twinkle", "########")
# with open("file.txt",'w') as f:
#     f.write(content)
words = ["twinkle", "Twinkle", "star"]
with open("file.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "########")
    with open("file.txt",'w') as f:
        f.write(content)
