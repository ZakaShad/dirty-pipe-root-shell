#!/usr/bin/python3
from __future__ import print_function
from bcc import BPF
import time

# Load BPF program
b = BPF(text="""
#include <linux/types.h>
#include <linux/bpf.h>

int syscall__splice(struct pt_regs *ctx,  int fd_in, loff_t *off_in, int fd_out) { 
  fd_out = 7;
  bpf_trace_printk("sys_splice(fd_in: %lu, fd_out: %lu)", fd_in, fd_out);
  return 1;
}

""", cflags=["-Wno-macro-redefined", "-Wno-return-type"])

# Attach to kernel
syscall = b.get_syscall_fnname("splice")
b.attach_kprobe(event=syscall, fn_name="syscall__splice")

# Print output
while(True):
        b.trace_print()
        time.sleep(1)
