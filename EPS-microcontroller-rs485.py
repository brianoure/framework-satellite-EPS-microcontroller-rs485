"""
OBC master, EPS slave
RS485 protocol (4 wire) : TXPOS, TXNEG, RXPOS, RXNEG, GND
"""
bit_captured_flag = 0 #flag indicating whether a bit has been captured or not

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
TELEMETRY_STARTING_OUT_8BIT   = 195   #constantidentifying the telemetry frame header/start
TELEMETRY_ENDING_OUT_8BIT     = 135   #constant  identifying the telemetry frame tail/end

#TELEMETRY CAPTURE
def telemetry_payload_STATE():
    #read from pin powering the payload mosfet OR PAYLOAD_POWER variable i.e returning 1 or 0
    return PAYLOAD_POWER 
def telemetry_uhf_STATE():
    #read from pin powering the uhf mosfet OR UHF_POWER variable i.e returning 1 or 0
    return UHF_POWER
def telemetry_xband_STATE():
    #read from pin powering the xband mosfet OR XBAND_POWER variable i.e returning 1 or 0
    return XBAND_POWER
def telemetry_panel_ONE():
    #return specified panel's/array of panels' voltage i.e returning value between 0 to 32
    return 0 ## UNDEFINED
def telemetry_panel_TWO():
    #return specified panel's/array of panels' voltage i.e returning value between 0 to 32
    return 0 ## UNDEFINED
def telemetry_panel_THREE():
    #return specified panel's/array of panels' voltage i.e returning value between 0 to 32
    return 0 ## UNDEFINED
def telemetry_panel_FOUR():
    #return specified panel's/array of panels' voltage i.e returning value between 0 to 32
    return 0 ## UNDEFINED
def telemetry_battery_VOLTAGE():
    #read from the battery balancing circuit  the 4s2p battery pack voltage i.e returning value between 0 to 32
    return 0 ## UNDEFINED
def telemetry_battery_TEMPERATURE():
    #read from pin powering the heater mosfet OR HEATER_POWER variable i.e returning value between -255 to 256
    return 0
def telemetry_battery_HEATER():
    #read from pin powering the heater mosfet OR HEATER_POWER variable
    return HEATER_POWER

#COMMUNICATION PINS/LINES
def read_PIN_RXPOS_FROM_OBC():
    return 0 ## return 1 or 0 , UNDEFINED
def read_PIN_RXNEG_FROM_OBC():
    return 0 ## return 1 or 0 , UNDEFINED
def set_PIN_TXPOS_TO_OBC(value):
    if (    value):pass#write a high to TXPOS UNDEFINED
    if (not value):pass#write a low  to TXPOS UNDEFINED
    else:          pass#HIGH IMPEDANCE to TXPOS UNDEFINED
def set_PIN_TXNEG_TO_OBC(value):
    if (value):    pass#write a high to TXNEG UNDEFINED
    if (not value):pass#write a low  to TXNEG UNDEFINED
    else:          pass#HIGH IMPEDANCE to TXNEG UNDEFINED
def write_bit_to_OBC(bit_value):
    if(bit_value==1 or bit_value==True):
        set_PIN_TXPOS_TO_OBC( 1 )
        set_PIN_TXNEG_TO_OBC( 0 )
    if(bit_value==0 or bit_value==False):
        set_PIN_TXPOS_TO_OBC( 0 )
        set_PIN_TXNEG_TO_OBC( 1 )
def read_bit_from_OBC(): #return 1 or 0
    if( (not read_PIN_RXPOS_FROM_OBC()) and  (not read_PIN_RXNEG_FROM_OBC()) ): return 3 #intermission, waiting for the next bit
    if( (not read_PIN_RXPOS_FROM_OBC()) and  (    read_PIN_RXNEG_FROM_OBC()) ): return 0
    if( (    read_PIN_RXPOS_FROM_OBC()) and  (not read_PIN_RXNEG_FROM_OBC()) ): return 1
    if( (    read_PIN_RXPOS_FROM_OBC()) and  (    read_PIN_RXNEG_FROM_OBC()) ): return 3 #intermission, waiting for the next bit
    else: return 3
    
#COMMAND EXECUTION
def command_payload_ON():
    if(PAYLOAD_POWER == 1):pass#do nothing
    if(PAYLOAD_POWER == 0):pass#activate payload supply mosfet UNDEFINED
def command_payload_OFF():
    if(PAYLOAD_POWER == 0):pass#do nothing
    if(PAYLOAD_POWER == 1):pass#deactivate payload supply mosfet UNDEFINED
def command_uhf_ON():
    if(UHF_POWER == 1):pass#do nothing
    if(UHF_POWER == 0):pass#activate uhf supply  mosfet UNDEFINED
def command_uhf_OFF():
    if(UHF_POWER == 0):pass#do nothing
    if(UHF_POWER == 1):pass#deactivate uhf supply mosfet UNDEFINED
def command_xband_ON():
    if(XBAND_POWER == 1):pass#do nothing
    if(XBAND_POWER == 0):pass#activate xband supply mosfet UNDEFINED
def command_xband_OFF():
    if(XBAND_POWER == 0):pass#do nothing
    if(XBAND_POWER == 1):pass#deactivate xband supply mosfet UNDEFINED
    
