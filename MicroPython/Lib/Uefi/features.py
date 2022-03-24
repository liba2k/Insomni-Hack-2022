## @file
# Hardware feature class definition.
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

from ucollections import OrderedDict as SETTINGS
from register import REG
from cpuid import CPUID
from msr import MSR

PROCESSOR_FEATURES = {
    "VMX" : {
        "Description"       :   "Virtual-Machine Extentions",
        "{Support}"         :   SETTINGS((
                                    ("CPUID[01].ECX.VMX", 1),
                                )),
        "{Enable}"          :   SETTINGS((
                                    ("REG.CR4.VMXE", 1),
                                )),
        "{Disable}"         :   SETTINGS((
                                    ("REG.CR4.VMXE", 0),
                                )),
        "(Capabilities)"    :   [],
        "[RelatedSettings]" :   ["MSR[0x3A].Lock_bit",
                                 "MSR[0x3A].Enable_VMX_inside_SMX_operation",
                                 "MSR[0x3A].Enable_VMX_outside_SMX_operation"],
    },

    "SMX" : {
        "Description"       :   "Safer Mode Extentions",
        "{Support}"         :   SETTINGS((
                                    ("CPUID[01].ECX.SMX", 1),
                                )),
        "{Enable}"          :   SETTINGS((
                                    ("REG.CR4.SMXE", 1),
                                )),
        "{Disable}"         :   SETTINGS((
                                    ("REG.CR4.SMXE", 0),
                                )),
        "(Capabilities)"    :   [],
        "[RelatedSettings]" :   ["MSR[0x3A].Lock_bit",
                                 "MSR[0x3A].Enable_VMX_inside_SMX_operation",
                                 "MSR[0x3A].Enable_VMX_outside_SMX_operation",
                                 "MSR[0x3A].SENTER_Local_Function_Enables",
                                 "MSR[0x3A].SENTER_Global_Enable"],
    },

    "SGX" : {
        "Description"       :   "Software Guard Extentions",
        "{Support}"         :   SETTINGS((
                                    ("CPUID[07].EBX.SGX", 1),
                                )),
        "{Enable}"          :   SETTINGS((
                                    ("REG.CR4.SMXE", 1),
                                )),
        "{Disable}"         :   SETTINGS((
                                    ("REG.CR4.SMXE", 0),
                                )),
        "(Capabilities)"    :   ["CPUID[0x12,0].EAX",
                                 "CPUID[0x12,0].EBX",
                                 "CPUID[0x12,0].EDX",
                                 "CPUID[0x12,1].EAX",
                                 "CPUID[0x12,1].EBX",
                                 "CPUID[0x12,1].ECX",
                                 "CPUID[0x12,1].EDX",
                                 "CPUID[0x12,2].EAX",
                                 "CPUID[0x12,2].EBX",
                                 "CPUID[0x12,2].ECX",
                                 "CPUID[0x12,2].EDX",
                                 ],
        "[RelatedSettings]" :   ["MSR[0x3A].Lock_bit",
                                 "MSR[0x3A].SGX_Launch_Control_Enable",
                                 "MSR[0x3A].SGX_Global_Enable"],
    },

    "APIC" : {
        "Description"       :   "Local APIC",
        "{Support}"         :   SETTINGS((
                                    ("CPUID[01].EDX.APIC", 1),
                                )),
        "{Enable}"          :   SETTINGS((
                                    ("MSR[0x1B].APIC_Global_Enable", 1),
                                )),
        "{Disable}"         :   SETTINGS((
                                    ("MSR[0x1B].APIC_Global_Enable", 0),
                                    ("MSR[0x80F].APIC_Software_Enable", 0),
                                )),
        "(Capabilities)"    :   [],
        "[RelatedSettings]" :   ["MSR[0x3A].Lock_bit",
                                 "MSR[0x3A].SGX_Launch_Control_Enable",
                                 "MSR[0x3A].SGX_Global_Enable"],
    },

    "X2APIC" : {
        "Description"       :   "Extended XAPIC",
        "{Support}"         :   SETTINGS((
                                    ("CPUID[01].ECX.x2APIC", 1),
                                )),
        "{Enable}"          :   SETTINGS((
                                    ("MSR[0x1B].APIC_Global_Enable", 1),
                                    ("MSR[0x1B].Enable_x2APIC_mode", 1),
                                )),
        "{Disable}"         :   SETTINGS((
                                    ("MSR[0x1B].Enable_x2APIC_mode", 0),
                                )),
        "(Capabilities)"    :   [],
        "[RelatedSettings]" :   ["MSR[0x802]",
                                 "MSR[0x803]",
                                 "MSR[0x808]",
                                 "MSR[0x80A]",
                                 "MSR[0x80B]",
                                 "MSR[0x80D]",
                                 "MSR[0x80F]",
                                 "MSR[0x810]",
                                 "MSR[0x811]",
                                 "MSR[0x812]",
                                 "MSR[0x813]",
                                 "MSR[0x814]",
                                 "MSR[0x815]",
                                 "MSR[0x816]",
                                 "MSR[0x817]",
                                 "MSR[0x818]",
                                 "MSR[0x819]",
                                 "MSR[0x81A]",
                                 "MSR[0x81B]",
                                 "MSR[0x81C]",
                                 "MSR[0x81D]",
                                 "MSR[0x81E]",
                                 "MSR[0x81F]",
                                 "MSR[0x820]",
                                 "MSR[0x821]",
                                 "MSR[0x822]",
                                 "MSR[0x823]",
                                 "MSR[0x824]",
                                 "MSR[0x825]",
                                 "MSR[0x826]",
                                 "MSR[0x827]",
                                 "MSR[0x828]",
                                 "MSR[0x82F]",
                                 "MSR[0x830]",
                                 "MSR[0x832]",
                                 "MSR[0x833]",
                                 "MSR[0x834]",
                                 "MSR[0x835]",
                                 "MSR[0x836]",
                                 "MSR[0x837]",
                                 "MSR[0x838]",
                                 "MSR[0x839]",
                                 "MSR[0x83E]",
                                 "MSR[0x83F]",
                                 ],
    },

}

