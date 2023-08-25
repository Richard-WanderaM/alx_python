#!/usr/bin/env python3
""" Module containing inherits_from function """

def inherits_from(obj, a_class):
    """ Check if an object inherits from a specified class """
    return issubclass(type(obj), a_class) and type(obj) != a_class

if __name__ == "__main__":
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    obj_a = A()
    obj_b = B()
    obj_c = C()

    print(inherits_from(obj_b, A))  # Should print True
    print(inherits_from(obj_c, A))  # Should print True
    print(inherits_from(obj_c, B))  # Should print True
    print(inherits_from(obj_a, B))  # Should print False
    print(inherits_from(obj_a, C))  # Should print False
