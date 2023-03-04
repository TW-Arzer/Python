import sys
import math

list = sys.argv[1:]

for i in list:
    new_i = int(i)
    try:
        x = math.sqrt(new_i)
    except ValueError as e:
        print("No negative Values allowed")
    else:
        print(x)
    finally:
        print("Au revoir!")