class FeatureClass(object):
    DESC = {}

    def __new__(Class, FeatureDesc):
        for Obj in Class.DESC:
            if Class.DESC[Obj] == FeatureDesc:
                return Obj
        return super(Class, FeatureClass).__new__(Class)

    def __init__(self, FeatureDesc):
        FeatureClass.DESC[self] = FeatureDesc

    def __getattr__(self, Name):
        Desc = FeatureClass.DESC[self]

        if Name in Desc:
            return Desc[Name]

        ActName = "{%s}" % Name
        if ActName in Desc:
            for Cond in Desc[ActName]:
                if eval("%s != %s" % (Cond, Desc[ActName][Cond])):
                    return False
            return True

        ActName = "[%s]" % Name
        if ActName in Desc:
            Result = {}
            for Cond in Desc[ActName]:
                try:
                    Result[Cond] = eval(Cond)
                except:
                    Result[Cond] = None
            return Result

        return None

    def __setattr__(self, Name, Settings):
        Desc = FeatureClass.DESC[self]

        ActName = "{%s}" % Name
        if ActName in Desc:
            for Reg in Desc[ActName]:
                if Reg in Settings:
                    Data = Settings[Reg]
                else:
                    Data = Desc[ActName][Reg]
                eval("%s = %s" % (Reg, Data))

class FeatureHelperClass(object):
    def __getattr__(self, Name):
        if Name in PROCESSOR_FEATURES:
            return FeatureClass(PROCESSOR_FEATURES[Name])
        return None

FEATURE = FeatureHelperClass()

if __name__ == "__main__":
    import sys

    feature = getattr(FEATURE, sys.argv[0])
    print (feature.Description)
    for item in ["Support", "Enable", "RelatedSettings"]:
        result = getattr(feature, item)
        if isinstance(result, dict) or isinstance(result, SETTINGS):
            print("  %s:" % item)
            for n in result:
                print("    %s:" % n, result[n])
        else:
            print("  %s:" % item, result)

