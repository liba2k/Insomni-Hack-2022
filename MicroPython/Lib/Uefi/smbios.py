## @file
# Definitions of SMBIOS standard.
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
from ucollections import OrderedDict
from protocols import *

import uefi

SMBIOS_STRUCTURE = OrderedDict((
    ("Type",    'B'),
    ("Length",  'B'),
    ("Handle",  'H')
))

EFI_SMBIOS_PROTOCOL = OrderedDict((
  ("Add",           'FE(PO#EFI_SMBIOS_PROTOCOL,T,PH,PO#SMBIOS_STRUCTURE)'),
  ("UpdateString",  'FE(PO#EFI_SMBIOS_PROTOCOL,PH,PN,S)'),
  ("Remove",        'FE(PO#EFI_SMBIOS_PROTOCOL,H)'),
  ("GetNext",       'FE(PO#EFI_SMBIOS_PROTOCOL,PH,PB,PPO#SMBIOS_STRUCTURE,PT)'),
  ("MajorVersion",  'B'),
  ("MinorVersion",  'B')
))

SMBIOS_TYPES = {
    "BIOS_INFORMATION"                      : 0,
    "Type0"                                 : 0,
    "SYSTEM_INFORMATION"                    : 1,
    "Type1"                                 : 1,
    "BASEBOARD_INFORMATION"                 : 2,
    "Type2"                                 : 2,
    "SYSTEM_ENCLOSURE"                      : 3,
    "Type3"                                 : 3,
    "PROCESSOR_INFORMATION"                 : 4,
    "Type4"                                 : 4,
    "MEMORY_CONTROLLER_INFORMATION"         : 5,
    "Type5"                                 : 5,
    "MEMORY_MODULE_INFORMATON"              : 6,
    "Type6"                                 : 6,
    "CACHE_INFORMATION"                     : 7,
    "Type7"                                 : 7,
    "PORT_CONNECTOR_INFORMATION"            : 8,
    "Type8"                                 : 8,
    "SYSTEM_SLOTS"                          : 9,
    "Type9"                                 : 9,
    "ONBOARD_DEVICE_INFORMATION"            : 10,
    "Type10"                                : 10,
    "OEM_STRINGS"                           : 11,
    "Type11"                                : 11,
    "SYSTEM_CONFIGURATION_OPTIONS"          : 12,
    "Type12"                                : 12,
    "BIOS_LANGUAGE_INFORMATION"             : 13,
    "Type13"                                : 13,
    "GROUP_ASSOCIATIONS"                    : 14,
    "Type14"                                : 14,
    "SYSTEM_EVENT_LOG"                      : 15,
    "Type15"                                : 15,
    "PHYSICAL_MEMORY_ARRAY"                 : 16,
    "Type16"                                : 16,
    "MEMORY_DEVICE"                         : 17,
    "Type17"                                : 17,
    "32BIT_MEMORY_ERROR_INFORMATION"        : 18,
    "Type18"                                : 18,
    "MEMORY_ARRAY_MAPPED_ADDRESS"           : 19,
    "Type19"                                : 19,
    "MEMORY_DEVICE_MAPPED_ADDRESS"          : 20,
    "Type20"                                : 20,
    "BUILT_IN_POINTING_DEVICE"              : 21,
    "Type21"                                : 21,
    "PORTABLE_BATTERY"                      : 22,
    "Type22"                                : 22,
    "SYSTEM_RESET"                          : 23,
    "Type23"                                : 23,
    "HARDWARE_SECURITY"                     : 24,
    "Type24"                                : 24,
    "SYSTEM_POWER_CONTROLS"                 : 25,
    "Type25"                                : 25,
    "VOLTAGE_PROBE"                         : 26,
    "Type26"                                : 26,
    "COOLING_DEVICE"                        : 27,
    "Type27"                                : 27,
    "TEMPERATURE_PROBE"                     : 28,
    "Type28"                                : 28,
    "ELECTRICAL_CURRENT_PROBE"              : 29,
    "Type29"                                : 29,
    "OUT_OF_BAND_REMOTE_ACCESS"             : 30,
    "Type30"                                : 30,
    "BOOT_INTEGRITY_SERVICE"                : 31,
    "Type31"                                : 31,
    "SYSTEM_BOOT_INFORMATION"               : 32,
    "Type32"                                : 32,
    "64BIT_MEMORY_ERROR_INFORMATION"        : 33,
    "Type33"                                : 33,
    "MANAGEMENT_DEVICE"                     : 34,
    "Type34"                                : 34,
    "MANAGEMENT_DEVICE_COMPONENT"           : 35,
    "Type35"                                : 35,
    "MANAGEMENT_DEVICE_THRESHOLD_DATA"      : 36,
    "Type36"                                : 36,
    "MEMORY_CHANNEL"                        : 37,
    "Type37"                                : 37,
    "IPMI_DEVICE_INFORMATION"               : 38,
    "Type38"                                : 38,
    "SYSTEM_POWER_SUPPLY"                   : 39,
    "Type39"                                : 39,
    "ADDITIONAL_INFORMATION"                : 40,
    "Type40"                                : 40,
    "ONBOARD_DEVICES_EXTENDED_INFORMATION"  : 41,
    "Type41"                                : 41,
    "MANAGEMENT_CONTROLLER_HOST_INTERFACE"  : 42,
    "Type42"                                : 42,
    "TPM_DEVICE"                            : 43,
    "Type43"                                : 43,
}

SMBIOS_HANDLE = "H"
SMBIOS_TABLE_STRING = "B"

