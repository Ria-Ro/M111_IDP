import navigation
from machine import Pin, PWM, I2C
from utime import sleep
from lib.tiny_code_reader import TinyCodeReader
from lib.VL53L0X import VL53L0X

class Actuator:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
           
    # 1 for down, 0 for up
    #height should be "long" or "short"
    # function should incorporate time delays for appropriate extension + retraction
    def Fork_Lift(self, direction, distance):
        if distance == "long":
            movement_time = 4.9
        else:
            movement_time = 0.7
    
    # Use PWM to control forklift motor
        self.set(direction, 100) # set full speed in given direction
        sleep(movement_time) # adjust as needed for full extension
        self.set(0,0)

    def set(self, dir, speed):
        self.mDir.value(dir)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

class Motor:
    def __init__(self, dirPin, PWMPin):
        self.mDir = Pin(dirPin, Pin.OUT)  # set motor direction pin
        self.pwm = PWM(Pin(PWMPin))  # set motor pwm pin
        self.pwm.freq(1000)  # set PWM frequency
        self.pwm.duty_u16(0)  # set duty cycle - 0=off
        
    def off(self):
        self.pwm.duty_u16(0)
        
    def Forward(self, speed=100):
        self.mDir.value(0)                     # forward = 0 reverse = 1 motor
        self.pwm.duty_u16(int(65535 * speed / 100))  # speed range 0-100 motor

    def Reverse(self, speed=100):
        self.mDir.value(1)
        self.pwm.duty_u16(int(65535 * speed / 100))

# returns str(node) or str("none") if no code read
def QR_Read():
    i2c_bus = I2C(id=1, scl=Pin(11), sda=Pin(10), freq=400000)
    i2c_devs = i2c_bus.scan()
    assert len(i2c_devs) == 1 # This demo requires exactly one device
    assert i2c_devs[0] == 12 # Expected device
    code_reader = TinyCodeReader(i2c_bus)

    code = code_reader.poll()
    if code is not None:
        node = navigation.Translate_QR(code)
        return node
    else:
        return "none"

# Use VL53L0X sensor to get distance in mm
def Get_Distance():
    i2c_bus = I2C(id=0, sda=Pin(12), scl=Pin(13))
    sleep(0.09)
    vl53l0 = VL53L0X(i2c_bus)
    vl53l0.set_Vcsel_pulse_period(vl53l0.vcsel_period_type[0], 18)
    vl53l0.set_Vcsel_pulse_period(vl53l0.vcsel_period_type[1], 14)

    vl53l0.start()
    sleep(0.09)
    distance = vl53l0.read()
    vl53l0.stop()
    print(distance - 50)
    return (distance-50)