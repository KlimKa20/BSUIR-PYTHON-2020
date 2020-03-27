import projec.Sort as Sort
import pytest


class Testsort:

    def test_succesfull(self):
        result = True
        jj = list()
        ij = list()
        with open(Sort.sort(ij)) as file:
            jj.append(int(file.readline()))
        for num in range(0, len(jj) - 1):
            if jj[num] > jj[num]:
                result = False
        assert (result == True)

    def test_close_file(self):
        result = 0
        name_of_file = list()
        Sort.sort(name_of_file)
        for file in name_of_file:
            try:
                f = open(file)
                result +=1
            except:
                print("deleted")
        assert (result == 1)
