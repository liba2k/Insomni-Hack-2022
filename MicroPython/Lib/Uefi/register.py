## @file
# Definitions of processor registers.
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

from _uefi import mem
import _ets

from ucollections import OrderedDict

CR0_DEF = OrderedDict((
    ("PE",          "Q:1"),
    ("MP",          "Q:1"),
    ("EM",          "Q:1"),
    ("TS",          "Q:1"),
    ("ET",          "Q:1"),
    ("NE",          "Q:1"),
    ("Reserved1",   "Q:10"),
    ("WP",          "Q:1"),
    ("Reserved2",   "Q:1"),
    ("AM",          "Q:1"),
    ("Reserved3",   "Q:10"),
    ("NW",          "Q:1"),
    ("CD",          "Q:1"),
    ("PG",          "Q:1"),
    ("Reserved",    "Q:32"),
))

CR3_DEF = OrderedDict((
    ("Reserved1",           "Q:3"),
    ("PWT",                 "Q:1"),
    ("PCD",                 "Q:1"),
    ("Reserved2",           "Q:7"),
    ("Page_Directory_Base", "Q:52"),
))

CR4_DEF = OrderedDict((
    ("VME",         "Q:1"),
    ("PVI",         "Q:1"),
    ("TSD",         "Q:1"),
    ("DE",          "Q:1"),
    ("PSE",         "Q:1"),
    ("PAE",         "Q:1"),
    ("MCE",         "Q:1"),
    ("PGE",         "Q:1"),
    ("PCE",         "Q:1"),
    ("OSFXSR",      "Q:1"),
    ("OSXMMEXCPT",  "Q:1"),
    ("UMIP",        "Q:1"),
    ("Reserved1",   "Q:1"),
    ("VMXE",        "Q:1"),
    ("SMXE",        "Q:1"),
    ("Reserved2",   "Q:1"),
    ("FSGSBASE",    "Q:1"),
    ("PCIDE",       "Q:1"),
    ("OSXSAVE",     "Q:1"),
    ("Reserved3",   "Q:1"),
    ("SMEP",        "Q:1"),
    ("SMAP",        "Q:1"),
    ("PKE",         "Q:1"),
    ("Reserved4",   "Q:41"),
))

REG_DEFS = {
    "CR0"   :   "O#CR0_DEF",
    "CR3"   :   "O#CR3_DEF",
    "CR4"   :   "O#CR4_DEF",
}

class RegisterHelperClass(object):
    def __getattr__(self, Name):
        Value = getattr(_ets.regs, Name.lower())
        print(Name,'=',Value)
        if Name in REG_DEFS:
            Data = mem('Q')
            Data.VALUE = Value
            Data.CAST(REG_DEFS[Name])
        else:
            Data = Value
        return Data

    def __setattr__(self, Name, Value):
        setattr(_ets.regs, Name.lower(), Value)

REG = RegisterHelperClass()

if __name__ == "__main__":
    pass

