```sh
$ config-pin P8.03 gpio
ERROR: open() for /sys/devices/platform/ocp/ocp:P8_03_pinmux/state failed, No such file or directory

$ ls /sys/devices/platform/ocp/
40300000.ocmcram  48060000.mmc       49800000.tptc           ocp:P8_12_pinmux  ocp:P9_21_pinmux
44e07000.gpio     480c8000.mailbox   49900000.tptc           ocp:P8_13_pinmux  ocp:P9_22_pinmux
44e09000.serial   480ca000.spinlock  49a00000.tptc           ocp:P8_14_pinmux  ocp:P9_23_pinmux
44e0b000.i2c      4819c000.i2c       4a100000.ethernet       ocp:P8_15_pinmux  ocp:P9_24_pinmux
44e0d000.tscadc   481a0000.spi       4a326004.pruss-soc-bus  ocp:P8_16_pinmux  ocp:P9_26_pinmux
44e35000.wdt      481a6000.serial    4c000000.emif           ocp:P8_17_pinmux  ocp:P9_27_pinmux
44e3e000.rtc      481a8000.serial    53100000.sham           ocp:P8_18_pinmux  ocp:P9_30_pinmux
47400000.usb      481aa000.serial    53500000.aes            ocp:P8_19_pinmux  ocp:P9_41_pinmux
48022000.serial   481ac000.gpio      56000000.sgx            ocp:P8_26_pinmux  ocp:P9_42_pinmux
48024000.serial   481ae000.gpio      driver_override         ocp:P9_11_pinmux  ocp:P9_91_pinmux
4802a000.i2c      481cc000.can       modalias                ocp:P9_12_pinmux  ocp:P9_92_pinmux
48030000.spi      481d0000.can       ocp:A15_pinmux          ocp:P9_13_pinmux  of_node
48038000.mcasp    481d8000.mmc       ocp:cape-universal      ocp:P9_14_pinmux  power
48042000.timer    48300000.epwmss    ocp:l4_wkup@44c00000    ocp:P9_15_pinmux  subsystem
48044000.timer    48302000.epwmss    ocp:P8_07_pinmux        ocp:P9_16_pinmux  uevent
48046000.timer    48304000.epwmss    ocp:P8_08_pinmux        ocp:P9_17_pinmux
48048000.timer    4830e000.lcdc      ocp:P8_09_pinmux        ocp:P9_18_pinmux
4804a000.timer    48310000.rng       ocp:P8_10_pinmux        ocp:P9_19_pinmux
4804c000.gpio     49000000.edma      ocp:P8_11_pinmux        ocp:P9_20_pinmux

```
