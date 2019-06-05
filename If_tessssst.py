
'''
print('hej')

print('detta kanske fungerar ååå')


x = 2

if x < 3:
    print(x)
'''



with open('wysiwyg_cie_LLLL1_s3429075_s_.txt', 'r') as file:
    person1 = file.read().replace('\n', '')
    person1 = person1.replace('Â', '')
#print(person1)

p_length = ""

with open('wysiwyg_cie_LLLL1_s3429075_o_s3912728.txt', 'r') as file:
    person2 = file.read().replace('\n', '')
    person2 = person2.replace('Â', '')
    person2 = person2.split("/¦s")
#for p in person2 : p_length = len(p), print(p_length), print(p)


'''
with open('wysiwyg_cie_LLLL1_s3429075_t_.txt', 'r') as file:
    time_person1 = file.read().replace('\n', '')
    time_person1 = time_person1.replace('Â', '')
print(time_person1)

with open('wysiwyg_cie_RRRR1_s3912728_t_.txt', 'r') as file:
    time_person2 = file.read().replace('\n', '')
    time_person2 = time_person2.replace('Â', '')
print(time_person2)
'''

#Wiljam code

with open('wysiwyg_cie_LLLL1_s3429075_s_.txt', 'r') as file:
    data1 = file.read()

with open('wysiwyg_cie_LLLL1_s3429075_o_s3912728.txt', 'r') as file:
    data2 = file.read()


with open('wysiwyg_cie_LLLL1_s3429075_t_.txt', 'r') as file:
    time = file.read()


print(data1)

print(data1.index('/¦s'))
#lets use this a an pratice
print(data2.index('/¦s'))

print(data2[0:20])
print(data1[0:20])

print("time data", time[7:27])

print(time[7:27])


#actual conversation

#print(data2.find('/¦¦s', 21))

# data1 has no '/¦¦s' but data 2 has


#so 725 is when the conversation ends actually it is 359

print(data2[21:359])
print(data1[21:359])

# test 3 conversation

convA2 = data2[359:728]
convB2 = data1[359:728]

conA2 = convA2.replace('¦',' ')
conB2 = convB2.replace('¦',' ')

print(conA2)
print(conB2)


#def seperate(data)








