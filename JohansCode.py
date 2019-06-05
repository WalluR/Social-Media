p_length = ""
delimiter = "¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-¦-"
Final_list = []

with open('NEWwysiwyg_cie_LLLL2_LLLL2_w_.txt', 'r') as file:
    interface_used = file.read().replace('\n', '')
    interface_used = interface_used.replace('Â', '')
    interface_used = [x + delimiter for x in interface_used.split(delimiter, 1) if x ]
    for p in interface_used: print(len(p)), print(p),