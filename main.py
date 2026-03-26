from testbench_generator import generate_testbench
from simulate import run_simulation
from report_generator import generate_all_reports

if __name__ == "__main__":

    print("=== IMA Verification Pipeline ===")

    config = {
        "type": "SRAM"   # change to DRAM if needed
    }

    # Step 1: Generate testbench
    print("\n[1] Generating Testbench...")
    generate_testbench("controller.v", config)

    # Step 2: Run simulation
    print("\n[2] Running Simulation...")
    run_simulation()

    # Step 3: Generate reports
    print("\n[3] Generating Reports...")
    generate_all_reports()

    print("\n=== Pipeline Completed ===")