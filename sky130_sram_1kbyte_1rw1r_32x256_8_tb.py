# ************************************************** # 
#   File : SRAM Test
#   Version  : 0.001 
#   Design : sky130_sram_1kbyte_1rw1r_32x256_8 
#   Bugs  : -
# ************************************************** #

import cocotb
import random 
from  cocotb.triggers import RisingEdge 
from  cocotb.clock import Clock 

async def sram_test (dut) : 

    sram_rand_addr = [] 

    ### Generate Clock 
    clock = cocotb.start_soon(Clock(dut.clk, 10, 'us').start(start_high = False)) 

    ### Drive Initial Values on the Signals 
    dut.sram_cs_i.value = 0 
    dut.sram_we_i.value = 0 

    ### Wait for a few cycles 
    for _ in range(4) : 
        await RisingEdge(dut.clk) 

    ### Drive Random Stimulus to the SRAM 
    for i in range(256) : 
        sram_rand_addr.append(random.randrange(0, 256)) 
        dut.sram_cs_i.value = 0x1 
        dut.sram_we_i.value = 0x1 
        dut.sram_wmask_i.value = random.randrange(0, 16) 
        dut.sram_addr_i.value = sram_rand_addr[i] 
        dut.sram_wr_data_i.value = random.randrange(0, 0xFFFFFFFF)
        await RisingEdge(dut.clk) 

    
    random.shuffle(sram_rand_addr)

    ### Read Routine 
    for i in range(256) : 
        dut.sram_cs_i.value = 0x1 
        dut.sram_we_i.value = 0x0 
        dut.sram_addr_i.value = sram_rand_addr[i] 
        await RisingEdge(dut.clk) 

    dut.sram_cs_i.value = 0x0

    for _ in range(4) : 
        await RisingEdge(dut.clk)

    clock.kill() 

@cocotb.test() 
async def sram_rand_test(dut) : 
    await sram_test(dut) 
