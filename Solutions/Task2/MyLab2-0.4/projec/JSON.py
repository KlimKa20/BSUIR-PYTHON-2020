import  json
import types

def my_json(value):
    if isinstance(value, dict):
        string = ', '.join(['"{}"'.format(str(x)) + ': ' + my_json(y) for (x, y) in value.items()])
        return '{' + string + '}'
    elif isinstance(value, str):
        return '"{}"'.format(value)
    elif isinstance(value, bool):
        return 'true' if value == True else 'false'
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, list):
        string = ', '.join([my_json(i) for i in value])
        return '[' + string + ']'
    elif isinstance(value, tuple):
        string = ', '.join([my_json(i) for i in value])
        return '[' + string + ']'
    elif value == None:
        return "null"
    else:
        return my_json(object_to_dict(value))


def object_to_dict(object):
    fields = dict()
    fields.update(object.__class__.__dict__)
    fields.update(object.__dict__)
    fields = dict(filter(lambda x: not x[0].startswith('_'), fields.items()))
    new_fields = dict()
    for k, v in fields.items():
        if hasattr(v, '__dict__'):
            v = object_to_dict(v)
        new_fields[k] = v
    return new_fields


def from_json_split(string):
    try:
        return  from_json(string.split(',')[0], string.split(','))
    except Exception:
        return "bad input"

def from_json(text,string):
    if text == "true":
        return True
    elif text == "false":
        return False
    elif text == "null":
        return None
    elif text[0] == '"':
        temp = text[1: -1]
    elif text[0] != "{" and text[0] != "[":
        temp = int(text)
    elif text[0]=='[':
        temp = list()
        if text == '[]':
            return temp
        text = text[1:]
        while text.find(']') == -1:
            if text[0] == '{' or text[0] == '[':
                temp.append(from_json(text, string))
                if len(string[0]) != 0 and string[0][0] == ']': #проверка на закрытие строк
                    string[0] = string[0][1:]
                    return temp
                else:
                    if len(string) != 0:
                        string.pop(0)
                        text = string[0]
                        text = text[1:]
                        continue
            temp.append(from_json(text[:], string))
            string.pop(0)
            text = string[0]
            text = text[1:]
            if text[0] == '[' and text[1] == ']':# Словарь
                temp.append(list())
                # if len(text) != 2:
                #     return temp
                # else:
                #     string.pop(0)
                #     text = string[0]
                #     text = text[1:]
                string.pop(0)
                text = string[0]
                text = text[1:]
        tt = text.find(']')
        temp.append(from_json(text[:tt], string))
        string[0] = text[tt+1:]
    else:
        temp = dict()
        if text[0] == '{' and text[1] == '}':
            string[0] = string[0][string[0].find('}'):]
            return temp
        text = text[1:]
        while text.find('}') == -1 or (text.find('{') != -1 and text.find('}') != -1):
            index = text.find(':')
            if text[index+2] == '{' or text[index+2] == '[':
                temper = from_json(text[index + 2:], string)
                temp[text[1:index - 1]] = temper
                if len(string[0]) != 0 and string[0][0] == '}': #проверка на закрытие строк
                    string[0] = string[0][1:]
                    return temp
                else:
                    if len(string) != 0:
                        string.pop(0)
                        text = string[0]
                        text = text[1:]
                        continue
            temper = from_json(text[index+2:], string)
            temp[text[1:index-1]] = temper
            string.pop(0)
            text = string[0]
            text = text[1:]
            # if text[0] == '{' and text[1] == '}':# Словарь
            #     temp.append(dict())
            #     if len(text) != 2:
            #         return temp
            #     else:
            #         string.pop(0)
            #         text = string[0]
            #         text = text[1:]
        tt = text.find('}')
        index = text.find(':')
        string[0] = text[tt:]
        temper = from_json(text[index + 2:tt], string)
        temp[text[1:index - 1]] = temper
        string[0] = text[tt + 1:]
    return temp


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


data = [88, [45, [44, [44, [33, 212]]], 77, [], [32, True, "sdasd"]], {
        'key': 1005,
        '2': '2',
        "marks": 5,
        "sdf": [5, {6: [43, [34, {}, 90]]}, 8],
        "is_valid": True
    }]