MISC_BIOS_CHARACTERISTICS = OrderedDict((
    ("Reserved",                          "Q:2"),
    ("Unknown",                           "Q:1"),
    ("BiosCharacteristicsNotSupported",   "Q:1"),
    ("IsaIsSupported",                    "Q:1"),
    ("McaIsSupported",                    "Q:1"),
    ("EisaIsSupported",                   "Q:1"),
    ("PciIsSupported",                    "Q:1"),
    ("PcmciaIsSupported",                 "Q:1"),
    ("PlugAndPlayIsSupported",            "Q:1"),
    ("ApmIsSupported",                    "Q:1"),
    ("BiosIsUpgradable",                  "Q:1"),
    ("BiosShadowingAllowed",              "Q:1"),
    ("VlVesaIsSupported",                 "Q:1"),
    ("EscdSupportIsAvailable",            "Q:1"),
    ("BootFromCdIsSupported",             "Q:1"),
    ("SelectableBootIsSupported",         "Q:1"),
    ("RomBiosIsSocketed",                 "Q:1"),
    ("BootFromPcmciaIsSupported",         "Q:1"),
    ("EDDSpecificationIsSupported",       "Q:1"),
    ("JapaneseNecFloppyIsSupported",      "Q:1"),
    ("JapaneseToshibaFloppyIsSupported",  "Q:1"),
    ("Floppy525_360IsSupported",          "Q:1"),
    ("Floppy525_12IsSupported",           "Q:1"),
    ("Floppy35_720IsSupported",           "Q:1"),
    ("Floppy35_288IsSupported",           "Q:1"),
    ("PrintScreenIsSupported",            "Q:1"),
    ("Keyboard8042IsSupported",           "Q:1"),
    ("SerialIsSupported",                 "Q:1"),
    ("PrinterIsSupported",                "Q:1"),
    ("CgaMonoIsSupported",                "Q:1"),
    ("NecPc98",                           "Q:1"),
    ("ReservedForVendor",                 "Q:32"),
))

EXTENDED_BIOS_ROM_SIZE = OrderedDict((
  ("Size", "H:14"),
  ("Unit",  "H:2")
))


BASE_BOARD_FEATURE_FLAGS = OrderedDict((
    ("Motherboard",             "B:1"),
    ("RequiresDaughterCard",    "B:1"),
    ("Removable",               "B:1"),
    ("Replaceable",             "B:1"),
    ("HotSwappable",            "B:1"),
    ("Reserved",                "B:3"),
))

CONTAINED_ELEMENT = OrderedDict((
    ("ContainedElementType",    "B"),
    ("ContainedElementMinimum", "B"),
    ("ContainedElementMaximum", "B"),
))

PROCESSOR_VOLTAGE = OrderedDict((
    ("ProcessorVoltageCapability5V",        "B:1"),
    ("ProcessorVoltageCapability3_3V",      "B:1"),
    ("ProcessorVoltageCapability2_9V",      "B:1"),
    ("ProcessorVoltageCapabilityReserved",  "B:1"),
    ("ProcessorVoltageReserved",            "B:3"),
    ("ProcessorVoltageIndicateLegacy",      "B:1"),
))

PROCESSOR_SIGNATURE = OrderedDict((
    ("ProcessorSteppingId", "I:4"),
    ("ProcessorModel",      "I:4"),
    ("ProcessorFamily",     "I:4"),
    ("ProcessorType",       "I:2"),
    ("ProcessorReserved1",  "I:2"),
    ("ProcessorXModel",     "I:4"),
    ("ProcessorXFamily",    "I:8"),
    ("ProcessorReserved2",  "I:4"),
))

PROCESSOR_FEATURE_FLAGS = OrderedDict((
    ("ProcessorFpu",        "I:1"),
    ("ProcessorVme",        "I:1"),
    ("ProcessorDe",         "I:1"),
    ("ProcessorPse",        "I:1"),
    ("ProcessorTsc",        "I:1"),
    ("ProcessorMsr",        "I:1"),
    ("ProcessorPae",        "I:1"),
    ("ProcessorMce",        "I:1"),
    ("ProcessorCx8",        "I:1"),
    ("ProcessorApic",       "I:1"),
    ("ProcessorReserved1",  "I:1"),
    ("ProcessorSep",        "I:1"),
    ("ProcessorMtrr",       "I:1"),
    ("ProcessorPge",        "I:1"),
    ("ProcessorMca",        "I:1"),
    ("ProcessorCmov",       "I:1"),
    ("ProcessorPat",        "I:1"),
    ("ProcessorPse36",      "I:1"),
    ("ProcessorPsn",        "I:1"),
    ("ProcessorClfsh",      "I:1"),
    ("ProcessorReserved2",  "I:1"),
    ("ProcessorDs",         "I:1"),
    ("ProcessorAcpi",       "I:1"),
    ("ProcessorMmx",        "I:1"),
    ("ProcessorFxsr",       "I:1"),
    ("ProcessorSse",        "I:1"),
    ("ProcessorSse2",       "I:1"),
    ("ProcessorSs",         "I:1"),
    ("ProcessorReserved3",  "I:1"),
    ("ProcessorTm",         "I:1"),
    ("ProcessorReserved4",  "I:2"),
))

PROCESSOR_ID_DATA = OrderedDict((
    ("Signature",       "O#PROCESSOR_SIGNATURE"),
    ("FeatureFlags",    "O#PROCESSOR_FEATURE_FLAGS"),
))

MEMORY_ERROR_CORRECT_CAPABILITY = OrderedDict((
    ("Other",                   "B:1"),
    ("Unknown",                 "B:1"),
    ("None",                    "B:1"),
    ("SingleBitErrorCorrect",   "B:1"),
    ("DoubleBitErrorCorrect",   "B:1"),
    ("ErrorScrubbing",          "B:1"),
    ("Reserved",                "B:2"),
))

MEMORY_SPEED_TYPE = OrderedDict((
    ("Other",       "H:1"),
    ("Unknown",     "H:1"),
    ("SeventyNs",   "H:1"),
    ("SixtyNs",     "H:1"),
    ("FiftyNs",     "H:1"),
    ("Reserved",    "H:11"),
))

MEMORY_CURRENT_TYPE = OrderedDict((
    ("Other",       "H:1"),
    ("Unknown",     "H:1"),
    ("Standard",    "H:1"),
    ("FastPageMode","H:1"),
    ("Edo",         "H:1"),
    ("Parity",      "H:1"),
    ("Ecc",         "H:1"),
    ("Simm",        "H:1"),
    ("Dimm",        "H:1"),
    ("BurstEdo",    "H:1"),
    ("Sdram",       "H:1"),
    ("Reserved",    "H:5"),
))

