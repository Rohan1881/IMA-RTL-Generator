module sram_controller (
    input clk,
    input rst,
    input we,
    input [8:0] addr,
    input [255:0] din,
    output reg [255:0] dout
);

reg [255:0] mem [0:511];

always @(posedge clk) begin
    if (rst) begin
        dout <= 0;
    end else begin
        if (we) begin
            // Write path (low switching)
            mem[addr] <= din;
        end else begin
            // Low power read
            dout <= mem[addr];
        end
    end
end

endmodule