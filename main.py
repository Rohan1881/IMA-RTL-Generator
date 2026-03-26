from parser import parse_input
from rtl_generator import generate_rtl
from testbench_generator import generate_testbench
from simulate import run_simulation
from report_generator import generate_all_reports

if __name__ == "__main__":

    print("=== IMA RTL PIPELINE ===")

    # Step 1: Input
    user_input = input("Enter memory specification:\n")

    # Step 2: Parse
    config = parse_input(user_input)
    print("Parsed Config:", config)

    # Step 3: RTL generation
    generate_rtl(config)
    print("RTL GENERATED")

    # Step 4: Testbench generation
    generate_testbench("controller.v", config)
    print("TESTBENCH GENERATED")

    # Step 5: Simulation
    run_simulation()

    # Step 6: Reports
    generate_all_reports()

    print("=== FLOW COMPLETED ===")