MEMORY_INSTALLED_ENABLED_SIZE = OrderedDict((
    ("InstalledOrEnabledSize",  "B:7"),
    ("SingleOrDoubleBank",      "B:1"),
))

CACHE_SRAM_TYPE_DATA = OrderedDict((
    ("Other",           "H:1"),
    ("Unknown",         "H:1"),
    ("NonBurst",        "H:1"),
    ("Burst",           "H:1"),
    ("PipelineBurst",   "H:1"),
    ("Synchronous",     "H:1"),
    ("Asynchronous",    "H:1"),
    ("Reserved",        "H:9"),
))

MISC_SLOT_CHARACTERISTICS1 = OrderedDict((
    ("CharacteristicsUnknown",  "B:1"),
    ("Provides50Volts",         "B:1"),
    ("Provides33Volts",         "B:1"),
    ("SharedSlot",              "B:1"),
    ("PcCard16Supported",       "B:1"),
    ("CardBusSupported",        "B:1"),
    ("ZoomVideoSupported",      "B:1"),
    ("ModemRingResumeSupported","B:1"),
))

MISC_SLOT_CHARACTERISTICS2 = OrderedDict((
    ("PmeSignalSupported",      "B:1"),
    ("HotPlugDevicesSupported", "B:1"),
    ("SmbusSignalSupported",    "B:1"),
    ("Reserved",                "B:5"),
))

DEVICE_STRUCT = OrderedDict((
    ("DeviceType",          "B"),
    ("DescriptionString",   "O#SMBIOS_TABLE_STRING"),
))

GROUP_STRUCT = OrderedDict((
    ("ItemType",    "B"),
    ("ItemHandle",  "H"),
))

EVENT_LOG_TYPE = OrderedDict((
    ("LogType",         "B"),
    ("DataFormatType",  "B"),
))

MEMORY_DEVICE_TYPE_DETAIL = OrderedDict((
    ("Reserved",    "H:1"),
    ("Other",       "H:1"),
    ("Unknown",     "H:1"),
    ("FastPaged",   "H:1"),
    ("StaticColumn","H:1"),
    ("PseudoStatic","H:1"),
    ("Rambus",      "H:1"),
    ("Synchronous", "H:1"),
    ("Cmos",        "H:1"),
    ("Edo",         "H:1"),
    ("WindowDram",  "H:1"),
    ("CacheDram",   "H:1"),
    ("Nonvolatile", "H:1"),
    ("Registered",  "H:1"),
    ("Unbuffered",  "H:1"),
    ("LrDimm",      "H:1"),
))

MISC_VOLTAGE_PROBE_LOCATION = OrderedDict((
    ("VoltageProbeSite",    "B:5"),
    ("VoltageProbeStatus",  "B:3"),
))

MISC_COOLING_DEVICE_TYPE = OrderedDict((
    ("CoolingDevice",       "B:5"),
    ("CoolingDeviceStatus", "B:3"),
))

MISC_TEMPERATURE_PROBE_LOCATION = OrderedDict((
    ("TemperatureProbeSite",    "B:5"),
    ("TemperatureProbeStatus",  "B:3"),
))

MISC_ELECTRICAL_CURRENT_PROBE_LOCATION = OrderedDict((
    ("ElectricalCurrentProbeSite", "B:5"),
    ("ElectricalCurrentProbeStatus", "B:3"),
))

MEMORY_DEVICE = OrderedDict((
    ("DeviceLoad",   "B"),
    ("DeviceHandle", "H"),
))

SYS_POWER_SUPPLY_CHARACTERISTICS = OrderedDict((
    ("PowerSupplyHotReplaceable",   "H:1"),
    ("PowerSupplyPresent",          "H:1"),
    ("PowerSupplyUnplugged",        "H:1"),
    ("InputVoltageRangeSwitch",     "H:4"),
    ("PowerSupplyStatus",           "H:3"),
    ("PowerSupplyType",             "H:4"),
    ("Reserved",                    "H:2"),
))

ADDITIONAL_INFORMATION_ENTRY = OrderedDict((
    ("EntryLength",         "B"),
    ("ReferencedHandle",    "H"),
    ("ReferencedOffset",    "B"),
    ("EntryString",         "O#SMBIOS_TABLE_STRING"),
    ("Value",               "1B"),
))

SMBIOS_TABLE_TYPE0 = OrderedDict((
    ("Hdr",                                       "O#SMBIOS_STRUCTURE"),
    ("Vendor",                                    "O#SMBIOS_TABLE_STRING"),
    ("BiosVersion",                               "O#SMBIOS_TABLE_STRING"),
    ("BiosSegment",                               "H"),
    ("BiosReleaseDate",                           "O#SMBIOS_TABLE_STRING"),
    ("BiosSize",                                  "B"),
    ("BiosCharacteristics",                       "O#MISC_BIOS_CHARACTERISTICS"),
    ("BIOSCharacteristicsExtensionBytes",         "2B"),
    ("SystemBiosMajorRelease",                    "B"),
    ("SystemBiosMinorRelease",                    "B"),
    ("EmbeddedControllerFirmwareMajorRelease",    "B"),
    ("EmbeddedControllerFirmwareMinorRelease",    "B"),
    ("ExtendedBiosSize",                          "O#EXTENDED_BIOS_ROM_SIZE"),
))

SMBIOS_TABLE_TYPE1 = OrderedDict((
    ("Hdr",             "O#SMBIOS_STRUCTURE"),
    ("Manufacturer",    "O#SMBIOS_TABLE_STRING"),
    ("ProductName",     "O#SMBIOS_TABLE_STRING"),
    ("Version",         "O#SMBIOS_TABLE_STRING"),
    ("SerialNumber",    "O#SMBIOS_TABLE_STRING"),
    ("Uuid",            "G"),
    ("WakeUpType",      "B"),
    ("SKUNumber",       "O#SMBIOS_TABLE_STRING"),
    ("Family",          "O#SMBIOS_TABLE_STRING"),
))

