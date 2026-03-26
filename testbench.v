
module tb;

reg clk;
reg rst;
reg we;
reg [7:0] addr;
reg [255:0] din;
wire [255:0] dout;

sram_controller uut (
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
    we = 1; addr = 255; din = 167;
    #10 we = 0;
    #10;
    if (dout == 167) $display("TEST3 PASS");
    else $display("TEST3 FAIL");

    #10 $finish;
end

endmodule
