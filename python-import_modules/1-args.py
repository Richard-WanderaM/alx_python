#!/usr/bin/env python3
import sys

def main():
    argc = len(sys.argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        plural = "s" if argc > 1 else ""
        print(f"{argc} argument{plural}:")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