SMBIOS_TABLE_TYPE2 = OrderedDict((
    ("Hdr",                             "O#SMBIOS_STRUCTURE"),
    ("Manufacturer",                    "O#SMBIOS_TABLE_STRING"),
    ("ProductName",                     "O#SMBIOS_TABLE_STRING"),
    ("Version",                         "O#SMBIOS_TABLE_STRING"),
    ("SerialNumber",                    "O#SMBIOS_TABLE_STRING"),
    ("AssetTag",                        "O#SMBIOS_TABLE_STRING"),
    ("FeatureFlag",                     "O#BASE_BOARD_FEATURE_FLAGS"),
    ("LocationInChassis",               "O#SMBIOS_TABLE_STRING"),
    ("ChassisHandle",                   "H"),
    ("BoardType",                       "B"),
    ("NumberOfContainedObjectHandles",  "B"),
    ("ContainedObjectHandles",          "1H"),
))

SMBIOS_TABLE_TYPE3 = OrderedDict((
    ("Hdr",                         "O#SMBIOS_STRUCTURE"),
    ("Manufacturer",                "O#SMBIOS_TABLE_STRING"),
    ("Type",                        "B"),
    ("Version",                     "O#SMBIOS_TABLE_STRING"),
    ("SerialNumber",                "O#SMBIOS_TABLE_STRING"),
    ("AssetTag",                    "O#SMBIOS_TABLE_STRING"),
    ("BootupState",                 "B"),
    ("PowerSupplyState",            "B"),
    ("ThermalState",                "B"),
    ("SecurityStatus",              "B"),
    ("OemDefined",                  "4B"),
    ("Height",                      "B"),
    ("NumberofPowerCords",          "B"),
    ("ContainedElementCount",       "B"),
    ("ContainedElementRecordLength","B"),
    ("ContainedElements",           "1O#CONTAINED_ELEMENT"),
))

SMBIOS_TABLE_TYPE4 = OrderedDict((
    ("Hdr",                         "O#SMBIOS_STRUCTURE"),
    ("Socket",                      "O#SMBIOS_TABLE_STRING"),
    ("ProcessorType",               "B"),
    ("ProcessorFamily",             "B"),
    ("ProcessorManufacture",        "O#SMBIOS_TABLE_STRING"),
    ("ProcessorId",                 "O#PROCESSOR_ID_DATA"),
    ("ProcessorVersion",            "O#SMBIOS_TABLE_STRING"),
    ("Voltage",                     "O#PROCESSOR_VOLTAGE"),
    ("ExternalClock",               "H"),
    ("MaxSpeed",                    "H"),
    ("CurrentSpeed",                "H"),
    ("Status",                      "B"),
    ("ProcessorUpgrade",            "B"),
    ("L1CacheHandle",               "H"),
    ("L2CacheHandle",               "H"),
    ("L3CacheHandle",               "H"),
    ("SerialNumber",                "O#SMBIOS_TABLE_STRING"),
    ("AssetTag",                    "O#SMBIOS_TABLE_STRING"),
    ("PartNumber",                  "B"),
    ("CoreCount",                   "B"),
    ("EnabledCoreCount",            "B"),
    ("ThreadCount",                 "B"),
    ("ProcessorCharacteristics",    "H"),
    ("ProcessorFamily2",            "H"),
    ("CoreCount2",                  "H"),
    ("EnabledCoreCount2",           "H"),
    ("ThreadCount2",                "H"),
))

SMBIOS_TABLE_TYPE5 = OrderedDict((
    ("Hdr",                         "O#SMBIOS_STRUCTURE"),
    ("ErrDetectMethod",             "B"),
    ("ErrCorrectCapability",        "O#MEMORY_ERROR_CORRECT_CAPABILITY"),
    ("SupportInterleave",           "B"),
    ("CurrentInterleave",           "B"),
    ("MaxMemoryModuleSize",         "B"),
    ("SupportSpeed",                "O#MEMORY_SPEED_TYPE"),
    ("SupportMemoryType",           "H"),
    ("MemoryModuleVoltage",         "B"),
    ("AssociatedMemorySlotNum",     "B"),
    ("MemoryModuleConfigHandles",   "1H"),
))

SMBIOS_TABLE_TYPE6 = OrderedDict((
    ("Hdr",                 "O#SMBIOS_STRUCTURE"),
    ("SocketDesignation",   "O#SMBIOS_TABLE_STRING"),
    ("BankConnections",     "B"),
    ("CurrentSpeed",        "B"),
    ("CurrentMemoryType",   "O#MEMORY_CURRENT_TYPE"),
    ("InstalledSize",       "O#MEMORY_INSTALLED_ENABLED_SIZE"),
    ("EnabledSize",         "O#MEMORY_INSTALLED_ENABLED_SIZE"),
    ("ErrorStatus",         "B"),
))

SMBIOS_TABLE_TYPE7 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("SocketDesignation", "O#SMBIOS_TABLE_STRING"),
    ("CacheConfiguration", "H"),
    ("MaximumCacheSize", "H"),
    ("InstalledSize", "H"),
    ("SupportedSRAMType", "O#CACHE_SRAM_TYPE_DATA"),
    ("CurrentSRAMType", "O#CACHE_SRAM_TYPE_DATA"),
    ("CacheSpeed", "B"),
    ("ErrorCorrectionType", "B"),
    ("SystemCacheType", "B"),
    ("Associativity", "B"),
    ("MaximumCacheSize2", "I"),
    ("InstalledSize2", "I"),
))

SMBIOS_TABLE_TYPE8 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("InternalReferenceDesignator", "O#SMBIOS_TABLE_STRING"),
    ("InternalConnectorType", "B"),
    ("ExternalReferenceDesignator", "O#SMBIOS_TABLE_STRING"),
    ("ExternalConnectorType", "B"),
    ("PortType", "B"),
))

