import random

def generate_testbench(config):
    width = config["width"]
    depth = config["depth"]
    module_name = "dram_controller" if config["type"] == "DRAM" else "sram_controller"
    max_addr = depth - 1
    rand_val = random.randint(1, 255)

    tb = f"""
module tb;

reg clk;
reg rst;
reg we;
reg [{depth.bit_length()-2}:0] addr;
reg [{width-1}:0] din;
wire [{width-1}:0] dout;

{module_name} uut (
    .clk(clk),
    .rst(rst),
    .we(we),
    .addr(addr),
    .din(din),
    .dout(dout)
);

// Clock
always #5 clk = ~clk;

initial begin
    clk = 0;
    rst = 1;
    we = 0;
    addr = 0;
    din = 0;

    #10 rst = 0;

    // TEST 1: Basic Write/Read
    we = 1; addr = 1; din = 10;
    #10 we = 0;
    #10;
    if (dout == 10) $display("TEST1 PASS");
    else $display("TEST1 FAIL");

    // TEST 2: Boundary
    we = 1; addr = 0; din = 20;
    #10 we = 0;
    #10;
    if (dout == 20) $display("TEST2 PASS");
    else $display("TEST2 FAIL");

    // TEST 3: Random
    we = 1; addr = {max_addr}; din = {rand_val};
    #10 we = 0;
    #10;
    if (dout == {rand_val}) $display("TEST3 PASS");
    else $display("TEST3 FAIL");

    #10 $finish;
end

endmodule
"""
    return tb


def save_testbench(code):
    with open("testbench.v", "w") as f:
        f.write(code)
