#WAP to Create duplicate of existing list (not same reference)

li = [10, 20, 30]
copy_li = []

for i in li:
    copy_li.append(i)

print("Original list:", li)
print("Duplicate list:", copy_li)
