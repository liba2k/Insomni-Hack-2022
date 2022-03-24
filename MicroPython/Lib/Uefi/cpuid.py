## @file
# MicroPython wrapper of cpuid
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

CPUID_00 = {
    "EAX"   :   "I",
    "EBX"   :   "4a",
    "ECX"   :   "4a",
    "EDX"   :   "4a",
}

CPUID_01 = {
    "EAX"   :   OrderedDict((
                    ("Stepping_ID",         "I:4"),
                    ("Model",               "I:4"),
                    ("Family_ID",           "I:4"),
                    ("Processor_Type",      "I:2"),
                    ("Reserved1",           "I:2"),
                    ("Extended_Model_ID",   "I:4"),
                    ("Extended_Family_ID",  "I:8"),
                    ("Reserved2",           "I:4"),
                )),
    "EBX"   :   OrderedDict((
                    ("Brand_Index",             "I:8"),
                    ("CLFLUSH_line_size",       "I:8"),
                    ("Maximum_addressable_IDs", "I:8"),
                    ("Initial_APIC_ID",         "I:8"),
                )),
    "ECX"   :   OrderedDict((
                    ("SSE3",                "I:1"),
                    ("PCLMULQDQ",           "I:1"),
                    ("DTES64",              "I:1"),
                    ("MONITOR",             "I:1"),
                    ("DSCPL",               "I:1"),
                    ("VMX",                 "I:1"),
                    ("SMX",                 "I:1"),
                    ("EIST",                "I:1"),
                    ("TM2",                 "I:1"),
                    ("SSSE3",               "I:1"),
                    ("CNXTID",              "I:1"),
                    ("SDBG",                "I:1"),
                    ("FMA",                 "I:1"),
                    ("CMPXCHG16B",          "I:1"),
                    ("xTPR_Update_Control", "I:1"),
                    ("PDCM",                "I:1"),
                    ("Reserved1",           "I:1"),
                    ("PCID",                "I:1"),
                    ("DCA",                 "I:1"),
                    ("SSE41",               "I:1"),
                    ("SSE42",               "I:1"),
                    ("x2APIC",              "I:1"),
                    ("MOVBE",               "I:1"),
                    ("POPCNT",              "I:1"),
                    ("TSC_Deadline",        "I:1"),
                    ("AESNI",               "I:1"),
                    ("XSAVE",               "I:1"),
                    ("OSXSAVE",             "I:1"),
                    ("AVX",                 "I:1"),
                    ("F16C",                "I:1"),
                    ("RDRAND",              "I:1"),
                    ("Reserved2",           "I:1"),
                )),
    "EDX"   :   OrderedDict((
                    ("FPU",         "I:1"),
                    ("VME",         "I:1"),
                    ("DE",          "I:1"),
                    ("PSE",         "I:1"),
                    ("TSC",         "I:1"),
                    ("MSR",         "I:1"),
                    ("PAE",         "I:1"),
                    ("MCE",         "I:1"),
                    ("CX8",         "I:1"),
                    ("APIC",        "I:1"),
                    ("Reserved1",   "I:1"),
                    ("SEP",         "I:1"),
                    ("MTRR",        "I:1"),
                    ("PGE",         "I:1"),
                    ("MCA",         "I:1"),
                    ("CMOV",        "I:1"),
                    ("PAT",         "I:1"),
                    ("PSE36",       "I:1"),
                    ("PSN",         "I:1"),
                    ("CLFSH",       "I:1"),
                    ("Reserved2",   "I:1"),
                    ("DS",          "I:1"),
                    ("ACPI",        "I:1"),
                    ("MMX",         "I:1"),
                    ("FXSR",        "I:1"),
                    ("SSE",         "I:1"),
                    ("SSE2",        "I:1"),
                    ("SS",          "I:1"),
                    ("HTT",         "I:1"),
                    ("TM",          "I:1"),
                    ("Reserved3",   "I:1"),
                    ("PBE",         "I:1"),
                )),
}

