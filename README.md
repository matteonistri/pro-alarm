# pro-alarm
##occurrent
-raspberry 40
-optional: pir sensor  2
-keypad 3
-display lcd 0
-powered speakers 0
-ups ?
-jumper wires 8
-box ?
-x3 magnetic contacts 22
-433 Mhz tx and rx 3
-optional: touch screen display 50?

##features:
-arm/disarm from keypad
-4 digits code request when movement detected
-alarm sound if code wrong or not inserted
-display information on LCD and with speakers
-send slack message

##future features:
-save logs on database
-web server
	web server features:
	-login
	-see logs
	-change pw user
	-change alarm code
	-change number of digits (min.4, max.6)
	-change delay
	-delete logs
	-change slackbot parameters
	-read from database
-optional: pyqt GUI for display

##lcd pins:
d7 p14 - 29(g5)
d6 p13 - 31(g6)
d5 p12 - 33(g13)
d4 p11 - 35(g19)
e p6 - 37(g26)
rs p4 - 38(g20)
p7-8-9-10 - nulla
p1-3-5-16 gnd
p2 5v
p15 5v via 220 ohm
