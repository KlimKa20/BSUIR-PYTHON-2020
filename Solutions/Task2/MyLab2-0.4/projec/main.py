import projec.Vector as Vector
import projec.JSON as JSON
import projec.Fibonacci as Fibonacci
import projec.Singleton as Singleton
import projec.Sort as Sort
import json


def vector_e():
    try:
        vec1 = 3 * Vector.Vector([4, 3, 4, 6])
        print("{0:.2f}".format(vec1.len()))
        print(Vector.Vector([2, 3, 4, 5]).len())
    except BaseException as ex:
        print(ex)


def singleton_e():
    s1 = Singleton.Singleton("Kate")
    s2 = Singleton.Singleton("Alex")
    print(s1.__dict__)
    print(s2.__dict__)
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")

    else:
        print("Singleton failed, variables contain different instances.")


def fibonacci_e():
    print([Fibonacci.fib(n) for n in range(7)])


def json_e():
    obj = JSON.Object()
    data = [88, [45, [44, [44, [33, 212]]], 77, [], [32, True, "sdasd"]], {
        'key': 1005,
        '2': '2',
        "marks": 5,
        "sdf": [5, {6: [43, [34, {}, 90]]}, 8],
        "is_valid": True
    }]
    print(json.loads(JSON.my_json(JSON.object_to_dict(obj))))
    print(JSON.from_json_split(JSON.my_json(JSON.object_to_dict(obj))))
    print(json.loads(JSON.my_json(data)))
    print(JSON.from_json_split(JSON.my_json(data)))


def sort_e():
    name_of_file = list()
    print(Sort.sort(name_of_file))

print("Vector\n")
vector_e()
print("\nFibonacci\n")
fibonacci_e()
print("\nJSON\n")
json_e()
print("\nSingleton\n")
singleton_e()
print("\nSort\n")
sort_e()
