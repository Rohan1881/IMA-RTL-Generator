from flask import Flask, request, render_template_string
import re

app = Flask(__name__)

def parse_input(text):
    width = int(re.search(r'width\s*(\d+)', text).group(1))
    depth = int(re.search(r'depth\s*(\d+)', text).group(1))
    low_power = "low power" in text.lower()

    return {"width": width, "depth": depth, "low_power": low_power}

def generate_reports(config):
    width = config["width"]
    depth = config["depth"]
    low_power = config["low_power"]

    power = "Low" if low_power else "Medium"
    cdc = "HIGH" if width > 16 else "LOW"

    delay = width * 0.1 + depth * 0.05
    timing = "Violation" if delay > 10 else "Met"

    return power, cdc, timing, delay

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        text = request.form['text']
        config = parse_input(text)
        power, cdc, timing, delay = generate_reports(config)

        result = f"""
        <h3>Results:</h3>
        Power: {power}<br>
        CDC Risk: {cdc}<br>
        Timing: {timing} ({delay:.2f} ns)
        """

    return render_template_string("""
    <h2>RTL Generator (Phase 3)</h2>
    <form method="post">
        <input name="text" style="width:400px">
        <input type="submit">
    </form>
    <br>
    """ + result)

if __name__ == "__main__":
    app.run(debug=True)