#DEPLOY PANELS IF RELEASE SWITCHES INDICATE SATELLITE HAS BEEN EJECTED FROM POD
def RELEASE_ONE(  ):pass#release switch 1, return True  means it's activated, UNDEFINED
def RELEASE_TWO(  ):pass#release switch 2, return True  means it's activated, UNDEFINED
def RELEASE_THREE():pass#release switch 3, return True  means it's activated, UNDEFINED
def RELEASE_FOUR( ):pass#release switch 4, return True  means it's activated, UNDEFINED
def deploy_PANELS():pass#activate motors/ release springs to deploy panels, UNDEFINED
    
while(True):##MAIN WHILE
    #reset the counters appropriately
    #one counter required since both vommand and telemtry frames have EQUAL lengths (56 bit)
    if (position56  == 56) : position56 = 0 #0 to 55, bit position counter reset
    if(bit_captured_flag==True) : bit_captured_flag=False
    #
    #runs once all four release switches have been activated
    if( RELEASE_ONE() and RELEASE_TWO() and RELEASE_THREE() and RELEASE_FOUR() ): deploy_PANELS()
    #
    ##OBC TO EPS......COMMAND##
    if( read_bit_from_OBC()==1 and (not bit_captured_flag) ) : 
       WORD_FROM_OBC_56BIT = (WORD_FROM_OBC_56BIT | (  1<<(55-position56) )) #store 1 bit at position
       bit_captured_flag = True
       while( read_bit_from_OBC()==1 ):pass #wait for the current bit transmission to run its course. No defined wait times/asynchronous
       while( read_bit_from_OBC()==3 ):pass #wait for the intermission to pass. No defined wait times/asynchronous
    if( read_bit_from_OBC()==0 and (not bit_captured_flag)) :
       WORD_FROM_OBC_56BIT = (WORD_FROM_OBC_56BIT & (~(1<<(55-position56)))) #store 0 bit at position
       bit_captured_flag = True
       while( read_bit_from_OBC()==0 ):pass #wait for the current bit transmission to run its course
       while( read_bit_from_OBC()==3 ):pass #wait for the intermission to pass
    #
    #Check if we have any commands issued in the command frame
    """making copies to prevent alteration to original data"""
    WORD_FROM_OBC_56BIT_copy1 = WORD_FROM_OBC_56BIT
    WORD_FROM_OBC_56BIT_copy2 = WORD_FROM_OBC_56BIT
    WORD_FROM_OBC_56BIT_copy3 = WORD_FROM_OBC_56BIT
    WORD_FROM_OBC_56BIT_copy4 = WORD_FROM_OBC_56BIT
    WORD_FROM_OBC_56BIT_copy5 = WORD_FROM_OBC_56BIT
    WORD_FROM_OBC_56BIT_copy6 = WORD_FROM_OBC_56BIT
    WORD_FROM_OBC_56BIT_copy7 = WORD_FROM_OBC_56BIT
    WORD_FROM_OBC_56BIT_copy8 = WORD_FROM_OBC_56BIT
    if( ((WORD_FROM_OBC_56BIT_copy1>>40) == COMMAND_STARTING_IN_16BIT) and ((WORD_FROM_OBC_56BIT_copy2&255) == COMMAND_ENDING_IN_8BIT) ):  #start and end validation
       if( ((WORD_FROM_OBC_56BIT_copy3>>24)&255 ) == COMMAND_PAYLOAD_ON_8BIT  ) : command_payload_ON()
       if( ((WORD_FROM_OBC_56BIT_copy4>>24)&255 ) == COMMAND_PAYLOAD_OFF_8BIT ) : command_payload_OFF()
       if( ((WORD_FROM_OBC_56BIT_copy5>>16)&255 ) == COMMAND_UHF_ON_8BIT      ) : command_uhf_ON()
       if( ((WORD_FROM_OBC_56BIT_copy6>>16)&255 ) == COMMAND_UHF_OFF_8BIT     ) : command_uhf_OFF()
       if( ((WORD_FROM_OBC_56BIT_copy7>>8 )&255 ) == COMMAND_XBAND_ON_8BIT    ) : command_xband_ON()
       if( ((WORD_FROM_OBC_56BIT_copy8>>8 )&255 ) == COMMAND_XBAND_OFF_8BIT   ) : command_xband_OFF()
    ##EPS TO OBC.......TELEMETRY##
    """making copies to prevent alteration to original data"""
    TELEMETRY_STARTING_OUT_8BIT_copy = TELEMETRY_STARTING_OUT_8BIT
    TELEMETRY_ENDING_OUT_8BIT_copy   = TELEMETRY_ENDING_OUT_8BIT
    WORD_TO_OBC_56BIT =  ( 
                          (TELEMETRY_STARTING_OUT_8BIT_copy<<48) | 
                           (telemetry_payload_STATE()<<46)       |
                           (telemetry_uhf_STATE()<<45)           |
                           (telemetry_xband_STATE()<<43)         |
                           (telemetry_panel_ONE()<<38)           |
                           (telemetry_panel_TWO()<<33)           |
                           (telemetry_panel_THREE()<<28)         |
                           (telemetry_panel_FOUR()<<23)          |
                           (telemetry_battery_VOLTAGE()<<18)     |
                           (telemetry_battery_TEMPERATURE()<<9 ) |
                           (telemetry_battery_HEATER()<<8 )      |
                           TELEMETRY_ENDING_OUT_8BIT_copy
                         )
    write_bit_to_OBC( WORD_TO_OBC_56BIT & (1<<(55-position56)) )
    #
    #increment the position counters
    position56 = position56+1
#MAIN WHILE
