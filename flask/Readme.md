### Start.sh

start.sh is een bash script dat wordt uitgevoerd door gebruik van het volgende commando on de terminal in de flask folder:
```
bash start.sh
```

star.sh runt main.py en motion.py parallel, waardoor deze files via een textfile kunnen communiceren.

### Communicate_motion
Communicate_motion is de file die wordt gebruikt voor de communicatie tussen motion.py en main.py.
Main.py schrijf een 1 als motion sensor aan moet en een 0 als motionsensor uit moet.
Motion.py leest deze file en weet dan of hij de motionsensor aan of uit moet zetten.
