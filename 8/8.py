

#input_str = input()
input_str = "without,hello,bag,world"
items=[x for x in input_str.split(',')]
items.sort()
print (','.join(items))