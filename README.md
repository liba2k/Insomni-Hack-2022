# Insomni-Hack-2022
## Exploit for CVE-2021-0157 & CVE-2021-0158.
* Slides from our Insomi'Hack2022 talk `Insomnihack_Presentation.pdf`
* Detailed discription of the exploitation ROP chain [ROP.md](ROP.md)
* Python code for exploitation, based on [Chipsec](https://github.com/chipsec/chipsec) `latitude_chipsec_secureboot.py`.
## Exploitation tools and techniques
* Micropython environment for EFI shell.
    * Example script for MicroPython peachpy under EFI shell `peachpy_test.py`.
    * Example script for MicroPython UEFI protocol usage `capabilities.py`
* Patched version of EFI shell without 5 seconds delay `bootx64.efi`

## Executing brick on the EFI module 
[![Watch the video](https://img.youtube.com/vi/UKoEYGsuQXE/hqdefault.jpg)](https://youtu.be/UKoEYGsuQXE)


## Secure Boot bypass demo
[![Watch the video](https://img.youtube.com/vi/hHLKvjTZacE/hqdefault.jpg)](https://youtu.be/hHLKvjTZacE)

## Talk video
[![Watch the video](https://img.youtube.com/vi/ge_TnLfTv8I/hqdefault.jpg)](https://youtu.be/ge_TnLfTv8I)

## Related projects
https://github.com/Sentinel-One/brick
