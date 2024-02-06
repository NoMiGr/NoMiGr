
n=input()
lst=n.split()
lst=[int(i) for i in lst]
lst.sort()
print(*lst)
lst.sort(reverse=True)
print(*lst)