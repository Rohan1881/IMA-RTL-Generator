import json

def generate_testbench(controller_file, config):

    # Dynamic module selection
    module_name = "dram_controller" if config["type"] == "DRAM" else "sram_controller"

    tb = f"""
module testbench;

reg clk;
reg rst;
reg we;
reg [8:0] addr;
reg [255:0] din;
wire [255:0] dout;

// DUT
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
    //  Waveform dump
    $dumpfile("wave.vcd");
    $dumpvars(0, testbench);

    clk = 0;
    rst = 1;
    we = 0;
    addr = 0;
    din = 0;

    #10 rst = 0;

    // =========================
    // TEST1: Basic write/read
    // =========================
    we = 1;
    addr = 9'd1;
    din = 256'hA5A5;
    #10;

    we = 0;
    #10;

    $display("WRITE: addr=%d data=%h", addr, din);
    $display("READ : addr=%d data=%h", addr, dout);

    if (dout == 256'hA5A5)
        $display("TEST1 PASS");
    else
        $display("TEST1 FAIL");


    // =========================
    // TEST2: Boundary
    // =========================
    we = 1;
    addr = 9'd0;
    din = 256'hDEAD;
    #10;

    we = 0;
    #10;

    $display("WRITE: addr=%d data=%h", addr, din);
    $display("READ : addr=%d data=%h", addr, dout);

    if (dout == 256'hDEAD)
        $display("TEST2 PASS");
    else
        $display("TEST2 FAIL");


    // =========================
    // TEST3: Random
    // =========================
    we = 1;
    addr = 9'd100;
    din = 256'h1234;
    #10;

    we = 0;
    #10;

    $display("WRITE: addr=%d data=%h", addr, din);
    $display("READ : addr=%d data=%h", addr, dout);

    if (dout == 256'h1234)
        $display("TEST3 PASS");
    else
        $display("TEST3 FAIL");

    $finish;
end

endmodule
"""

    with open("testbench.v", "w") as f:
        f.write(tb)

    print(f" testbench.v generated for {module_name}")