CPUID_07_00 = {
    "EAX"   :   OrderedDict((
                    ("Maximum_Subleaves",   "I:32"),
                )),
    "EBX"   :   OrderedDict((
                    ("FSGSBASE",                "I:1"),
                    ("MSR_3B",                  "I:1"),
                    ("SGX",                     "I:1"),
                    ("BMI1",                    "I:1"),
                    ("HLE",                     "I:1"),
                    ("AVX2",                    "I:1"),
                    ("FDP_EXCPTN_ONLY",         "I:1"),
                    ("SMEP",                    "I:1"),
                    ("BMI2",                    "I:1"),
                    ("Enhanced_REP_MOVSB",      "I:1"),
                    ("INVPCID",                 "I:1"),
                    ("RTM",                     "I:1"),
                    ("RDT_M",                   "I:1"),
                    ("Deprecates_FPU_CS_DS",    "I:1"),
                    ("MPX",                     "I:1"),
                    ("PDCM",                    "I:1"),
                    ("RDT_A",                   "I:1"),
                    ("Reserved1",               "I:2"),
                    ("RDSEED",                  "I:1"),
                    ("ADX",                     "I:1"),
                    ("SMAP",                    "I:1"),
                    ("Reserved2",               "I:2"),
                    ("CLFLUSHOPT",              "I:1"),
                    ("CLWB",                    "I:1"),
                    ("Intel_Processor_Trace",   "I:1"),
                    ("Reserved3",               "I:3"),
                    ("SHA",                     "I:1"),
                    ("Reserved4",               "I:2"),
                )),
    "ECX"   :   OrderedDict((
                    ("PREFETCHWT1",     "I:1"),
                    ("Reserved1",       "I:1"),
                    ("UMIP",            "I:1"),
                    ("PKU",             "I:1"),
                    ("OSPKE",           "I:1"),
                    ("Reserved2",       "I:12"),
                    ("MAWAU",           "I:5"),
                    ("RDPID",           "I:1"),
                    ("Reserved3",       "I:7"),
                    ("SGX_LC",          "I:1"),
                    ("Reserved4",       "I:1"),
                )),
    "EDX"   :   OrderedDict((
                    ("Reserved",   "I:32"),
                )),
}

CPUID_07_00 = {
    "EAX"   :   OrderedDict((
                    ("SGX1",        "I:1"),
                    ("SGX2",        "I:1"),
                    ("Reserved1",   "I:30"),
                )),
    "EBX"   :   OrderedDict((
                    ("MISCSELECT",  "I:32"),
                )),
    "ECX"   :   OrderedDict((
                    ("Reserved",       "I:32"),
                )),
    "EDX"   :   OrderedDict((
                    ("MaxEnclaveSize_Not64",    "I:8"),
                    ("MaxEnclaveSize_64",       "I:8"),
                    ("Reserved",                "I:16"),
                )),
}

CPUID_07_01 = {
    "EAX"   :   OrderedDict((
                    ("SECS_ATTRIBUTES_0_31",    "I:32"),
                )),
    "EBX"   :   OrderedDict((
                    ("SECS_ATTRIBUTES_32_63",   "I:32"),
                )),
    "ECX"   :   OrderedDict((
                    ("SECS_ATTRIBUTES_64_95",   "I:32"),
                )),
    "EDX"   :   OrderedDict((
                    ("SECS_ATTRIBUTES_96_127",  "I:32"),
                )),
}

CPUID_07_02 = {
    "EAX"   :   OrderedDict((
                    ("Subleaf_status",          "I:4"),
                    ("Reserved1",               "I:8"),
                    ("EPC_section_base_12_31",  "I:20"),
                )),
    "EBX"   :   OrderedDict((
                    ("EPC_section_base_32_51",  "I:20"),
                    ("Reserved1",               "I:12"),
                )),
    "ECX"   :   OrderedDict((
                    ("Subleaf_status",          "I:4"),
                    ("Reserved1",               "I:8"),
                    ("EPC_section_size_12_31",  "I:20"),
                )),
    "EDX"   :   OrderedDict((
                    ("EPC_section_size_32_51",  "I:20"),
                    ("Reserved1",               "I:12"),
                )),
}

CPUID_DEFS = {
    0x00    :   [CPUID_00],
    0x01    :   [CPUID_01],
    0x07    :   [CPUID_07_00, CPUID_07_01],
}

class CpuidValue(object):
    def __init__(self, Eax, Ebx, Ecx, Edx):
        self.EAX = Eax
        self.EBX = Ebx
        self.ECX = Ecx
        self.EDX = Edx

class CpuidHelperClass(object):
    def __init__(self):
        pass

    def __getitem__(self, Index):
        if type(Index) in [list, tuple]:
            Index1, Index2 = Index
        else:
            Index1 = Index
            Index2 = 0

        if Index1 not in CPUID_DEFS or Index2 >= len(CPUID_DEFS[Index1]):
            raise(Exception("Not supported cpuid: EAX=0x%x (ECX=%d)" % (Index1, Index2)))

        Value = OrderedDict()
        Value['EAX'], Value['EBX'], Value['ECX'], Value['EDX'] = _ets.cpuid(Index1, Index2)
        for Reg in CPUID_DEFS[Index1][Index2]:
            Data = mem("I")
            Data.VALUE = Value[Reg]
            Data.CAST(CPUID_DEFS[Index1][Index2][Reg])
            Value[Reg] = Data

        return CpuidValue(Value['EAX'], Value['EBX'], Value['ECX'], Value['EDX'])

CPUID = CpuidHelperClass()

if __name__ == "__main__":
    import sys
    value = CPUID[int(sys.argv[0]),0]
    for reg in ["EAX", "EBX", "EDX", "ECX"]:
        reg = getattr(value, reg)
        for name in reg:
            if name.startswith("Reserved"):
                continue
            print("%s: %d" % (name.replace("_", " "), getattr(reg, name)))

