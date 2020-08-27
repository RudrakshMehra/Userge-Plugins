​from​ ​userge​ ​import​ ​userge​, ​Message​

​LOG​ ​=​ ​userge​.​getLogger​(​__name__​)  ​# logger object​

​CHANNEL​ ​=​ ​userge​.​getCLogger​(​__name__​)  ​# channel logger object​

​@​userge​.​on_cmd​(​"rudraksh"​, ​about​=​"help text to this cool command"​)  ​# adding handler and help text to .test command​
​async​ ​def​ ​testing​(​message​: ​Message​):
   ​LOG​.​info​(​"starting test command..."​)  ​# log to console​

   ​await​ ​message​.​edit​(​"trying..."​, ​del_in​=​5​)  ​# this will be automatically deleted after 5 sec​

   ​await​ ​CHANNEL​.​log​(​"testing completed yay!"​)  ​# log to channel
