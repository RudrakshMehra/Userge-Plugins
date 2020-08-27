​from​ ​userge​ ​import​ ​userge​, ​Message​

​LOG​ ​=​ ​userge​.​getLogger​(​__name__​)  ​# logger object​

​CHANNEL​ ​=​ ​userge​.​getCLogger​(​__name__​)  ​# channel logger object​

​@​userge​.​on_cmd​(​"rudraksh"​, ​about​=​"help text to this command"​)  ​# adding handler and help text to .test command​
​async​ ​def​ ​testing​(​message​: ​Message​):
   ​LOG​.​info​(​"starting dummy command..."​)  ​# log to console​

   ​await​ ​CHANNEL​.​log​(​"testing completed yay!"​)  ​# log to channel
