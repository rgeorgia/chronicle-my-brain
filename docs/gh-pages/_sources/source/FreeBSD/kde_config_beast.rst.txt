

$ doas sysrc sddm_enable=yes 
sddm_enable:  -> yes
$ pciconf -lv|grep -B4 VGA  
vgapci0@pci0:1:0:0:	class=0x030000 rev=0xa1 hdr=0x00 vendor=0x10de device=0x2504 subvendor=0x1458 subdevice=0x4074
    vendor     = 'NVIDIA Corporation'
    device     = 'GA106 [GeForce RTX 3060 Lite Hash Rate]'
    class      = display
    subclass   = VGA

sysctl machdep.bootmethod                                      Sat May 17 18:15:08 2025
machdep.bootmethod: UEFI
 

pciconf -lv | grep -B3 display
vgapci0@pci0:1:0:0:	class=0x030000 rev=0xa1 hdr=0x00 vendor=0x10de device=0x2504 subvendor=0x1458 subdevice=0x4074
    vendor     = 'NVIDIA Corporation'
    device     = 'GA106 [GeForce RTX 3060 Lite Hash Rate]'
    class      = display


