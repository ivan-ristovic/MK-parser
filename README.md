# MK-parser
Parse and pretty-print exam schedules in chronological order. Parsed schedules can be found in [schedules](schedules) directory.

**NOTE: Due to inconsistencies in scheduling table (extra dates for some exams), there are situations where the parser cannot possibly know which extra date corresponds to which exam, in which case the whole schedule for that year may be wrong. Use with caution.**

## Setup:
Python 3 is required.

```
$ pip install -r requirements.txt
```

## Usage:
```
usage: mkparser.py [-h] [-y YEAR] [--urls [URLS [URLS ...]]] [-j]

Convert MK PDF to a human readable format.

optional arguments:
  -h, --help            show this help message and exit
  -y YEAR, --year YEAR  Change year in URL because sometimes it is wrong
  --urls [URLS [URLS ...]]
                        PDF URLs in case you wish to add them manually for
                        some reason
  -j, --json            Generate JSON output
```

If URL list is not provided, program will automatically try to download files based on current year, unless it is overridden via `-y` option.

## Sample output:
```
======== RASPORED_ISPITA_JUN_1920.pdf ========
-----------------------------------------------------
YEAR: 1:
-----------------------------------------------------
P1 (N)                         |     2020-06-08 09:00
A1 (N)                         |     2020-06-09 13:00
TNP (N)                        |     2020-06-09 17:00
DS2 (N)                        |     2020-06-11 13:00
OA1                            |     2020-06-12 13:00
LAAG (N)                       |     2020-06-13 09:00
UOAR2                          |     2020-06-15 09:00
P2                             |     2020-06-17 09:00
OA2                            |     2020-06-18 13:00
DS1 (N)                        |     2020-06-19 13:00
UOAR1 (N)                      |     2020-06-22 17:00
E (N)                          |     2020-06-24 17:00
Z (N)                          |     2020-06-26 17:00
-----------------------------------------------------
YEAR: 2:
-----------------------------------------------------
OM                             |     2020-06-08 09:00
G (N)                          |     2020-06-09 09:00
KIAA (ТРГ + ЈАГ)               |     2020-06-12 17:00
OA                             |     2020-06-13 13:00
OOP (JAG)                      |     2020-06-16 09:00
UVIT                           |     2020-06-18 09:00
A3 (N)                         |     2020-06-20 13:00
ALG1 (N)                       |     2020-06-22 09:00
A2                             |     2020-06-23 13:00
OS                             |     2020-06-24 09:00
AISP                           |     2020-06-26 09:00
-----------------------------------------------------
YEAR: 3:
-----------------------------------------------------
PPJ                            |     2020-06-08 09:00
PROGBP                         |     2020-06-09 09:00
VI                             |     2020-06-10 13:00
RBP (N)                        |     2020-06-11 17:00
UNM                            |     2020-06-14 09:00
IP1                            |     2020-06-16 17:00
PP                             |     2020-06-19 09:00
V                              |     2020-06-20 17:00
RG (N)                         |     2020-06-22 13:00
KK                             |     2020-06-23 09:00
S                              |     2020-06-25 13:00
VIS                            |     2020-06-25 13:00
-----------------------------------------------------
YEAR: 4:
-----------------------------------------------------
A4 (N)                         |     2020-06-09 13:00
OMM                            |     2020-06-10 09:00
OI                             |     2020-06-11 17:00
PROJBP                         |     2020-06-12 09:00
PPGR (JAG)                     |     2020-06-13 17:00
SK-Ubisoft                     |     2020-06-15 17:00
TI                             |     2020-06-15 17:00
SK-ENDAVA (JAG)                |     2020-06-16 17:00
FP (N)                         |     2020-06-17 13:00
RS                             |     2020-06-19 17:00
URT (N)                        |     2020-06-20 17:00
ALG2 (N)                       |     2020-06-22 09:00
SK-FIS (JAG)                   |     2020-06-22 17:00
UKA                            |     2020-06-23 17:00
UTU                            |     2020-06-24 17:00
PVEB                           |     2020-06-25 17:00
-----------------------------------------------------
YEAR: 5:
-----------------------------------------------------
ODJ                            |     2020-06-09 17:00
OPDT                           |     2020-06-09 17:00
SMOI                           |     2020-06-09 17:00
MMA                            |     2020-06-10 09:00
MNG                            |     2020-06-10 09:00
VS (JAG)                       |     2020-06-10 09:00
KIAA2                          |     2020-06-11 09:00
FP                             |     2020-06-11 13:00
OI                             |     2020-06-11 17:00
UPIN                           |     2020-06-12 13:00
MMM                            |     2020-06-16 13:00
BIO (N)                        |     2020-06-16 17:00
RS2 (JAG)                      |     2020-06-17 17:00
OPG B                          |     2020-06-20 09:00
ZO                             |     2020-06-20 09:00
ML (JAG)                       |     2020-06-20 17:00
OPA                            |     2020-06-22 13:00
OPA                            |     2020-06-22 13:00
OPMS                           |     2020-06-22 13:00
OPSP                           |     2020-06-22 17:00
KRIP                           |     2020-06-23 17:00
MNR C                          |     2020-06-23 17:00
OPKA                           |     2020-06-23 17:00
OPML                           |     2020-06-23 17:00
AR (JAG)                       |     2020-06-24 17:00
MIN математике                 |     2020-06-24 17:00
GV                             |     2020-06-25 09:00
NI (JAG)                       |     2020-06-25 09:00
PNM                            |     2020-06-25 09:00
=======================
```
