"""
OBC master, EPS slave
RS485 protocol : TXPOS, TXNEG, RXPOS, RXNEG, GND
"""

PAYLOAD_POWER = 0 #initialisation
UHF_POWER     = 0 #initialisation
XBAND_POWER   = 0 #initialisation
HEATER_POWER  = 0 #initialisation

"""Initalising variables"""
position56          = 0
WORD_FROM_OBC_56BIT = 0
WORD_TO_OBC_56BIT   = 0

"""STM32 INPUT FROM OBC, the instructions we're receiving from the OBC and the specified frame constants"""
COMMAND_STARTING_IN_16BIT = 34539 #constant identifying the command frame header/start
COMMAND_PAYLOAD_ON_8BIT   = 197   #constant indicating that the OBC wants the EPS to turn ON payload
COMMAND_PAYLOAD_OFF_8BIT  = 245   #constant indicating that the OBC wants the EPS to turn OFF payload
COMMAND_UHF_ON_8BIT       = 117   #constant indicating that the OBC wants the EPS to turn ON uhf
COMMAND_UHF_OFF_8BIT      = 199   #constant indicating that the OBC wants the EPS to turn OFF uhf
COMMAND_XBAND_ON_8BIT     = 149   #constant indicating that the OBC wants the EPS to turn ON xband
COMMAND_XBAND_OFF_8BIT    = 87    #constant indicating that the OBC wants the EPS to turn OFF xband
COMMAND_HEATER_ON_8BIT    = 139   #constant indicating that the OBC wants the EPS to turn ON the heater
COMMAND_HEATER_OFF_8BIT   = 213   #constant indicating that the OBC wants the EPS to turn OFF the heater
COMMAND_ENDING_IN_8BIT    = 135   #constant identifying the command frame tail/end

"""STM32 OUTPUT TO OBC, the telemetry we're sending to the OBC and the specified frame constants"""
TELEMETRY_STARTING_OUT_16BIT  = 34539 #constantidentifying the telemetry frame header/start
TELEMETRY_ENDING_OUT_8BIT     = 135   #constant  identifying the telemetry frame tail/end

#TELEMETRY CAPTURE
def telemetry_payload_STATE():
    #read from pin powering the payload mosfet OR PAYLOAD_POWER variable 
    return PAYLOAD_POWER 
def telemetry_uhf_STATE():
    #read from pin powering the uhf mosfet OR UHF_POWER variable
    return UHF_POWER
def telemetry_xband_STATE():
    #read from pin powering the xband mosfet OR XBAND_POWER variable
    return XBAND_POWER
def telemetry_panel_ONE():
    #return specified panel's/array of panels' voltage
    return 0 ## UNDEFINED
def telemetry_panel_TWO():
    #return specified panel's/array of panels' voltage
    return 0 ## UNDEFINED
def telemetry_panel_THREE():
    #return specified panel's/array of panels' voltage
    return 0 ## UNDEFINED
def telemetry_panel_FOUR():
    #return specified panel's/array of panels' voltage
    return 0 ## UNDEFINED
def telemetry_battery_VOLTAGE():
    #read from the battery balancing circuit
    return 0 ## UNDEFINED
def telemetry_battery_HEATER():
    #read from pin powering the heater mosfet OR HEATER_POWER variable
    return HEATER_POWER

#COMMUNICATION PINS/LINES
def read_PIN_RXPOS_FROM_OBC():
    return 0 ## UNDEFINED
def read_PIN_RXNEG_FROM_OBC():
    return 0 ## UNDEFINED
def set_PIN_TXPOS_TO_OBC(value):
    if (    value):#write a high to TXPOS UNDEFINED
    if (not value):#write a low  to TXPOS UNDEFINED
    else:          #HIGH IMPEDANCE to TXPOS UNDEFINED
def set_PIN_TXNEG_TO_OBC(value):
    if (value):    #write a high to TXNEG UNDEFINED
    if (not value):#write a low  to TXNEG UNDEFINED
    else:          #HIGH IMPEDANCE to TXNEG UNDEFINED
def write_bit_to_OBC(bit_value):
    if(bit_value==1):
        set_PIN_TXPOS_TO_OBC( 1 )
        set_PIN_TXNEG_TO_OBC( 0 )
    if(bit_value==0):
        set_PIN_TXPOS_TO_OBC( 0 )
        set_PIN_TXNEG_TO_OBC( 1 )
def read_bit_from_OBC():
    if( (read_PIN_RXPOS_FROM_OBC())     and  (not read_PIN_RXNEG_FROM_OBC()) ): return 1
    if( (not read_PIN_RXPOS_FROM_OBC()) and  (read_PIN_RXNEG_FROM_OBC())     ): return 0
    else: return 0
    
#COMMAND EXECUTION
def command_payload_ON():
    if(PAYLOAD_POWER == 1):#do nothing
    if(PAYLOAD_POWER == 0):#activate payload supply mosfet UNDEFINED
