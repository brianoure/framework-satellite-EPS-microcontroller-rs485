# satellite-EPS-microcontroller-rs485
A model Electrical Power Subsystem (EPS) microcontroller program for communicating with an (On Board Computer)OBC using the rs485 protocol in Python3 and C.<br />

The rs485 - 4 wire - channel requires five lines - 2 signal pairs (i.e TXPOS,TXNEG,RXPOS,RXNEG) and 1 ground (GND) are implemented to
enable transmission and reception of packets between the OBC and the EPS respective microcontrollers.

Considering that other slaves/subsystems in the same communication bus might be sending data to the master, it is imperative that any slave <br />
not transmitting any data have the transmission pins set to HIGH IMPEDANCE.

As for telemetry data, the EPS outputs a - 56 bit telemetry frame - to the OBC sectioned as follows; (MSB to LSB/ Left to Right/First to Last)
| Packet Section                                 | Bit width     | Valid Decimal Values    (Meaning or representation)|
| -------------                                  | ------------- | --------------                                     |
| Header (Most significant)                      | 8             | 195(valid frame identifier starting constant)      |
| Payload subsystem state                        | 2             | 1(Payload is ON) or 0(Payload is OFF)              |
| Communication subsystem component (UHF) state  | 1             | 1(UHF is ON)    or 0(UHF is OFF)                   |
| Communication subsystem component (Xband) state| 2             | 1(Xband is ON) or 0(Xband is OFF)                  |
| Solar Panel Array1 output voltage              | 5             | 0 to 32 (integer value for voltage range)          |
| Solar Panel Array2 output voltage              | 5             | 0 to 32 (integer value for voltage range)          |
| Solar Panel Array3 output voltage              | 5             | 0 to 32 (integer value for voltage range)          |
| Solar Panel Array4 output voltage              | 5             | 0 to 32 (integer value for voltage range)          |
| 8 cell Battery voltage (4S2P arrangement)      | 5             | 0 to 32 (integer value for voltage range - for a maximum output of 4V per cell, the highest yield should be 16V) |
| Battery temperature                            | 9             | -255 to 256(valid frame ending identifier constant)|
| Battery heater state                           | 1             | 1(heater is ON) or 0(heater is OFF)                |
| Tail (Least significant)                       | 8             | 135(valid frame ending identifier constant)        |

Whereas the EPS receives a - 56 bit command frame - from the OBC that consists of the following information; (MSB to LSB/ Left to Right/First to Last)
| Packet Section                                 | Bit width     | Valid Decimal Values   (Meaning or representation)|
| -------------                                  | ------------- | --------------                                    |
| Header (Most significant)                      | 16            | 34539(valid frame identifier starting constant)   |
| Payload subsystem commmand                     | 8             | 197(turn payload ON) or 245(turn payload OFF)     |
| Communication subsystem component (UHF) state  | 8             | 117(turn UHF ON)    or 199(turn UHF OFF)          |
| Communication subsystem component (Xband) state| 8             | 149(turn Xband ON) or 87(turn Xband OFF)          |
| Battery heater command                         | 8             | 139(turn heater ON) or 213(turn heater OFF)       |
| Tail (Least significant)                       | 8             | 135(valid frame ending identifier constant)       |

The image below illustrates the connections
<br />
![How the EPS and OBC microcontrollers connect](https://raw.githubusercontent.com/brianoure/satellite-EPS-microcontroller-rs485/main/rs485_4_wire_full_duplex.png)
