import os

def run_simulation():
    print("Running Simulation...")

    # Compile
    compile_status = os.system("iverilog -o sim.out controller.v testbench.v")

    if compile_status != 0:
        print(" Compilation Failed")
        return

    # Run
    run_status = os.system("vvp sim.out > output.log")

    if run_status != 0:
        print(" Simulation Failed")
        return

    # Read output
    with open("output.log", "r", encoding="utf-8") as f:
        output = f.read()

    results = {
        "TEST1": "FAIL",
        "TEST2": "FAIL",
        "TEST3": "FAIL"
    }

    for key in results:
        if f"{key} PASS" in output:
            results[key] = "PASS"

    print("--------------------------------")
    for k, v in results.items():
        print(f"{k} {v}")

    if all(v == "PASS" for v in results.values()):
        print("ALL TESTS PASSED")
    else:
        print(" SOME TESTS FAILED")

    print("--------------------------------")