SMBIOS_TABLE_TYPE9 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("SlotDesignation", "O#SMBIOS_TABLE_STRING"),
    ("SlotType", "B"),
    ("SlotDataBusWidth", "B"),
    ("CurrentUsage", "B"),
    ("SlotLength", "B"),
    ("SlotID", "H"),
    ("SlotCharacteristics1", "O#MISC_SLOT_CHARACTERISTICS1"),
    ("SlotCharacteristics2", "O#MISC_SLOT_CHARACTERISTICS2"),
    ("SegmentGroupNum", "H"),
    ("BusNum", "B"),
    ("DevFuncNum", "B"),
))

SMBIOS_TABLE_TYPE10 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Device", "1O#DEVICE_STRUCT"),
))

SMBIOS_TABLE_TYPE11 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("StringCount", "B"),
))

SMBIOS_TABLE_TYPE12 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("StringCount", "B"),
))

SMBIOS_TABLE_TYPE13 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("InstallableLanguages", "B"),
    ("Flags", "B"),
    ("Reserved", "15B"),
    ("CurrentLanguages", "O#SMBIOS_TABLE_STRING"),
))

SMBIOS_TABLE_TYPE14 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("GroupName", "O#SMBIOS_TABLE_STRING"),
    ("Group", "1O#GROUP_STRUCT"),
))

SMBIOS_TABLE_TYPE15 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("LogAreaLength", "H"),
    ("LogHeaderStartOffset", "H"),
    ("LogDataStartOffset", "H"),
    ("AccessMethod", "B"),
    ("LogStatus", "B"),
    ("LogChangeToken", "I"),
    ("AccessMethodAddress", "I"),
    ("LogHeaderFormat", "B"),
    ("NumberOfSupportedLogTypeDescriptors", "B"),
    ("LengthOfLogTypeDescriptor", "B"),
    ("EventLogTypeDescriptors", "1O#EVENT_LOG_TYPE"),
))

SMBIOS_TABLE_TYPE16 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Location", "B"),
    ("Use", "B"),
    ("MemoryErrorCorrection", "B"),
    ("MaximumCapacity", "I"),
    ("MemoryErrorInformationHandle", "H"),
    ("NumberOfMemoryDevices", "H"),
    ("ExtendedMaximumCapacity", "Q"),
))

SMBIOS_TABLE_TYPE17 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("MemoryArrayHandle", "H"),
    ("MemoryErrorInformationHandle", "H"),
    ("TotalWidth", "H"),
    ("DataWidth", "H"),
    ("Size", "H"),
    ("FormFactor", "B"),
    ("DeviceSet", "B"),
    ("DeviceLocator", "O#SMBIOS_TABLE_STRING"),
    ("BankLocator", "O#SMBIOS_TABLE_STRING"),
    ("MemoryType", "B"),
    ("TypeDetail", "O#MEMORY_DEVICE_TYPE_DETAIL"),
    ("Speed", "H"),
    ("Manufacturer", "O#SMBIOS_TABLE_STRING"),
    ("SerialNumber", "O#SMBIOS_TABLE_STRING"),
    ("AssetTag", "O#SMBIOS_TABLE_STRING"),
    ("PartNumber", "O#SMBIOS_TABLE_STRING"),
    ("Attributes", "B"),
    ("ExtendedSize", "I"),
    ("ConfiguredMemoryClockSpeed", "H"),
    ("MinimumVoltage", "H"),
    ("MaximumVoltage", "H"),
    ("ConfiguredVoltage", "H"),
))

SMBIOS_TABLE_TYPE18 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("ErrorType", "B"),
    ("ErrorGranularity", "B"),
    ("ErrorOperation", "B"),
    ("VendorSyndrome", "I"),
    ("MemoryArrayErrorAddress", "I"),
    ("DeviceErrorAddress", "I"),
    ("ErrorResolution", "I"),
))

SMBIOS_TABLE_TYPE19 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("StartingAddress", "I"),
    ("EndingAddress", "I"),
    ("MemoryArrayHandle", "H"),
    ("PartitionWidth", "B"),
    ("ExtendedStartingAddress", "Q"),
    ("ExtendedEndingAddress", "Q"),
))

SMBIOS_TABLE_TYPE20 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("StartingAddress", "I"),
    ("EndingAddress", "I"),
    ("MemoryDeviceHandle", "H"),
    ("MemoryArrayMappedAddressHandle", "H"),
    ("PartitionRowPosition", "B"),
    ("InterleavePosition", "B"),
    ("InterleavedDataDepth", "B"),
    ("ExtendedStartingAddress", "Q"),
    ("ExtendedEndingAddress", "Q"),
))

SMBIOS_TABLE_TYPE21 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Type", "B"),
    ("Interface", "B"),
    ("NumberOfButtons", "B"),
))

SMBIOS_TABLE_TYPE22 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Location", "O#SMBIOS_TABLE_STRING"),
    ("Manufacturer", "O#SMBIOS_TABLE_STRING"),
    ("ManufactureDate", "O#SMBIOS_TABLE_STRING"),
    ("SerialNumber", "O#SMBIOS_TABLE_STRING"),
    ("DeviceName", "O#SMBIOS_TABLE_STRING"),
    ("DeviceChemistry", "B"),
    ("DeviceCapacity", "H"),
    ("DesignVoltage", "H"),
    ("SBDSVersionNumber", "O#SMBIOS_TABLE_STRING"),
    ("MaximumErrorInBatteryData", "B"),
    ("SBDSSerialNumber", "H"),
    ("SBDSManufactureDate", "H"),
    ("SBDSDeviceChemistry", "O#SMBIOS_TABLE_STRING"),
    ("DesignCapacityMultiplier", "B"),
    ("OEMSpecific", "I"),
))

SMBIOS_TABLE_TYPE23 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Capabilities", "B"),
    ("ResetCount", "H"),
    ("ResetLimit", "H"),
    ("TimerInterval", "H"),
    ("Timeout", "H"),
))

