import ArtEngine as e

class Data:
    def __init__(self):
        pass

global D
D = Data()

def init_globals():
    global D
    D.hb = e.HeartBeat(.25, sonar_test)
    D.l = e.Devices.PiFaceLED(2)
    D.l.turn_on()
    D.switchOffButton = e.Devices.PiFaceBUTTON(2)
    D.killSwitch = e.Devices.PiFaceBUTTON(2)
    D.irsensor1 = e.Sensors.IrSensor(1)
    D.sonarSensor = e.Sensors.SonarDistance(7, 7)
    D.lights = []
    D.count = 0
    for i in range(3,7):
        D.lights.append(e.Devices.PiFaceLED(i))

def sonar_test():
    D.sonarSensor.update()
    print "distance: " + str(D.sonarSensor.get_value())
    print "button status: " + str(D.switchOffButton.get_value())

def logic():
    global D
    D.switchOffButton.update()
    D.sonarSensor.update()
    if D.switchOffButton.is_on() == False:
       dist = D.sonarSensor.get_value()
       for light in D.lights:
            if dist/10 > (light.pin-2)*2 or dist == -1:
                light.turn_on()
            else:
                light.turn_off()
    else:
        if D.count % 25 == 0:
            for light in D.lights:
                if light.is_on:
                    light.turn_off()
                else:
                    light.turn_on()
        D.count += 1

    if D.killSwitch.get_value() == 1:
        D.hb.stopSpin()
        for light in D.lights:
            light.turn_off()

def main():
    global D
    init_globals()
    D.hb.spin()
    print "quitting"

main()
