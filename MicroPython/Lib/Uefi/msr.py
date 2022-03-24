## @file
# MicroPython wrapper of processor MSR.
#
# Copyright (c) 2018, Intel Corporation. All rights reserved.<BR>
# This program and the accompanying materials
# are licensed and made available under the terms and conditions of the BSD License
# which accompanies this distribution.  The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#

from _uefi import *
import _ets

from ucollections import OrderedDict

IA32_APIC_BASE = OrderedDict((
    ("Reserved1",                           "Q:8"),
    ("Processor_is_BSP",                    "Q:1"),
    ("Reserved2",                           "Q:1"),
    ("Enable_x2APIC_mode",                  "Q:1"),
    ("APIC_Global_Enable",                  "Q:1"),
    ("APIC_Base",                           "Q:24"),
    ("Reserved3",                           "Q:28"),
))

IA32_FEATURE_CONTROL = OrderedDict((
    ("Lock_bit",                            "Q:1"),
    ("Enable_VMX_inside_SMX_operation",     "Q:1"),
    ("Enable_VMX_outside_SMX_operation",    "Q:1"),
    ("Reserved1",                           "Q:5"),
    ("SENTER_Local_Function_Enables",       "Q:7"),
    ("SENTER_Global_Enable",                "Q:1"),
    ("Reserved2",                           "Q:1"),
    ("SGX_Launch_Control_Enable",           "Q:1"),
    ("SGX_Global_Enable",                   "Q:1"),
    ("Reserved3",                           "Q:1"),
    ("LMCE_On",                             "Q:1"),
    ("Reserved4",                           "Q:43"),
))

IA32_MISC_ENABLE = OrderedDict((
    ("Fast_Strings_Enable",                         "Q:1"),
    ("Reserved1",                                   "Q:2"),
    ("Automatic_Thermal_Control_Circuit_Enable",    "Q:1"),
    ("Reserved2",                                   "Q:3"),
    ("Performance_Monitoring_Available",            "Q:1"),
    ("Reserved3",                                   "Q:3"),
    ("Branch_Trace_Storage_Unavailable",            "Q:1"),
    ("Processor_Event_Based_Sampling_Unavailable",  "Q:1"),
    ("Reserve4",                                    "Q:3"),
    ("Enhanced_Intel_SpeedStep_Technology_Enable",  "Q:1"),
    ("Reserved5",                                   "Q:1"),
    ("ENABLE_MONITOR_FSM",                          "Q:1"),
    ("Reserved6",                                   "Q:3"),
    ("Limit_CPUID_Maxval",                          "Q:1"),
    ("xTPR_Message_Disable",                        "Q:1"),
    ("Reserved7",                                   "Q:10"),
    ("XD_Bit_Disable",                              "Q:1"),
    ("Reserved8",                                   "Q:29"),
))

MSR_MISC_FEATURE_CONTROL = OrderedDict((
    ("L2_Hardware_Prefetcher_Disable",    "Q:1"),
    ("Reserved1",                         "Q:1"),
    ("DCU_Hardware_Prefetcher_Disable",   "Q:1"),
    ("Reserved2",                         "Q:61"),
))

IA32_EFER = OrderedDict((
    ("SYSCALL_Enable",              "Q:1"),
    ("Reserved1",                   "Q:7"),
    ("IA32e_Mode_Enable",           "Q:1"),
    ("Reserved2",                   "Q:1"),
    ("IA32e_Mode_Active",           "Q:1"),
    ("Execute_Disable_Bit_Enable",  "Q:1"),
    ("Reserved3",                   "Q:52"),
))