def command_payload_OFF():
    if(PAYLOAD_POWER == 0):#do nothing
    if(PAYLOAD_POWER == 1):#deactivate payload supply mosfet UNDEFINED
def command_uhf_ON():
    if(UHF_POWER == 1):#do nothing
    if(UHF_POWER == 0):#activate uhf supply  mosfet UNDEFINED
def command_uhf_OFF():
    if(UHF_POWER == 0):#do nothing
    if(UHF_POWER == 1):#deactivate uhf supply mosfet UNDEFINED
def command_xband_ON():
    if(XBAND_POWER == 1):#do nothing
    if(XBAND_POWER == 0):#activate xband supply mosfet UNDEFINED
def command_xband_OFF():
    if(XBAND_POWER == 0):#do nothing
    if(XBAND_POWER == 1):#deactivate xband supply mosfet UNDEFINED
    
#DEPLOY PANELS IF RELEASE SWITCHES INDICATE SATELLITE HAS BEEN EJECTED FROM POD
def RELEASE_ONE():
    #release switch 1, return True  means it's activated
def RELEASE_TWO():
    #release switch 2, return True  means it's activated
def RELEASE_THREE():
    #release switch 3, return True  means it's activated
def RELEASE_FOUR():
    #release switch 4, return True  means it's activated
def deploy_PANELS():
    #activate motors/ release springs to deploy panels
    
while(True):##MAIN WHILE
    #reset the counters appropriately
    #one counter required since both vommand and telemtry frames have EQUAL lengths (56 bit)
    if (position56  == 56) : position56 = 0 #0 to 55, bit position counter reset
    #
    #runs once all four release switches have been activated
    if( RELEASE_ONE() and RELEASE_TWO() and RELEASE_THREE() and RELEASE_FOUR() ): deploy_PANELS()
    #
    ##OBC TO EPS##
    if (read_PIN_SCL_FROM_OBC()) :# if SCL is high then data is coming in from OBC
        if(    read_PIN1_SDA_FROM_OBC() ) : WORD_FROM_OBC_56BIT = (WORD_FROM_OBC_56BIT | (  1<<(55-position56) )) #store 1 bit at position
        if(not read_PIN1_SDA_FROM_OBC() ) : WORD_FROM_OBC_56BIT = (WORD_FROM_OBC_56BIT & (~(1<<(55-position56)))) #store 0 bit at position
        if( ((WORD_FROM_OBC>>32) == STARTING_IN_8BIT) and ((WORD_FROM_OBC&255) == ENDING_IN_8BIT) ):  #start and end validation
            if( ((WORD_FROM_OBC_48BIT>>24)&255 ) == COMMAND_PAYLOAD_ON  ) : command_payload_ON()
            if( ((WORD_FROM_OBC_48BIT>>24)&255 ) == COMMAND_PAYLOAD_OFF ) : command_payload_OFF()
            if( ((WORD_FROM_OBC_48BIT>>16)&255 ) == COMMAND_UHF_ON      ) : command_uhf_ON()
            if( ((WORD_FROM_OBC_48BIT>>16)&255 ) == COMMAND_UHF_OFF     ) : command_uhf_OFF()
            if( ((WORD_FROM_OBC_48BIT>>08)&255 ) == COMMAND_XBAND_ON    ) : command_xband_ON()
            if( ((WORD_FROM_OBC_48BIT>>08)&255 ) == COMMAND_XBAND_OFF   ) : command_xband_OFF()
    while(read_PIN_SCL_FROM_OBC()):#PAUSE....wait for the SCL signal to change to low
    #
    ##EPS TO OBC##
    if ( not read_PIN_SCL_FROM_OBC()):#if SCL is low then data is going to OBC
        WORD_TO_OBC_56BIT =  ( 
                              (TELEMETRY_STARTING_OUT_8BIT<<48) | 
                                (telemetry_payload_STATE()<<46) |
                                    (telemetry_uhf_STATE()<<45) |
                                  (telemetry_xband_STATE()<<43) |
                                    (telemetry_panel_ONE()<<38) |
                                    (telemetry_panel_TWO()<<33) |
                                  (telemetry_panel_THREE()<<28) |
                                   (telemetry_panel_FOUR()<<23) |
                              (telemetry_battery_VOLTAGE()<<18) |
                          (telemetry_battery_TEMPERATURE()<<09) |
                               (telemetry_battery_HEATER()<<08) |
                                      TELEMETRY_ENDING_OUT_8BIT
                            )
        set_PIN_SDA_TO_OBC( WORD_TO_OBC_56BIT & (1<<(55-position56)) )
    while(not read_PIN_SCL_FROM_OBC()):#PAUSE....wait for the SCL signal to change to high
    #
    #increment the position counters
    position56 = position56+1
#MAIN WHILE