SMBIOS_TABLE_TYPE24 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("HardwareSecuritySettings", "B"),
))

SMBIOS_TABLE_TYPE25 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("NextScheduledPowerOnMonth", "B"),
    ("NextScheduledPowerOnDayOfMonth", "B"),
    ("NextScheduledPowerOnHour", "B"),
    ("NextScheduledPowerOnMinute", "B"),
    ("NextScheduledPowerOnSecond", "B"),
))

SMBIOS_TABLE_TYPE26 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Description", "O#SMBIOS_TABLE_STRING"),
    ("LocationAndStatus", "O#MISC_VOLTAGE_PROBE_LOCATION"),
    ("MaximumValue", "H"),
    ("MinimumValue", "H"),
    ("Resolution", "H"),
    ("Tolerance", "H"),
    ("Accuracy", "H"),
    ("OEMDefined", "I"),
    ("NominalValue", "H"),
))

SMBIOS_TABLE_TYPE27 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("TemperatureProbeHandle", "H"),
    ("DeviceTypeAndStatus", "O#MISC_COOLING_DEVICE_TYPE"),
    ("CoolingUnitGroup", "B"),
    ("OEMDefined", "I"),
    ("NominalSpeed", "H"),
    ("Description", "O#SMBIOS_TABLE_STRING"),
))

SMBIOS_TABLE_TYPE28 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Description", "O#SMBIOS_TABLE_STRING"),
    ("LocationAndStatus", "O#MISC_TEMPERATURE_PROBE_LOCATION"),
    ("MaximumValue", "H"),
    ("MinimumValue", "H"),
    ("Resolution", "H"),
    ("Tolerance", "H"),
    ("Accuracy", "H"),
    ("OEMDefined", "I"),
    ("NominalValue", "H"),
))

SMBIOS_TABLE_TYPE29 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Description", "O#SMBIOS_TABLE_STRING"),
    ("LocationAndStatus", "O#MISC_ELECTRICAL_CURRENT_PROBE_LOCATION"),
    ("MaximumValue", "H"),
    ("MinimumValue", "H"),
    ("Resolution", "H"),
    ("Tolerance", "H"),
    ("Accuracy", "H"),
    ("OEMDefined", "I"),
    ("NominalValue", "H"),
))

SMBIOS_TABLE_TYPE30 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("ManufacturerName", "O#SMBIOS_TABLE_STRING"),
    ("Connections", "B"),
))

SMBIOS_TABLE_TYPE31 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Checksum", "B"),
    ("Reserved1", "B"),
    ("Reserved2", "H"),
    ("BisEntry16", "I"),
    ("BisEntry32", "I"),
    ("Reserved3", "Q"),
    ("Reserved4", "I"),
))

SMBIOS_TABLE_TYPE32 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Reserved", "6B"),
    ("BootStatus", "B"),
))

SMBIOS_TABLE_TYPE33 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("ErrorType", "B"),
    ("ErrorGranularity", "B"),
    ("ErrorOperation", "B"),
    ("VendorSyndrome", "I"),
    ("MemoryArrayErrorAddress", "Q"),
    ("DeviceErrorAddress", "Q"),
    ("ErrorResolution", "I"),
))

SMBIOS_TABLE_TYPE34 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Description", "O#SMBIOS_TABLE_STRING"),
    ("Type", "B"),
    ("Address", "I"),
    ("AddressType", "B"),
))

SMBIOS_TABLE_TYPE35 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("Description", "O#SMBIOS_TABLE_STRING"),
    ("ManagementDeviceHandle", "H"),
    ("ComponentHandle", "H"),
    ("ThresholdHandle", "H"),
))

SMBIOS_TABLE_TYPE36 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("LowerThresholdNonCritical", "H"),
    ("UpperThresholdNonCritical", "H"),
    ("LowerThresholdCritical", "H"),
    ("UpperThresholdCritical", "H"),
    ("LowerThresholdNonRecoverable", "H"),
    ("UpperThresholdNonRecoverable", "H"),
))

SMBIOS_TABLE_TYPE37 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("ChannelType", "B"),
    ("MaximumChannelLoad", "B"),
    ("MemoryDeviceCount", "B"),
    ("MemoryDevice", "1O#MEMORY_DEVICE"),
))

SMBIOS_TABLE_TYPE38 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("InterfaceType", "B"),
    ("IPMISpecificationRevision", "B"),
    ("I2CSlaveAddress", "B"),
    ("NVStorageDeviceAddress", "B"),
    ("BaseAddress", "Q"),
    ("BaseAddressModifier_InterruptInfo", "B"),
    ("InterruptNumber", "B"),
))

SMBIOS_TABLE_TYPE39 = OrderedDict((
    ("Hdr", "O#SMBIOS_STRUCTURE"),
    ("PowerUnitGroup", "B"),
    ("Location", "O#SMBIOS_TABLE_STRING"),
    ("DeviceName", "O#SMBIOS_TABLE_STRING"),
    ("Manufacturer", "O#SMBIOS_TABLE_STRING"),
    ("SerialNumber", "O#SMBIOS_TABLE_STRING"),
    ("AssetTagNumber", "O#SMBIOS_TABLE_STRING"),
    ("ModelPartNumber", "O#SMBIOS_TABLE_STRING"),
    ("RevisionLevel", "O#SMBIOS_TABLE_STRING"),
    ("MaxPowerCapacity", "H"),
    ("PowerSupplyCharacteristics", "O#SYS_POWER_SUPPLY_CHARACTERISTICS"),
    ("InputVoltageProbeHandle", "H"),
    ("CoolingDeviceHandle", "H"),
    ("InputCurrentProbeHandle", "H"),
))

SMBIOS_TABLE_TYPE40 = OrderedDict((
    ("Hdr",                                  "O#SMBIOS_STRUCTURE"),
    ("NumberOfAdditionalInformationEntries", "B"),
    ("AdditionalInfoEntries",                "1O#ADDITIONAL_INFORMATION_ENTRY"),
))

