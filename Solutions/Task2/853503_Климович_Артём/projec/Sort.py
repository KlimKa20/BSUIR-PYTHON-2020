import tempfile
import os


def merge_sort_file1(files_open, file_write):
    mass_of_files = list()
    file_write_open = open(file_write, 'w')
    for file in files_open:
        mass_of_files.append(open(file, 'r'))
    numbers = list()
    for line in mass_of_files:
        numbers.append(line.readline())
    while numbers:
        temp = str(min(numbers, key=lambda i: int(i)))
        file_write_open.write(temp)
        index = numbers.index(temp)
        numbers[index] = mass_of_files[index].readline()
        if numbers[index] == '':
            numbers.pop(index)
            mass_of_files[index].close()
            mass_of_files.pop(index)
    file_write_open.close()


def sort(file_list):
    with open('numbers.txt', "r") as file_handler:
        number_of_num = 100000
        count_of_file = 0
        temper = tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt')
        temp = list()
        name_of_file = list()
        for line in file_handler:
            temp.append(line)
            if len(temp) + 1 > number_of_num:
                temp.sort(key=lambda i: int(i))
                for line in temp:
                    temper.write(line)
                name_of_file.append(temper.name)
                temper.close()
                temp.clear()
                temper = tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt')
                print(count_of_file)
                count_of_file += 1

        if temp:
            temp.sort(key=lambda i: int(i))
            for line in temp:
                temper.write(line)
            name_of_file.append(temper.name)
            temper.close()

    variable_of_slice = 2
    for file in name_of_file:
        file_list.append(file)
    while len(name_of_file) > 1:
        new_temper = tempfile.NamedTemporaryFile('w', delete=False, suffix='.txt')
        file_list.append(new_temper.name)
        if len(name_of_file) > variable_of_slice:
            merge_sort_file1(name_of_file[:variable_of_slice], new_temper.name)
            for delet in name_of_file[:variable_of_slice]:
                os.remove(delet)
            name_of_file = name_of_file[variable_of_slice:]
            name_of_file.append(new_temper.name)
        else:
            merge_sort_file1(name_of_file, new_temper.name)
            for delet in name_of_file:
                os.remove(delet)
            name_of_file.clear()
            name_of_file.append(new_temper.name)
    return name_of_file[0]


# def merge_sort(li):
#     if len(li) > 1:
#         mid = len(li) // 2
#         left_part = li[:mid]
#         right_part = li[mid:]
#
#         merge_sort(left_part)
#         merge_sort(right_part)
#         in_place(left_part,right_part,li)
#
# def in_place(left_part,right_part,li):
#     i = 0
#     j = 0
#     k = 0
#     while i < len(left_part) and j < len(right_part):
#         if int(left_part[i]) < int(right_part[j]):
#             li[k] = left_part[i]
#             i = i + 1
#         else:
#             li[k] = right_part[j]
#             j = j + 1
#         k = k + 1
#
#     while i < len(left_part):
#         li[k] = left_part[i]
#         i = i + 1
#         k = k + 1
#
#     while j < len(right_part):
#         li[k] = right_part[j]
#         j = j + 1
#         k = k + 1
# def merge_sort_file(path,path1,path2,number_of_num):
#     f = open(path, 'r')
#     f1 = open(path1, 'r')
#     f2 = open(path2, 'w')
#     right = f1.readline()
#     left = f.readline()
#     while  right!='' and left!='':
#         if int(left) < int(right):
#             f2.write(left)
#             left = f.readline()
#         else:
#             f2.write(right)
#             right = f1.readline()
#
#     while  left!='':
#         f2.write(left)
#         left = f.readline()
#
#     while  right!='' :
#         f2.write(right)
#         right = f1.readline()
#     f2.close()
#     f1.close()
#     f.close()
