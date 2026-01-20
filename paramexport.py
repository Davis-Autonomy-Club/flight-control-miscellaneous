#!/usr/bin/env python3
#alt:/usr/bin/python3

import sys
from decimal import Decimal

def format_float(val):
    d = Decimal(val)
    return "{0:f}".format(d.quantize(Decimal("1.0000000")).normalize())

def main():
    if len(sys.argv) < 3:
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
            f_out.write("# NOTE: Converted from QGroundControl\n")
            
            for line in f_in:
                if line.startswith('#') or not line.strip():
                    continue

                parts = line.split()
                
                if len(parts) >= 5:
                    name = parts[2]
                    value = parts[3]
                    param_type = parts[4]

                    if param_type == "9":
                        try:
                            value = format_float(value)
                        except:
                            pass

                    f_out.write(f"{name},{value}\n")

    except Exception:
        pass

if __name__ == '__main__':
    main()