SMBIOS_TABLE_TYPE41 = OrderedDict((
    ("Hdr",                     "O#SMBIOS_STRUCTURE"),
    ("ReferenceDesignation",    "O#SMBIOS_TABLE_STRING"),
    ("DeviceType",              "B"),
    ("DeviceTypeInstance",      "B"),
    ("SegmentGroupNum",         "H"),
    ("BusNum",                  "B"),
    ("DevFuncNum",              "B"),
))

SMBIOS_TABLE_TYPE41 = OrderedDict((
    ("Hdr",                   "O#SMBIOS_STRUCTURE"),
    ("ReferenceDesignation",  "B"),
    ("DeviceType",            "B"),
    ("DeviceTypeInstance",    "B"),
    ("SegmentGroupNum",       "H"),
    ("BusNum",                "B"),
    ("DevFuncNum",            "B"),
))

SMBIOS_TABLE_TYPE42 = OrderedDict((
    ("Hdr",                   "O#SMBIOS_STRUCTURE"),
    ("InterfaceType",         "B"),
    ("MCHostInterfaceData",   "B"),
))

SMBIOS_TABLE_TYPE43 = OrderedDict((
    ("Hdr",                   "O#SMBIOS_STRUCTURE"),
    ("VendorID",              "4B"),
    ("MajorSpecVersion",      "B"),
    ("MinorSpecVersion",      "B"),
    ("FirmwareVersion1",      "I"),
    ("FirmwareVersion2",      "I"),
    ("Description",           "O#SMBIOS_TABLE_STRING"),
    ("Characteristics",       "Q"),
    ("OemDefined",            "I"),
))


def GetSmbiosProtocol():
    Infc = mem()    # empty object just used to hold the protocol pointer
    uefi.bs.LocateProtocol (gEfiSmbiosProtocolGuid, null, Infc.REF().REF())
    Infc.CAST("O#EFI_SMBIOS_PROTOCOL")  # typecast it so we can access its fields
    return Infc

    # Following code works too but it needs to allocate memory from heap.
    #
    #   Infcp = mem("PO#EFI_SMBIOS_PROTOCOL")
    #   uefi.bs.LocateProtocol (gEfiSmbiosProtocolGuid, null, Infcp.REF())
    #   Infc = Infcp.DREF()
    #   Infcp.FREE()    # remember to free
    #   return Infc
    #
    

__PROT__ = GetSmbiosProtocol()

class SmbiosEntry(object):
    ENTRIES = {}
    STRINGS = {}
    TYPES = {}

    def __new__(Class, Entry, EntryType, StringList):
        for Obj in Class.ENTRIES:
            if Class.ENTRIES[Obj].ADDR == Entry.ADDR:
                return Obj
        return super(Class, SmbiosEntry).__new__(Class)

    def __init__(self, Entry, EntryType, StringList):
        if self in SmbiosEntry.ENTRIES:
            return

        SmbiosEntry.ENTRIES[self] = Entry
        SmbiosEntry.STRINGS[self] = StringList
        SmbiosEntry.TYPES[self] = EntryType

    def __getattr__(self, Name):
        Entry = SmbiosEntry.ENTRIES[self]
        Strings = SmbiosEntry.STRINGS[self]

        Value = getattr(Entry, Name)
        Type = self._GetEntryType(Name)
        if Type == "SMBIOS_TABLE_STRING" and Value > 0 and Value <= len(Strings):
            return Strings[Value - 1]
        elif type(Type) == OrderedDict:
            return RecordEntry(Value, Type, Strings)
        return Value

    def __setattr__(self, Name, Value):
        Entry = SmbiosEntry.ENTRIES[self]
        Strings = SmbiosEntry.STRINGS[self]
        if type(Value) == str:
            Index = getattr(Entry, Name)
            Strings[Index - 1] = Value
        else:
            setattr(Entry, Name, Value)

    def _GetEntryType(self, EntryName):
        TypeDef = SmbiosEntry.TYPES[self]
        DefStr = TypeDef[EntryName]
        try:
            TypeStart = DefStr.index("O#")
            DefStr = DefStr[TypeStart + 2:]
            DefObj = eval(DefStr)
            if type(DefObj) == OrderedDict:
                return DefObj
        except:
            pass
        return DefStr

    def __iter__(self):
        Entry = SmbiosEntry.ENTRIES[self]
        return iter(Entry)

