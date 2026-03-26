from parser import parse_input
from rtl_generator import generate_rtl, save_rtl

config = parse_input("128-bit DRAM AXI depth 512 5ns low power")

code = generate_rtl(config)
save_rtl(code)

print("DONE")