IA32_X2APIC_APICID = OrderedDict((
    ("x2APIC_ID",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_VERSION = OrderedDict((
    ("Vector",                  "Q:8"),
    ("Reserved1",               "Q:8"),
    ("Max_LVT_Entry",           "Q:8"),
    ("Directed_EOI_Support",    "Q:1"),
    ("Reserved2",               "Q:7"),
))

IA32_X2APIC_TPR = OrderedDict((
    ("Task_Priority_Register",  "Q:8"),
    ("Reserved1",               "Q:56"),
))

IA32_X2APIC_PPR = OrderedDict((
    ("Processor_Priority_Register", "Q:32"),
    ("Reserved1",                   "Q:32"),
))

IA32_X2APIC_EOI = OrderedDict((
    ("EOI_Register",    "Q:32"),
    ("Reserved1",       "Q:32"),
))

IA32_X2APIC_LDR = OrderedDict((
    ("Logical_ID",  "Q:16"),
    ("Cluster_ID",  "Q:16"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_SIVR = OrderedDict((
    ("Spurious_Vector",         "Q:8"),
    ("APIC_Software_Enable",    "Q:1"),
    ("Reserved1",               "Q:3"),
    ("EOI_Broadcast_Disable",   "Q:1"),
    ("Reserved2",               "Q:51"),
))

IA32_X2APIC_ISR0 = OrderedDict((
    ("In_Service_Register_0_to_31",    "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_ISR1 = OrderedDict((
    ("In_Service_Register_32_to_63",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_ISR2 = OrderedDict((
    ("In_Service_Register_64_to_95",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_ISR3 = OrderedDict((
    ("In_Service_Register_96_to_127",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_ISR4 = OrderedDict((
    ("In_Service_Register_128_to_159",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_ISR5 = OrderedDict((
    ("In_Service_Register_160_to_191",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_ISR6 = OrderedDict((
    ("In_Service_Register_192_to_223",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_ISR7 = OrderedDict((
    ("In_Service_Register_224_to_255",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_TMR0 = OrderedDict((
    ("Trigger_Mode_Register_0_to_31",    "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_TMR1 = OrderedDict((
    ("Trigger_Mode_Register_32_to_63",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_TMR2 = OrderedDict((
    ("Trigger_Mode_Register_64_to_95",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_TMR3 = OrderedDict((
    ("Trigger_Mode_Register_96_to_127",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_TMR4 = OrderedDict((
    ("Trigger_Mode_Register_128_to_159",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_TMR5 = OrderedDict((
    ("Trigger_Mode_Register_160_to_191",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_TMR6 = OrderedDict((
    ("Trigger_Mode_Register_192_to_223",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_TMR7 = OrderedDict((
    ("Trigger_Mode_Register_224_to_255",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_IRR0 = OrderedDict((
    ("Interrupt_Request_Register_0_to_31",    "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_IRR1 = OrderedDict((
    ("Interrupt_Request_Register_32_to_63",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_IRR2 = OrderedDict((
    ("Interrupt_Request_Register_64_to_95",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_IRR3 = OrderedDict((
    ("Interrupt_Request_Register_96_to_127",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_IRR4 = OrderedDict((
    ("Interrupt_Request_Register_128_to_159",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_IRR5 = OrderedDict((
    ("Interrupt_Request_Register_160_to_191",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_IRR6 = OrderedDict((
    ("Interrupt_Request_Register_192_to_223",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_IRR7 = OrderedDict((
    ("Interrupt_Request_Register_224_to_255",   "Q:32"),
    ("Reserved",    "Q:32"),
))

IA32_X2APIC_ESR = OrderedDict((
    ("Reserved1",                   "Q:4"),
    ("Redirectible_IPI",            "Q:1"),
    ("Send Illegal_Vector",         "Q:1"),
    ("Received_Illegal_Vector",     "Q:1"),
    ("Illegal_Register_Address",    "Q:1"),
    ("Reserved2",                   "Q:56"),
))

IA32_X2APIC_LVT_CMCI = OrderedDict((
    ("Vector",                  "Q:8"),
    ("Delivery_Mode",           "Q:3"),
    ("Reserved1",               "Q:1"),
    ("Delivery_Status",         "Q:1"),
    ("Reserved2",               "Q:3"),
    ("Mask",                    "Q:1"),
    ("Reserved3",               "Q:47"),
))

IA32_X2APIC_ICR = OrderedDict((
    ("Vector",                  "Q:8"),
    ("Delivery_Mode",           "Q:3"),
    ("Destination_Mode",        "Q:1"),
    ("Reserved1",               "Q:2"),
    ("Level",                   "Q:1"),
    ("Trigger_Mode",            "Q:1"),
    ("Reserved2",               "Q:2"),
    ("Destination_Shorthand",   "Q:2"),
    ("Reserved3",               "Q:12"),
    ("Destination_Field",       "Q:32"),
))

IA32_X2APIC_LVT_TIMER = OrderedDict((
    ("Vector",                  "Q:8"),
    ("Reserved1",               "Q:4"),
    ("Delivery_Status",         "Q:1"),
    ("Reserved2",               "Q:3"),
    ("Mask",                    "Q:1"),
    ("Timer_Mode",              "Q:2"),
    ("Reserved3",               "Q:45"),
))

IA32_X2APIC_LVT_THERMAL = OrderedDict((
    ("Vector",                  "Q:8"),
    ("Delivery_Mode",           "Q:3"),
    ("Reserved1",               "Q:1"),
    ("Delivery_Status",         "Q:1"),
    ("Reserved2",               "Q:3"),
    ("Mask",                    "Q:1"),
    ("Reserved3",               "Q:47"),
))

IA32_X2APIC_LVT_PMI = OrderedDict((
    ("Vector",                  "Q:8"),
    ("Delivery_Mode",           "Q:3"),
    ("Reserved1",               "Q:1"),
    ("Delivery_Status",         "Q:1"),
    ("Reserved2",               "Q:3"),
    ("Mask",                    "Q:1"),
    ("Reserved3",               "Q:47"),
))

IA32_X2APIC_LVT_LINT0 = OrderedDict((
    ("Vector",                          "Q:8"),
    ("Delivery_Mode",                   "Q:3"),
    ("Reserved1",                       "Q:1"),
    ("Delivery_Status",                 "Q:1"),
    ("Interrupt_Input_Pin_Polarity",    "Q:1"),
    ("Remote_IRR",                      "Q:1"),
    ("Trigger_Mode",                    "Q:1"),
    ("Mask",                            "Q:1"),
    ("Reserved3",                       "Q:47"),
))

IA32_X2APIC_LVT_LINT1 = OrderedDict((
    ("Vector",                          "Q:8"),
    ("Delivery_Mode",                   "Q:3"),
    ("Reserved1",                       "Q:1"),
    ("Delivery_Status",                 "Q:1"),
    ("Interrupt_Input_Pin_Polarity",    "Q:1"),
    ("Remote_IRR",                      "Q:1"),
    ("Trigger_Mode",                    "Q:1"),
    ("Mask",                            "Q:1"),
    ("Reserved3",                       "Q:47"),
))

IA32_X2APIC_LVT_ERROR = OrderedDict((
    ("Vector",                  "Q:8"),
    ("Reserved1",               "Q:4"),
    ("Delivery_Status",         "Q:1"),
    ("Reserved2",               "Q:3"),
    ("Mask",                    "Q:1"),
    ("Reserved3",               "Q:47"),
))

IA32_X2APIC_INIT_COUNT = OrderedDict((
    ("Initial_Count",   "Q:32"),
    ("Reserved",        "Q:32"),
))

IA32_X2APIC_CUR_COUNT = OrderedDict((
    ("Current_Count",   "Q:32"),
    ("Reserved",        "Q:32"),
))

IA32_X2APIC_DIV_CONF = OrderedDict((
    ("Divide_Value1",   "Q:2"),
    ("Reserved1",       "Q:1"),
    ("Divide_Value2",   "Q:1"),
    ("Reserved2",       "Q:60"),
))

IA32_X2APIC_SELF_IPI = OrderedDict((
    ("Vector",      "Q:8"),
    ("Reserved",    "Q:56"),
))

MSR_DEFS = {
          0x1B  :   "O#IA32_APIC_BASE",
          0x3A  :   "O#IA32_FEATURE_CONTROL",
         0x1A0  :   "O#IA32_MISC_ENABLE",
         0x1A4  :   "O#MSR_MISC_FEATURE_CONTROL",
         0x802  :   "O#IA32_X2APIC_APICID",
         0x803  :   "O#IA32_X2APIC_VERSION",
         0x808  :   "O#IA32_X2APIC_TPR",
         0x80A  :   "O#IA32_X2APIC_PPR",
         0x80B  :   "O#IA32_X2APIC_EOI",
         0x80D  :   "O#IA32_X2APIC_LDR",
         0x80F  :   "O#IA32_X2APIC_SIVR",
         0x810  :   "O#IA32_X2APIC_ISR0",
         0x811  :   "O#IA32_X2APIC_ISR1",
         0x812  :   "O#IA32_X2APIC_ISR2",
         0x813  :   "O#IA32_X2APIC_ISR3",
         0x814  :   "O#IA32_X2APIC_ISR4",
         0x815  :   "O#IA32_X2APIC_ISR5",
         0x816  :   "O#IA32_X2APIC_ISR6",
         0x817  :   "O#IA32_X2APIC_ISR7",
         0x818  :   "O#IA32_X2APIC_TMR0",
         0x819  :   "O#IA32_X2APIC_TMR1",
         0x81A  :   "O#IA32_X2APIC_TMR2",
         0x81B  :   "O#IA32_X2APIC_TMR3",
         0x81C  :   "O#IA32_X2APIC_TMR4",
         0x81D  :   "O#IA32_X2APIC_TMR5",
         0x81E  :   "O#IA32_X2APIC_TMR6",
         0x81F  :   "O#IA32_X2APIC_TMR7",
         0x820  :   "O#IA32_X2APIC_IRR0",
         0x821  :   "O#IA32_X2APIC_IRR1",
         0x822  :   "O#IA32_X2APIC_IRR2",
         0x823  :   "O#IA32_X2APIC_IRR3",
         0x824  :   "O#IA32_X2APIC_IRR4",
         0x825  :   "O#IA32_X2APIC_IRR5",
         0x826  :   "O#IA32_X2APIC_IRR6",
         0x827  :   "O#IA32_X2APIC_IRR7",
         0x828  :   "O#IA32_X2APIC_ESR",
         0x82F  :   "O#IA32_X2APIC_LVT_CMCI",
         0x830  :   "O#IA32_X2APIC_ICR",
         0x832  :   "O#IA32_X2APIC_LVT_TIMER",
         0x833  :   "O#IA32_X2APIC_LVT_THERMAL",
         0x834  :   "O#IA32_X2APIC_LVT_PMI",
         0x835  :   "O#IA32_X2APIC_LVT_LINT0",
         0x836  :   "O#IA32_X2APIC_LVT_LINT1",
         0x837  :   "O#IA32_X2APIC_LVT_ERROR",
         0x838  :   "O#IA32_X2APIC_INIT_COUNT",
         0x839  :   "O#IA32_X2APIC_CUR_COUNT",
         0x83E  :   "O#IA32_X2APIC_DIV_CONF",
         0x83F  :   "O#IA32_X2APIC_SELF_IPI",
    0xC0000080  :   "O#IA32_EFER",
}

class MsrHelperClass(object):
    def __init__(self):
        pass

    def __getitem__(self, Index):
        Data = mem("Q")
        Data.VALUE = _ets.rdmsr(Index)
        Data.CAST(MSR_DEFS[Index])
        return Data

    def __setitem__(self, Index, Value):
        if type(Value) == mem:
            Value.CAST('Q')
            MsrVal = Value.VALUE
        else:
            MsrVal = Value
        _ets.wrmsr(Index, MsrVal)

MSR = MsrHelperClass()

if __name__ == "__main__":
    import sys

    value = MSR[int(sys.argv[0])]
    for name in value:
        if name.startswith("Reserved"):
            continue
        print("%s: %d" % (name.replace("_", " "), getattr(value, name)))