class SmbiosRecord(object):
    #TRICK: MicroPython doesn't support object.__setattr__() to add object
    #       attributes if __setattr__ is overridden. We have to use class
    #       attributes to avoid infinite loop.
    RECORDS = {}
    STRINGS = {}
    TYPES = {}

    def __init__(self, RawData):
        SmbiosRecord.RECORDS[self] = RawData
        self._GetTypeDefinition()
        self._ExtractStringList()

    def __str__(self):
        return "smbios.type%d[%x]" % (self.Hdr.Type, self.Hdr.Handle)

    def _GetEntryType(self, TypeDef, EntryName):
        DefStr = TypeDef[EntryName]
        try:
            TypeStart = DefStr.index("O#")
            DefStr = DefStr[TypeStart + 2:]
            DefObj = eval(DefStr)
            if type(DefObj) == OrderedDict:
                return DefObj
        except:
            pass
        return DefStr

    def _DumpEntries(self, Data, TypeDef, StringList, Indent=0):
        if not Data:
            return

        ConvertArray = False
        for Name in Data:
            if type(Name) not in [str]:
                if not ConvertArray:
                    ConvertArray = True
                    print("%s[%02x" % (' ' * Indent, Name), end='')
                else:
                    print(", %02x" % Name, end='')
                continue

            Field = getattr(Data, Name, None)
            if Field == None:
                continue

            if type(Field) == mem:
                print("%s.%s" % (' ' * Indent, Name))
                self._DumpEntries(Field, self._GetEntryType (TypeDef, Name), StringList, Indent + 2)
            elif type(Field) == guid:
                print("%s.%s = %s" % (' ' * Indent, Name, Field))
            elif type(Field) == str:
                print('%s.%s = "%s"' % (' ' * Indent, Name, Field))
            else:
                TypeStr = self._GetEntryType (TypeDef, Name)
                if TypeStr == "SMBIOS_TABLE_STRING" and Field <= len(StringList):
                    Field = StringList[Field - 1]
                    print('%s.%s = "%s"' % (' ' * Indent, Name, Field))
                else:
                    Field = hex(Field)
                    print("%s.%s = %s" % (' ' * Indent, Name, Field))
        else:
            if ConvertArray:
                print("]")

    def _GetTypeDefinition(self):
        Data = SmbiosRecord.RECORDS[self]
        TypeDef = eval("SMBIOS_TABLE_TYPE%s" % Data.Hdr.Type)
        SmbiosRecord.TYPES[self] = TypeDef

    def _ExtractStringList(self):
        Data = SmbiosRecord.RECORDS[self]
        Buf = mem(0, Data.ADDR + Data.Hdr.Length)
        Index = 0
        Start = Buf.ADDR
        Length = 0
        StringList = []

        while (Buf[Index] != 0 or Buf[Index + 1] != 0):
            Length += 1
            if Buf[Index] == 0:
                StrObj = mem("%da" % Length, Start)
                StringList.append(StrObj.VALUE)

                Start += Length
                Length = 0

            Index += 1

        if Length > 0:
            StrObj = mem("%da" % (Length + 1), Start)
            StringList.append(StrObj.VALUE)

        # Update size for the sake of strings
        Data.SIZE = Data.Hdr.Length + Index + 2
        SmbiosRecord.STRINGS[self] = StringList

    def __getattr__(self, Name):
        Data = SmbiosRecord.RECORDS[self]
        TypeDef = SmbiosRecord.TYPES[self]
        Strings = SmbiosRecord.STRINGS[self]
        assert (Data != None)

        Value = getattr(Data, Name)
        Type = self._GetEntryType(TypeDef, Name)
        if (Type == "SMBIOS_TABLE_STRING" and Value > 0 and Value <= len(Strings)):
            return Strings[Value - 1]
        elif type(Type) == OrderedDict:
            return SmbiosEntry(Value, Type, Strings)
        return Value

    def __setattr__(self, Name, Value):
        Data = SmbiosRecord.RECORDS[self]
        assert (Data != None)

        Strings = SmbiosRecord.STRINGS[self]
        if type(Value) == str:
            Index = getattr(Data, Name)
            Strings[Index - 1] = Value
        else:
            setattr(Data, Name, Value)

    def __iter__(self):
        Data = SmbiosRecord.RECORDS[self]
        return iter(Data)

    def Publish(self):
        Done = False

        Data = SmbiosRecord.RECORDS[self]
        Handle = mem("H")
        Handle.VALUE = Data.Hdr.Handle

        NewStringList = SmbiosRecord.STRINGS[self]
        # Get old string list by parsing raw data again
        self._ExtractStringList()
        OldStringList = SmbiosRecord.STRINGS[self]

        StringNumber = mem("N")
        for Index in range(len(NewStringList)):
            if NewStringList[Index] != OldStringList[Index]:
                StringNumber.VALUE = Index + 1
                SMBIOS._Protocol.UpdateString(SMBIOS._Protocol, Handle, StringNumber, NewStringList[Index])
                Done = True

        #
        # Updating string will also update other record data. No more update
        # needed if it just happened.
        #
        if not Done:
            #
            # Removal will free the memory of record data. We need to keep it in a
            # new memory block in advance.
            #
            NewData = mem("%dB" % Data.SIZE)
            NewData.VALUE = Data    # This will do copying.
            NewData.CAST("O#SMBIOS_TABLE_TYPE%d" % Data.Hdr.Type)

            SMBIOS._Protocol.Remove(SMBIOS._Protocol, Handle)
            SMBIOS._Protocol.Add(SMBIOS._Protocol, null, Handle, NewData)

        # Once the record is updated, original record data memory will be freed
        # and cannot be used any longer.
        SmbiosRecord.RECORDS[self] = None
        Handle.FREE()
        StringNumber.FREE()

    def Dump(self):
        Data = SmbiosRecord.RECORDS[self]
        TypeDef = SmbiosRecord.TYPES[self]
        StringList = SmbiosRecord.STRINGS[self]
        self._DumpEntries (Data, TypeDef, StringList)

class SmbiosHelperClass(object):
    def __init__(self):
        self._Protocol = __PROT__

    def __str__(self):
        return "smbios%d.%d" % (self._Protocol.MajorVersion, self._Protocol.MinorVersion)

    def __getattr__(self, Name):
        if not Name:
            return None

        if Name in ["MajorVersion", "MinorVersion"]:
            return getattr(self._Protocol, Name)

        if Name not in SMBIOS_TYPES:
            return None

        Type = "PO#SMBIOS_TABLE_TYPE%d" % SMBIOS_TYPES[Name]
        SmbiosHandle = mem(SMBIOS_HANDLE)
        SmbiosHandle.VALUE = 0xFFFE
        RecordType = mem('B')
        RecordType.VALUE = SMBIOS_TYPES[Name]
        RecordPtr = mem("P")
        Record = None
        RecordList = []

        while True:
            try:
                self._Protocol.GetNext (self._Protocol, SmbiosHandle.REF(), RecordType.REF(), RecordPtr.REF(), null)
            except:
                break
            Record = RecordPtr.DREF(Type)
            if Record.Hdr.Type == SMBIOS_TYPES[Name]:
                RecordList.append(SmbiosRecord(Record))

        SmbiosHandle.FREE()
        RecordType.FREE()

        return RecordList

SMBIOS = SmbiosHelperClass()

if __name__ == '__main__':
    import sys

    s=SMBIOS
    print(s)
    if len(sys.argv) == 0:
        tlist = range(44)
    else:
        tlist = [int(sys.argv[0], 0)]

    for t in tlist:
        print("\n======== Type%d ========" % t)
        for r in getattr(s, "Type%d" % t, []):
            r.Dump()
            print()

