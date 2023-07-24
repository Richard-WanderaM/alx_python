#!/usr/bin/python3
import importlib.util

def load_variable_from_file(file_path, variable_name):
    spec = importlib.util.spec_from_file_location("module_name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, variable_name)

if __name__ == "__main__":
    variable_file_path = "variable_load_2.py"
    variable_name = "a"
    variable_value = load_variable_from_file(variable_file_path, variable_name)
    print(variable_value)
