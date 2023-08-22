from collections import OrderedDict

CFG_INFOS_DEFAULTS = {
    '3.35': OrderedDict([
        ('ACTIVE', '{NO YES}'),
        ('PROTLEVEL', 'INTEGER'),
        ('NAMELOCK', '{NO YES}'),
        ('CATENTRY', 'INTEGER'),
        ('POWERON', '{NO YES}'),
        ('MOTPHASES', '{1 2 3}'),
        ('MOTSENSE', '{NORMAL INVERTED}'),
        ('MOTPOLES', 'INTEGER'),
        ('MREGMODE', '{EXT VOLT CURR CURR_VECT TORQUE}'),
        ('NRES', 'FLOAT'),
        ('NCURR', 'FLOAT'),
        ('BCURR', 'INTEGER'),
        ('ICURR', 'INTEGER'),
        ('NVOLT', 'FLOAT'),
        ('IVOLT', 'FLOAT'),
        ('CURRGAIN', '{CUSTOM LOW MEDIUM HIGH}'),
        ('MREGP', 'FLOAT'),
        ('MREGI', 'FLOAT'),
        ('MREGD', 'FLOAT'),
        ('ANTURN', 'INTEGER'),
        ('ANSTEP', 'INTEGER'),
        ('DEFVEL', 'FLOAT'),
        ('STRTVEL', 'FLOAT'),
        ('DEFACCT', 'FLOAT'),
        ('INDEXER', '{INTERNAL InPos EncIn Sync}'),
        ('LNKNAME', 'STRING12'),
        ('SHFTENC', '{NONE InPos EncIn AbsEnc}'),
        ('TGTENC', '{NONE InPos EncIn AbsEnc}'),
        ('CTRLENC', '{NONE InPos EncIn AbsEnc}'),
        ('CTRLERROR', 'INTEGER'),
        ('POSUPDATE', '{NORMAL MEASURE}'),
        ('PCLOOP', '{OFF TGTENC SHFTENC}'),
        ('PCLTAU', 'FLOAT'),
        ('PCLERROR', 'INTEGER'),
        ('PCLMODE', '[SIMPLECHK]'),
        ('PCLDEADBD', 'INTEGER'),
        ('PCLSETLW', 'INTEGER'),
        ('PCLSETLT', 'FLOAT'),
        ('LPPOL', '{NORMAL INVERTED}'),
        ('LMPOL', '{NORMAL INVERTED}'),
        ('HOMEPOL', '{NORMAL INVERTED}'),
        ('EINNTURN', 'INTEGER'),
        ('EINNSTEP', 'INTEGER'),
        ('EINMODE', '{QUAD PULSE+ PULSE-}'),
        ('EINSENSE', '{NORMAL INVERTED}'),
        ('EINAUXPOL', '{NORMAL INVERTED}'),
        ('INPNTURN', 'INTEGER'),
        ('INPNSTEP', 'INTEGER'),
        ('INPMODE', '{QUAD PULSE+ PULSE-}'),
        ('INPSENSE', '{NORMAL INVERTED}'),
        ('INPAUXPOL', '{NORMAL INVERTED}'),
        ('ABSNTURN', 'INTEGER'),
        ('ABSNSTEP', 'INTEGER'),
        ('ABSSENSE', '{NORMAL INVERTED}'),
        ('ABSOFFSET', 'INTEGER'),
        ('SSIDBITS', 'INTEGER'),
        ('SSICODE', '{BINARY GRAY}'),
        ('SSICLOCK', '{125KHz 250KHz 500KHz 1.25MHz 2.5MHz 7.5MHz 12.5MHz '
                     '18.75MHz OFF}'),
        ('SSIDELAY', '{0 5us 10us 20us 30us 50us 100us 500us}'),
        ('SSISTATUS', '{S .S ES OS ...S ..ES ..OS BISS_EWC BISS_WEC '
                      'BISS_E.C BISS_.EC BISS_..C BISS_...}'),
        ('HOMESRC', '{NONE Lim- Lim+ Home EncAux InpAux}'),
        ('HOMETYPE', '{LEVEL PULSE MPULSE}'),
        ('HOMEFLAGS', '[AUTODIR REVERSE SETPOS SLOW NEGEDGE]'),
        ('HOMEPOS', 'INTEGER'),
        ('HOMEVEL', 'FLOAT'),
        ('OUTPSRC', '{AXIS MOTOR SHFTENC TGTENC InPos EncIn AbsEnc Sync '
                    'MEASURE INDEXER}'),
        ('OUTPMODE', '{QUAD PULSE+ PULSE-}'),
        ('OUTPPULSE', '{50ns 200ns 2us 20us}'),
        ('OUTPSENSE', '{NORMAL INVERTED}'),
        ('OUTPAUXSRC', '{LOW HIGH Lim+ Lim- Home EncAux InpAux SyncAux eCAM}'),
        ('OUTPAUXPOL', '{NORMAL INVERTED}'),
        ('INFOASRC', '{LOW HIGH Lim- Lim+ Home EncAux InpAux SyncAux '
                     'PWRCTRL ENABLED ALARM READY WAITING MOVING BOOST '
                     'STEADY eCAM INMOTION .MAIN .ISR .PISR}'),
        ('INFOAPOL', '{NORMAL INVERTED}'),
        ('INFOBSRC', '{LOW HIGH Lim- Lim+ Home EncAux InpAux SyncAux '
                     'PWRCTRL ENABLED ALARM READY WAITING MOVING BOOST '
                     'STEADY eCAM INMOTION .MAIN .ISR .PISR}'),
        ('INFOBPOL', '{NORMAL INVERTED}'),
        ('INFOCSRC', '{LOW HIGH Lim- Lim+ Home EncAux InpAux SyncAux PWRCTRL '
                     'ENABLED ALARM READY WAITING MOVING BOOST STEADY eCAM '
                     'INMOTION .MAIN .ISR .PISR}'),
        ('INFOCPOL', '{NORMAL INVERTED}'),
        ('EXTDISABLE', '{NONE LIMITS Home EncAux InpAux Disable}'),
        ('EXTALARM', '{NONE LIMITS Home EncAux InpAux Disable}'),
        ('EXTBUSY', '{NONE LIMITS Home EncAux InpAux Disable}'),
        ('EXTWARNING', '{NONE LIMITS Home EncAux InpAux Disable}'),
        ('EXTPOWER', '{NONE LIMITS Home EncAux InpAux Disable}'),
        ('EXTHOLD', '{NONE LIMITS Home EncAux InpAux Disable}'),
        ('HOLDTIME', 'FLOAT'),
        ('SSISTRTB', 'INTEGER'),
        ('SSILDC', 'INTEGER'),
        ('SSIMSKNB', 'INTEGER'),
        ('SSIEEPOL', '{ACTIVE_LOW ACTIVE_HIGH}'),
        ('SSIEWPOL', '{ACTIVE_LOW ACTIVE_HIGH}'),
        ('SSIOVF', '{NO YES}')]),

    '1.22': OrderedDict([
        ('ACTIVE', '{NO YES}'),
        ('PROTLEVEL', 'INTEGER'),
        ('NAMELOCK', '{NO YES}'),
        ('CATENTRY', 'INTEGER'),
        ('POWERON', '{NO YES}'),
        ('MOTPHASES', '{1 2 3}'),
        ('MOTSENSE', '{NORMAL INVERTED}'),
        ('MOTPOLES', 'INTEGER'),
        ('MREGMODE', '{EXT VOLT CURR CURR_VECT TORQUE}'),
        ('NRES', 'FLOAT'),
        ('NCURR', 'FLOAT'),
        ('BCURR', 'INTEGER'),
        ('ICURR', 'INTEGER'),
        ('NVOLT', 'FLOAT'),
        ('IVOLT', 'FLOAT'),
        ('CURRGAIN', '{CUSTOM LOW MEDIUM HIGH}'),
        ('MREGP', 'FLOAT'),
        ('MREGI', 'FLOAT'),
        ('MREGD', 'FLOAT'),
        ('ANTURN', 'INTEGER'),
        ('ANSTEP', 'INTEGER'),
        ('DEFVEL', 'FLOAT'),
        ('STRTVEL', 'FLOAT'),
        ('DEFACCT', 'FLOAT'),
        ('INDEXER', '{INTERNAL InPos EncIn}'),
        ('SHFTENC', '{NONE InPos EncIn AbsEnc}'),
        ('TGTENC', '{NONE InPos EncIn AbsEnc}'),
        ('CTRLENC', '{NONE InPos EncIn AbsEnc}'),
        ('CTRLERROR', 'INTEGER'),
        ('POSSRC', '{INDEXER SHFTENC TGTENC}'),
        ('PCLOOP', '{OFF TGTENC}'),
        ('PCLTAU', 'FLOAT'),
        ('PCLERROR', 'INTEGER'),
        ('PCLDEADBD', 'INTEGER'),
        ('PCLSETLW', 'INTEGER'),
        ('PCLSETLT', 'FLOAT'),
        ('LPPOL', '{NORMAL INVERTED}'),
        ('LMPOL', '{NORMAL INVERTED}'),
        ('HOMEPOL', '{NORMAL INVERTED}'),
        ('EINNTURN', 'INTEGER'),
        ('EINNSTEP', 'INTEGER'),
        ('EINMODE', '{QUAD PULSE+ PULSE-}'),
        ('EINSENSE', '{NORMAL INVERTED}'),
        ('EINAUXPOL', '{NORMAL INVERTED}'),
        ('INPNTURN', 'INTEGER'),
        ('INPNSTEP', 'INTEGER'),
        ('INPMODE', '{QUAD PULSE+ PULSE-}'),
        ('INPSENSE', '{NORMAL INVERTED}'),
        ('INPAUXPOL', '{NORMAL INVERTED}'),
        ('ABSNTURN', 'INTEGER'),
        ('ABSNSTEP', 'INTEGER'),
        ('ABSSENSE', '{NORMAL INVERTED}'),
        ('ABSOFFSET', 'INTEGER'),
        ('SSIDBITS', 'INTEGER'),
        ('SSICODE', '{BINARY GRAY}'),
        ('SSICLOCK', '{125KHz 250KHz 500KHz 1.25MHz 2.5MHz 7.5MHz 12.5MHz '
                     '18.75MHz OFF}'),
        ('SSIDELAY', '{0 5us 10us 20us 30us 50us 100us 500us}'),
        ('SSISTATUS', '{S .S ES OS}'),
        ('HOMESRC', '{NONE Lim- Lim+ Home EncAux InpAux}'),
        ('HOMETYPE', '{LEVEL PULSE MPULSE}'),
        ('HOMEFLAGS', '[AUTODIR REVERSE SETPOS SLOW NEGEDGE]'),
        ('HOMEPOS', 'INTEGER'),
        ('HOMEVEL', 'FLOAT'),
        ('OUTPSRC', '{AXIS INDEXER SHFTENC TGTENC InPos EncIn Sync}'),
        ('OUTPMODE', '{QUAD PULSE+ PULSE-}'),
        ('OUTPPULSE', '{50ns 200ns 2us 20us}'),
        ('OUTPSENSE', '{NORMAL INVERTED}'),
        ('OUTPAUXSRC', '{LOW HIGH Lim+ Lim- Home EncAux InpAux SyncAux}'),
        ('OUTPAUXPOL', '{NORMAL INVERTED}'),
        ('INFOASRC', '{LOW HIGH Lim- Lim+ Home EncAux InpAux SyncAux ENABLE '
                     'ALARM READY MOVING BOOST STEADY .MAIN .ISR}'),
        ('INFOAPOL', '{NORMAL INVERTED}'),
        ('INFOBSRC', '{LOW HIGH Lim- Lim+ Home EncAux InpAux SyncAux ENABLE '
                     'ALARM READY MOVING BOOST STEADY .MAIN .ISR}'),
        ('INFOBPOL', '{NORMAL INVERTED}'),
        ('INFOCSRC', '{LOW HIGH Lim- Lim+ Home EncAux InpAux SyncAux ENABLE '
                     'ALARM READY MOVING BOOST STEADY .MAIN .ISR}'),
        ('INFOCPOL', '{NORMAL INVERTED}'),
        ('EXTALARM', '{NONE SOME}'),
        ('EXTWARNING', '{NONE SOME}')])
}

