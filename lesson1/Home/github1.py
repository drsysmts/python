number = 23
number1 = 34
sum = number + number1
mul=number*number1
sus=number1-number
print(sum,mul,sus)
#code work good
caution={1:"name",2:"age"}  #dic
print("local333")

text = "abc abc                   "
text = text.lower()
counter = {}
for ch in text:
    if ch not in counter:
        counter[ch] = 1
    else:
        counter[ch] += 1

print(counter.items())
