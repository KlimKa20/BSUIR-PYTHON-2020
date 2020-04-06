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


