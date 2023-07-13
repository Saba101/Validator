import operator
import re


# def between_(a:int, _tuple):
#     return _tuple[0] <= a <= _tuple[1]


def in_(a, _list):
    return a in _list


def empty_(a):
    if type(a) is str:
        return len(a) == 0 or a is None
    elif type(a) is int or type(a) is float:
        return a is None


def not_empty_(a):
    if type(a) is str:
        return len(a) > 0 and a is not None
    elif type(a) is int or type(a) is float:
        return a is not None


def contains_(a:str, value):
    if re.search(f"{value}", a):
        return True
    else:
        return False


def starts_with_(a:str, value):
    if re.search(f"^{value}", a):
        return True
    else:
        return False


def ends_with_(a:str, value):
    if re.search(f"{value}$", a):
        return True
    else:
        return False

def and_(a, b):
    return operator.and_(a, b)

def or_(a, b):
    return operator.or_(a, b)


class Operations:

    def __init__(self):
        self.__operation = None
        self.__operations = {
            'not_equals': operator.ne,  # "!=",
            'equals': operator.eq,  # "==",
            'is': operator.eq,
            'greater_than': operator.gt,  # ">",
            'less_than': operator.lt,  # "<",
            'greater_than_or_equal': operator.ge,  # ">=",
            'less_than_or_equal': operator.le,  # "<=",

            # 'between': between_,
            'in': in_,

            'is_empty': empty_,
            'not_empty': not_empty_,

            'contains': contains_,
            'starts_with': starts_with_,
            'ends_with': ends_with_
        }

    def select_operation(self, condition):
        self.__operation = self.__operations.get(condition)
        # print(self.__operation)

    # def apply_operation(self, a, b=None):
    #     if b == None:
    #         if self.__operation == empty_ or self.__operation == not_empty_:
    #             return self.__operation(a)
    #
    #         else:
    #             print("Error: One required argument missing!")
    #             return "Operation not performed!"
    #
    #     else:
    #         return self.__operation(a, b) if a != None and b != None else "Error.."

    def apply_operation(self, _params: tuple):
        if len(_params) == 0:
            return "No parameters are provided. Cannot perform any operation!"

        import inspect
        req_params = dict(inspect.signature(self.__operation).parameters)
        # given_params = dict(inspect.signature(self.apply_operation).parameters)
        # print("Required:" , req_params, "\nGiven:", given_params)

        if len(req_params) == len(_params):
            return self.__operation(*_params)

        else:
            print("Error: One required argument missing!")
            return "Operation not performed!"