import re

def parse_input(user_input):
    text = user_input.lower()
    config = {}

    if "dram" in text:
        config["type"] = "DRAM"
    else:
        config["type"] = "SRAM"

    m = re.search(r'(\d+)[- ]?bit', text)
    config["width"] = int(m.group(1)) if m else 32

    m = re.search(r'depth\s*(\d+)', text)
    config["depth"] = int(m.group(1)) if m else 256

    config["protocol"] = "AXI" if "axi" in text else "BASIC"

    m = re.search(r'(\d+)\s*ns', text)
    config["timing_ns"] = int(m.group(1)) if m else 10

    config["low_power"] = "low power" in text
    # Intent-based interpretation
    if "high performance" in text:
        config["mode"] = "HIGH_PERFORMANCE"
    elif "low power" in text:
        config["mode"] = "LOW_POWER"
    else:
        config["mode"] = "NORMAL"

    return config
    
