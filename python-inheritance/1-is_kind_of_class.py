#!/usr/bin/env python3
""" Module containing is_kind_of_class function """

def is_kind_of_class(obj, a_class):
    """ Check if an object is an instance of a specified class or its subclass """
    return isinstance(obj, a_class)

if __name__ == "__main__":
    class A:
        pass

    class B(A):
        pass

    obj_a = A()
    obj_b = B()

    print(is_kind_of_class(obj_a, A))  # Should print True
    print(is_kind_of_class(obj_b, B))  # Should print True
    print(is_kind_of_class(obj_b, A))  # Should print True
    print(is_kind_of_class(obj_a, B))  # Should print False
