#sets in python
#we write sets with these { }

num1 = {1,2,3,4,4,99}
num2 = {4,6,8,9,6,3}
num3 = {2,4,87,97,5}

#union '|' , combines only unqiue values
union = num1 | num2 | num3
print(union)

#intersection , '&' , finds the common values
common = num1 & num2 & num3
print(common)

#only in one , '-'
onlyINnum1 = num1 - num2 - num3
print(onlyINnum1)

#membership test
print({'3' in num1})