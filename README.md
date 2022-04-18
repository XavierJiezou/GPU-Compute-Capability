# GPU-Compute-Capability

An application for querying the computing power of each gpu released by NVIDIA.

## Install

```bash
pip install -r requirements.txt
```

## Usage

```bash
git clone https://github.com/XavierJiezou/GPU-Compute-Capability.git
```

## Deploy

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/yourGitHubName/yourRepo/yourApp/)

## Table

```plainText
CUDA-Enabled Datacenter Products
Tesla Workstation Products
┌───────────────────┬────────────────────┐
│ GPU               │ Compute Capability │
├───────────────────┼────────────────────┤
│ Tesla K80         │ 3.7                │
│ Tesla K40         │ 3.5                │
│ Tesla K20         │ 3.5                │
│ Tesla C2075       │ 2.0                │
│ Tesla C2050/C2070 │ 2.0                │
└───────────────────┴────────────────────┘
CUDA-Enabled Datacenter Products    
NVIDIA Data Center Products
┌─────────────┬────────────────────┐
│ GPU         │ Compute Capability │
├─────────────┼────────────────────┤
│ NVIDIA A100 │ 8.0                │
│ NVIDIA A40  │ 8.6                │
│ NVIDIA A30  │ 8.0                │
│ NVIDIA A10  │ 8.6                │
│ NVIDIA A16  │ 8.6                │
│ NVIDIA A2   │ 8.6                │
│ NVIDIA T4   │ 7.5                │
│ NVIDIA V100 │ 7.0                │
│ Tesla P100  │ 6.0                │
│ Tesla P40   │ 6.1                │
│ Tesla P4    │ 6.1                │
│ Tesla M60   │ 5.2                │
│ Tesla M40   │ 5.2                │
│ Tesla K80   │ 3.7                │
│ Tesla K40   │ 3.5                │
│ Tesla K20   │ 3.5                │
│ Tesla K10   │ 3.0                │
└─────────────┴────────────────────┘
CUDA-Enabled NVIDIA Quadro and NVIDIA RTX 
NVIDIA Quadro and NVIDIA RTX Desktop GPUs
┌───────────────────┬────────────────────┐
│ GPU               │ Compute Capability │
├───────────────────┼────────────────────┤
│ RTX A6000         │ 8.6                │
│ RTX A5000         │ 8.6                │
│ RTX A4000         │ 8.6                │
│ T1000             │ 7.5                │
│ T600              │ 7.5                │
│ T400              │ 7.5                │
│ Quadro RTX 8000   │ 7.5                │
│ Quadro RTX 6000   │ 7.5                │
│ Quadro RTX 5000   │ 7.5                │
│ Quadro RTX 4000   │ 7.5                │
│ Quadro GV100      │ 7.0                │
│ Quadro GP100      │ 6.0                │
│ Quadro P6000      │ 6.1                │
│ Quadro P5000      │ 6.1                │
│ Quadro P4000      │ 6.1                │
│ Quadro P2200      │ 6.1                │
│ Quadro P2000      │ 6.1                │
│ Quadro P1000      │ 6.1                │
│ Quadro P620       │ 6.1                │
│ Quadro P600       │ 6.1                │
│ Quadro P400       │ 6.1                │
│ Quadro M6000 24GB │ 5.2                │
│ Quadro M6000      │ 5.2                │
│ Quadro K6000      │ 3.5                │
│ Quadro M5000      │ 5.2                │
│ Quadro K5200      │ 3.5                │
│ Quadro K5000      │ 3.0                │
│ Quadro M4000      │ 5.2                │
│ Quadro K4200      │ 3.0                │
│ Quadro K4000      │ 3.0                │
│ Quadro M2000      │ 5.2                │
│ Quadro K2200      │ 5.0                │
│ Quadro K2000      │ 3.0                │
│ Quadro K2000D     │ 3.0                │
│ Quadro K1200      │ 5.0                │
│ Quadro K620       │ 5.0                │
│ Quadro K600       │ 3.0                │
│ Quadro K420       │ 3.0                │
│ Quadro 410        │ 3.0                │
│ Quadro Plex 7000  │ 2.0                │
└───────────────────┴────────────────────┘
CUDA-Enabled NVIDIA Quadro and NVIDIA 
RTX
NVIDIA Quadro and NVIDIA RTX Mobile
GPUs
┌───────────────┬────────────────────┐
│ GPU           │ Compute Capability │
├───────────────┼────────────────────┤
│ RTX A5000     │ 8.6                │
│ RTX A4000     │ 8.6                │
│ RTX A3000     │ 8.6                │
│ RTX A2000     │ 8.6                │
│ RTX 5000      │ 7.5                │
│ RTX 4000      │ 7.5                │
│ RTX 3000      │ 7.5                │
│ T2000         │ 7.5                │
│ T1200         │ 7.5                │
│ T1000         │ 7.5                │
│ T600          │ 7.5                │
│ T500          │ 7.5                │
│ P620          │ 6.1                │
│ P520          │ 6.1                │
│ Quadro P5200  │ 6.1                │
│ Quadro P4200  │ 6.1                │
│ Quadro P3200  │ 6.1                │
│ Quadro P5000  │ 6.1                │
│ Quadro P4000  │ 6.1                │
│ Quadro P3000  │ 6.1                │
│ Quadro P2000  │ 6.1                │
│ Quadro P1000  │ 6.1                │
│ Quadro P600   │ 6.1                │
│ Quadro P500   │ 6.1                │
│ Quadro M5500M │ 5.2                │
│ Quadro M2200  │ 5.2                │
│ Quadro M1200  │ 5.0                │
│ Quadro M620   │ 5.2                │
│ Quadro M520   │ 5.0                │
│ Quadro K6000M │ 3.0                │
│ Quadro K5200M │ 3.0                │
│ Quadro K5100M │ 3.0                │
│ Quadro M5000M │ 5.0                │
│ Quadro K500M  │ 3.0                │
│ Quadro K4200M │ 3.0                │
│ Quadro K4100M │ 3.0                │
│ Quadro M4000M │ 5.0                │
│ Quadro K3100M │ 3.0                │
│ Quadro M3000M │ 5.0                │
│ Quadro K2200M │ 3.0                │
│ Quadro K2100M │ 3.0                │
│ Quadro M2000M │ 5.0                │
│ Quadro K1100M │ 3.0                │
│ Quadro M1000M │ 5.0                │
│ Quadro K620M  │ 5.0                │
│ Quadro K610M  │ 3.5                │
│ Quadro M600M  │ 5.0                │
│ Quadro K510M  │ 3.5                │
│ Quadro M500M  │ 5.0                │
└───────────────┴────────────────────┘
CUDA-Enabled NVS Products
Desktop Products
┌────────────────┬────────────────────┐
│ GPU            │ Compute Capability │
├────────────────┼────────────────────┤
│ NVIDIA NVS 810 │ 5.0                │
│ NVIDIA NVS 510 │ 3.0                │
│ NVIDIA NVS 315 │ 2.1                │
│ NVIDIA NVS 310 │ 2.1                │
└────────────────┴────────────────────┘
CUDA-Enabled NVS Products
Mobile Products
┌───────────┬────────────────────┐
│ GPU       │ Compute Capability │
├───────────┼────────────────────┤
│ NVS 5400M │ 2.1                │
│ NVS 5200M │ 2.1                │
│ NVS 4200M │ 2.1                │
└───────────┴────────────────────┘
CUDA-Enabled GeForce and TITAN Products
GeForce and TITAN Products
┌──────────────────────────┬────────────────────┐
│ GPU                      │ Compute Capability │
├──────────────────────────┼────────────────────┤
│ Geforce RTX 3060 Ti      │ 8.6                │
│ Geforce RTX 3060         │ 8.6                │
│ GeForce RTX 3090         │ 8.6                │
│ GeForce RTX 3080         │ 8.6                │
│ GeForce RTX 3070         │ 8.6                │
│ GeForce GTX 1650 Ti      │ 7.5                │
│ NVIDIA TITAN RTX         │ 7.5                │
│ Geforce RTX 2080 Ti      │ 7.5                │
│ Geforce RTX 2080         │ 7.5                │
│ Geforce RTX 2070         │ 7.5                │
│ Geforce RTX 2060         │ 7.5                │
│ NVIDIA TITAN V           │ 7.0                │
│ NVIDIA TITAN Xp          │ 6.1                │
│ NVIDIA TITAN X           │ 6.1                │
│ GeForce GTX 1080 Ti      │ 6.1                │
│ GeForce GTX 1080         │ 6.1                │
│ GeForce GTX 1070 Ti      │ 6.1                │
│ GeForce GTX 1070         │ 6.1                │
│ GeForce GTX 1060         │ 6.1                │
│ GeForce GTX 1050         │ 6.1                │
│ GeForce GTX TITAN X      │ 5.2                │
│ GeForce GTX TITAN Z      │ 3.5                │
│ GeForce GTX TITAN Black  │ 3.5                │
│ GeForce GTX TITAN        │ 3.5                │
│ GeForce GTX 980 Ti       │ 5.2                │
│ GeForce GTX 980          │ 5.2                │
│ GeForce GTX 970          │ 5.2                │
│ GeForce GTX 960          │ 5.2                │
│ GeForce GTX 950          │ 5.2                │
│ GeForce GTX 780 Ti       │ 3.5                │
│ GeForce GTX 780          │ 3.5                │
│ GeForce GTX 770          │ 3.0                │
│ GeForce GTX 760          │ 3.0                │
│ GeForce GTX 750 Ti       │ 5.0                │
│ GeForce GTX 750          │ 5.0                │
│ GeForce GTX 690          │ 3.0                │
│ GeForce GTX 680          │ 3.0                │
│ GeForce GTX 670          │ 3.0                │
│ GeForce GTX 660 Ti       │ 3.0                │
│ GeForce GTX 660          │ 3.0                │
│ GeForce GTX 650 Ti BOOST │ 3.0                │
│ GeForce GTX 650 Ti       │ 3.0                │
│ GeForce GTX 650          │ 3.0                │
│ GeForce GTX 560 Ti       │ 2.1                │
│ GeForce GTX 550 Ti       │ 2.1                │
│ GeForce GTX 460          │ 2.1                │
│ GeForce GTS 450          │ 2.1                │
│ GeForce GTS 450          │ 2.1                │
│ GeForce GTX 590          │ 2.0                │
│ GeForce GTX 580          │ 2.0                │
│ GeForce GTX 570          │ 2.0                │
│ GeForce GTX 480          │ 2.0                │
│ GeForce GTX 470          │ 2.0                │
│ GeForce GTX 465          │ 2.0                │
│ GeForce GT 740           │ 3.0                │
│ GeForce GT 730           │ 3.5                │
│ GeForce GT 730           │ 2.1                │
│ GeForce GT 720           │ 3.5                │
│ GeForce GT 705           │ 3.5                │
│ GeForce GT 640 (GDDR5)   │ 3.5                │
│ GeForce GT 640           │ 2.1                │
│ GeForce GT 630           │ 2.1                │
│ GeForce GT 620           │ 2.1                │
│ GeForce GT 610           │ 2.1                │
│ GeForce GT 520           │ 2.1                │
│ GeForce GT 440           │ 2.1                │
│ GeForce GT 440           │ 2.1                │
│ GeForce GT 430           │ 2.1                │
│ GeForce GT 430           │ 2.1                │
└──────────────────────────┴────────────────────┘
CUDA-Enabled GeForce and TITAN Products     
GeForce Notebook Products
┌─────────────────────┬────────────────────┐
│ GPU                 │ Compute Capability │
├─────────────────────┼────────────────────┤
│ GeForce RTX 3080    │ 8.6                │
│ GeForce RTX 3070    │ 8.6                │
│ GeForce RTX 3060    │ 8.6                │
│ GeForce RTX 3050 Ti │ 8.6                │
│ GeForce RTX 3050    │ 8.6                │
│ Geforce RTX 2080    │ 7.5                │
│ Geforce RTX 2070    │ 7.5                │
│ Geforce RTX 2060    │ 7.5                │
│ GeForce GTX 1080    │ 6.1                │
│ GeForce GTX 1070    │ 6.1                │
│ GeForce GTX 1060    │ 6.1                │
│ GeForce GTX 980     │ 5.2                │
│ GeForce GTX 980M    │ 5.2                │
│ GeForce GTX 970M    │ 5.2                │
│ GeForce GTX 965M    │ 5.2                │
│ GeForce GTX 960M    │ 5.0                │
│ GeForce GTX 950M    │ 5.0                │
│ GeForce 940M        │ 5.0                │
│ GeForce 930M        │ 5.0                │
│ GeForce 920M        │ 3.5                │
│ GeForce 910M        │ 5.2                │
│ GeForce GTX 880M    │ 3.0                │
│ GeForce GTX 870M    │ 3.0                │
│ GeForce GTX 860M    │ 3.0/5.0(**)        │
│ GeForce GTX 850M    │ 5.0                │
│ GeForce 840M        │ 5.0                │
│ GeForce 830M        │ 5.0                │
│ GeForce 820M        │ 2.1                │
│ GeForce 800M        │ 2.1                │
│ GeForce GTX 780M    │ 3.0                │
│ GeForce GTX 770M    │ 3.0                │
│ GeForce GTX 765M    │ 3.0                │
│ GeForce GTX 760M    │ 3.0                │
│ GeForce GTX 680MX   │ 3.0                │
│ GeForce GTX 680M    │ 3.0                │
│ GeForce GTX 675MX   │ 3.0                │
│ GeForce GTX 675M    │ 2.1                │
│ GeForce GTX 670MX   │ 3.0                │
│ GeForce GTX 670M    │ 2.1                │
│ GeForce GTX 660M    │ 3.0                │
│ GeForce GT 755M     │ 3.0                │
│ GeForce GT 750M     │ 3.0                │
│ GeForce GT 650M     │ 3.0                │
│ GeForce GT 745M     │ 3.0                │
│ GeForce GT 645M     │ 3.0                │
│ GeForce GT 740M     │ 3.0                │
│ GeForce GT 730M     │ 3.0                │
│ GeForce GT 640M     │ 3.0                │
│ GeForce GT 640M LE  │ 3.0                │
│ GeForce GT 735M     │ 3.0                │
│ GeForce GT 635M     │ 2.1                │
│ GeForce GT 730M     │ 3.0                │
│ GeForce GT 630M     │ 2.1                │
│ GeForce GT 625M     │ 2.1                │
│ GeForce GT 720M     │ 2.1                │
│ GeForce GT 620M     │ 2.1                │
│ GeForce 710M        │ 2.1                │
│ GeForce 705M        │ 2.1                │
│ GeForce 610M        │ 2.1                │
│ GeForce GTX 580M    │ 2.1                │
│ GeForce GTX 570M    │ 2.1                │
│ GeForce GTX 560M    │ 2.1                │
│ GeForce GT 555M     │ 2.1                │
│ GeForce GT 550M     │ 2.1                │
│ GeForce GT 540M     │ 2.1                │
│ GeForce GT 525M     │ 2.1                │
│ GeForce GT 520MX    │ 2.1                │
│ GeForce GT 520M     │ 2.1                │
│ GeForce GTX 485M    │ 2.1                │
│ GeForce GTX 470M    │ 2.1                │
│ GeForce GTX 460M    │ 2.1                │
│ GeForce GT 445M     │ 2.1                │
│ GeForce GT 435M     │ 2.1                │
│ GeForce GT 420M     │ 2.1                │
│ GeForce GT 415M     │ 2.1                │
│ GeForce GTX 480M    │ 2.0                │
│ GeForce 710M        │ 2.1                │
│ GeForce 410M        │ 2.1                │
└─────────────────────┴────────────────────┘
CUDA-Enabled Jetson Products
Jetson Products
┌───────────────────┬────────────────────┐
│ GPU               │ Compute Capability │
├───────────────────┼────────────────────┤
│ Jetson AGX Xavier │ 7.2                │
│ Jetson Nano       │ 5.3                │
│ Jetson TX2        │ 6.2                │
│ Jetson TX1        │ 5.3                │
│ Tegra X1          │ 5.3                │
└───────────────────┴────────────────────┘
```

## References

> - [Requests: HTTP for Humans™](https://docs.python-requests.org/en/latest/)
> - [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
> - [Welcome to Rich’s documentation!](https://rich.readthedocs.io/en/latest/)
> - [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
