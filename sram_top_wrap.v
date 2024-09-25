// SRAM Top 

module sky130_sram_1kbyte_1rw1r_32x256_8_top(
  
  input      wire    clk, 
  
  input      wire    sram_cs_i, 
  input      wire    sram_we_i, 
  
  input      wire [3:0] sram_wmask_i, 
  input      wire [7:0] sram_addr_i, 
  
  input      wire [31:0] sram_wr_data_i, 
  
  output     wire [31:0] sram_rd_data_o
 
);

// SRAM Instance 

  sky130_sram_1kbyte_1rw1r_32x256_8 SRAM ( 
    .clk0                       (clk), 
    .csb0                       (~sram_cs_i), 
    .web0                       (~sram_we_i), 
    .wmask0                     (sram_wmask_i), 
    .addr0                      (sram_addr_i), 
    .din0                       (sram_wr_data_i), 
    .dout0                      (sram_rd_data_o), 
    .clk1                       (1'b0), 
    .csb1                       (1'b1), 
    .addr1                      (), 
    .dout1                      ()    
 );


 initial begin
    $dumpfile("sky130_sram_1kbyte_1rw1r_32x256_8_top.vcd"); 
    $dumpvars(0, sky130_sram_1kbyte_1rw1r_32x256_8_top); 
 end 


endmodule 
