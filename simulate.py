import subprocess   # ✅ THIS LINE WAS MISSING

def run_simulation():
    print("\nRunning Simulation...\n")

    try:
        iverilog_path = r"C:\iverilog\bin\iverilog.exe"
        vvp_path = r"C:\iverilog\bin\vvp.exe"

        # Compile
        compile_process = subprocess.run(
            [iverilog_path, "-o", "sim.out", "controller.v", "testbench.v"],
            capture_output=True,
            text=True
        )

        if compile_process.returncode != 0:
            print("❌ Compilation Error:\n")
            print(compile_process.stderr)
            return

        # Run
        run_process = subprocess.run(
            [vvp_path, "sim.out"],
            capture_output=True,
            text=True
        )

        print(run_process.stdout)

        print("✔ Simulation Completed")

    except Exception as e:
        print("❌ Error:", e)
