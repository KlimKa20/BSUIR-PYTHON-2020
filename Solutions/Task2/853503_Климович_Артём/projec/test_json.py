import pytest
import json
import projec.JSON as JSON
class TestJson:

    def test_emptylist(self):
        assert(JSON.my_json(list()) == json.dumps(list()))
        assert (JSON.from_json_split('[]') == json.loads('[]'))


    def test_emptytuple(self):
        assert(JSON.my_json(tuple()) == json.dumps(tuple()))


    def test_emptydict(self):
        assert(JSON.my_json(dict()) == json.dumps(dict()))
        assert (JSON.from_json_split('{}') == json.loads('{}'))

    def test_class(self):
        class SubField:
            def __init__(self):
                self.flag = True

        class Field:
            def __init__(self, tag1, tag2, sub_field_flag=True):
                self.tag1 = tag1
                self.tag2 = tag2

                self.sub_field = SubField()
                self.sub_field.flag = sub_field_flag

        class Object:
            a = 0
            b = '123'

            def __init__(self):
                self.c = 3
                self.items = [1, 2, 3, 4]
                self.maps = {
                    'is': True,
                    'not': 0,
                }

                self.field = Field('abc', 'tag2')
                self.field_2 = Field(777, False, sub_field_flag=False)

        obj = Object()
        assert (JSON.my_json(obj) == json.dumps(JSON.object_to_dict(obj)))
        assert (json.loads(JSON.my_json(obj)) == JSON.from_json_split(JSON.my_json(JSON.object_to_dict(obj))))

    def test_one(self):
        data = [88, [45, [44, [44, [33, 212]]], 77, [], [32, True, None, "sdasd"]], {
            'key': 1005,
            '2': '2',
            "marks": 5,
            "sdf": [5, {6: [43, [34, {}, 90]]}, 8],
            "is_valid": True
        }]
        data_json = '[88, [45, [44, [44, [33, null, 212]]], {"sfd": {}}, 77, [], [32, true, "sdasd"]], ' \
                    '{"key": 1005, "2": "2", "marks": 5, "sdf": [5, {"6": [43, [34, {}, 90]]}, 8], ' \
                    '"is_valid": true}]'
        assert(JSON.my_json(data) == json.dumps(data))
        assert (JSON.from_json_split(data_json) == json.loads(data_json))

    def test_two(self):
        assert(JSON.my_json([45, '34', (345)]) == json.dumps([45, '34', (345)]))

    def test_bad_input(self):
        assert (JSON.from_json_split("}}") == "bad input")
