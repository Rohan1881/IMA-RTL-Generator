import os

def run_simulation():
    print("Running Simulation...")
    logs = "Running Simulation...\n"

    # =========================
    # Compile
    # =========================
    compile_status = os.system("iverilog -o sim.out controller.v testbench.v")

    if compile_status != 0:
        print("Compilation Failed")
        return " Compilation Failed"

    # =========================
    # Run
    # =========================
    run_status = os.system("vvp sim.out > output.log")

    if run_status != 0:
        print("Simulation Failed")
        return " Simulation Failed"

    # =========================
    # Read output
    # =========================
    try:
        with open("output.log", "r", encoding="utf-8") as f:
            output = f.read()
    except FileNotFoundError:
        return " output.log not found"

    # =========================
    # Analyze results
    # =========================
    results = {
        "TEST1": "FAIL",
        "TEST2": "FAIL",
        "TEST3": "FAIL"
    }

    for key in results:
        if f"{key} PASS" in output:
            results[key] = "PASS"

    print("--------------------------------")
    logs += "--------------------------------\n"

    for k, v in results.items():
        print(f"{k} {v}")
        logs += f"{k} {v}\n"

    if all(v == "PASS" for v in results.values()):
        print("ALL TESTS PASSED")
        logs += "ALL TESTS PASSED\n"
    else:
        print("SOME TESTS FAILED")
        logs += "SOME TESTS FAILED\n"

    print("--------------------------------")
    logs += "--------------------------------\n"

    return logs
