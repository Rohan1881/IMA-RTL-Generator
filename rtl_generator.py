from jinja2 import Environment, FileSystemLoader

# Load templates folder
env = Environment(loader=FileSystemLoader("templates"))

def generate_rtl(config):
    width = config["width"]
    depth = config["depth"]
    addr_width = depth.bit_length() - 1

    # Select template
    if config["type"] == "DRAM":
        template = env.get_template("dram.v.j2")
    else:
        template = env.get_template("sram.v.j2")

    # Render template
    return template.render(
    width=width,
    depth=depth,
    addr_width=addr_width,
    low_power=config["low_power"],
    protocol=config["protocol"],
    mode=config.get("mode", "NORMAL")
)

def save_rtl(code):
    with open("controller.v", "w") as f:
        f.write(code)
