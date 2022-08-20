#!/usr/bin/python3

## Uso
## mv converter.py converter; chmod +x converter
## f2m -> feet to meters
## m2f -> meter to feet
## ./convert f2m 1
## ./convert m2f 0.3

import sys

def m2f(meter):
    return (meter/0.3048)

def f2m(feet):
    return (feet*0.3048)

def help():
    print("Convert feet->meters->feet")
    print("f2m -> feet to meters\nm2f -> meters to feet\n")
    print("  ~$ converter f2m 1")
    print("  ~$ converter m2f 0.3")

def main():
    if sys.argv[1] == "m2f":
        f = m2f(float(sys.argv[2]))
        print("{meter}m -> {feet:.3f}ft".format(
                meter=sys.argv[2],
                feet=f
            ))
    elif sys.argv[1] == "f2m":
        m = f2m(float(sys.argv[2]))
        print("{feet}f -> {meter:.3}m".format(
                feet=sys.argv[2],
                meter=m
            ))

# Defino para isso poder se tornar uma lib.
if __name__ == "__main__":
    print("### Converter ###")
    if len(sys.argv) == 3:
        main()
    else:
        help()
