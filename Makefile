SIM = icarus
TOPLEVEL_LANG = verilog
TOPLEVEL = sky130_sram_1kbyte_1rw1r_32x256_8_top
MODULE = sky130_sram_1kbyte_1rw1r_32x256_8_tb

VERILOG_SOURCES = ./sram_top_wrap.v \
		  ./sky130_sram_1kbyte_1rw1r_32x256_8.v


include $(shell cocotb-config --makefiles)/Makefile.sim
