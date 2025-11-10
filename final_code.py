from lib import navigation
from lib import components
from machine import Pin, PWM, I2C
from utime import sleep

class Bumblebee:
    # initialisation of components
    def __init__(self, MotorLeft, MotorRight, LinAc, sensor_pins, led_pins):
        self.MotorLeft = MotorLeft
        self.MotorRight = MotorRight
        self.LinAc = LinAc
        self.s1=Pin(sensor_pins[0],Pin.IN,Pin.PULL_DOWN)
        self.s2=Pin(sensor_pins[1],Pin.IN,Pin.PULL_DOWN)
        self.s3=Pin(sensor_pins[2],Pin.IN,Pin.PULL_DOWN)
        self.s4=Pin(sensor_pins[3],Pin.IN,Pin.PULL_DOWN)
        self.led_orange = Pin(led_pins[0], Pin.OUT, Pin.PULL_DOWN)
        self.led_red = Pin(led_pins[1], Pin.OUT, Pin.PULL_DOWN)

    # direction is "left", "right" or "around"
    # turning process consists of an intial short timed turn to clear any white lines, then continuous turning until outer middle sensor is back on track
    def Turn(self, direction):
        print("turning")
        reverse_time = 1.5
        turn_time = 0.6
        if direction == "right":
            # turn right
            self.MotorLeft.Reverse(speed=65)
            self.MotorRight.Forward(speed=90)
            sleep(turn_time)
            while not self.s3.value():
                pass

        elif direction == "left":
            # turn left
            self.MotorLeft.Forward(speed=90)
            self.MotorRight.Reverse(speed=65)
            sleep(turn_time)
            while not self.s2.value():
                pass
                
        elif direction == "around":
            # turn around
            self.MotorLeft.Reverse(speed=50)
            self.MotorRight.Forward(speed=50)
            sleep(reverse_time)
            while not self.s3.value():
                pass
            sleep(0.3)
        # stop after turn
        self.MotorLeft.off()
        self.MotorRight.off()
        
    # goes from start to end using navigation.Turns()
    def Traverse(self, start, end):
        print("traversing")
        path = navigation.Turns(start, end)
        print(path)
        for each in path:
            self.led_orange.value(1)

            # line follow to next junction i.e until returns 'stop'
            while self.Line_Follow() is not "stop":
                self.Line_Follow()
                
            # takes small step  to clear junction
            while self.s1.value() or self.s4.value():
                self.MotorLeft.Forward()
                self.MotorRight.Forward()
            self.MotorLeft.off()
            self.MotorRight.off()
         
            print(each, "turning")   
            self.Turn(each)
            
        self.led_orange.value(0)

    # hard coded box approach, including forklift control
    # includes faulty QR reader code - this was not used in the final competition, and is hence commented out
    def Box_Approach(self):
        print("approaching")
        qr_value = "none"
        approaching = True
        
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)   
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.5)
        self.Line_Follow(base=72)
        sleep(0.1)
        self.Line_Follow(base=72)
        sleep(0.1)

        sleep(0.5)
        
        self.MotorLeft.off()
        self.MotorRight.off()
        
        sleep(0.5)
        #drop forklift
        self.LinAc.Fork_Lift(1, "long")
    
        # QR reader code, including LED control
        # should have been able to return a str(node) value for the box drop-off location
#         while approaching:
#             if qr_value == "none":
#                 #qr_value = components.QR_Read()
#                 self.led_red.value(1)
#             else:
#                 self.led_red.value(0)
            
        self.led_red.value(0) # LED control since QR reader was not being used

        distance = components.Get_Distance()
        # if distance is not yet small enough, continue moving forwards
        while distance > 10 :
            print("too far, dist > 20")
            distance = components.Get_Distance()
            # line follow
            self.led_orange.value(1)
            self.MotorLeft.Forward(speed=50)
            self.MotorRight.Forward(speed=50)
            sleep(0.08)
        sleep(0.5)
        # continue moving forward a little to pick up the box
        self.MotorLeft.Forward(speed=40)
        self.MotorRight.Forward(speed=40)
        sleep(0.2)

        # stop in front of the box
        self.MotorLeft.off()
        self.MotorRight.off()
        
        sleep(1)
        # raise forklift
        self.LinAc.Fork_Lift(0, "medium")
        
        # reverse out
        self.MotorLeft.Reverse(speed=50)
        self.MotorRight.Reverse(speed=50)
        sleep(1)
        
        # turn 180 degrees
        self.Turn("around")

        approaching = False
        # self.led_orange.value(0)
        
        # should have used the following line to return the QR reader value instead, but was not able to implement it
        # return navigation.Translate_QR(qr_value)
        return ['ol5_port','pl6_port']
    
    # code regarding bay level-dependent forklift control is commented out, as only the lower bays were used during the competition
    # pass in "u" or "l" as level argument
    # if deposit fails, try again 
    def Box_Deposit(self):
        print("depositing")
        depositing = True
        self.led_orange.value(1)
        while depositing:
            
            self.LinAc.Fork_Lift(0, "medium")          
            
            self.Line_Follow(base=60)
            sleep(0.1)
            self.Line_Follow(base=60)
            sleep(0.1)
            self.Line_Follow(base=60)
            sleep(0.1)
            self.Line_Follow(base=60)
            sleep(0.1)
            self.Line_Follow(base=60)
            sleep(0.1)
            self.Line_Follow(base=60)
            sleep(0.1)
            self.Line_Follow(base=60)
            sleep(0.1)
            self.Line_Follow(base=60)
            # move to deposit position
            self.MotorLeft.Forward(speed=50)
            self.MotorRight.Forward(speed=50)
            sleep(0.7)

            # following code is commented out as only the lower bays were used during the competition
#             # upper procedure, bay is flush to floor
#             if level == "u":
#                 self.LinAc.Fork_Lift(0, "long")
# 
#             # lower procedure, bay is 20mm above floor, only drop forklift slightly
#             else:
            self.LinAc.Fork_Lift(1, "short")
            sleep(0.5)
            
            # reverse out
            self.MotorLeft.Reverse(speed=60)
            self.MotorRight.Reverse(speed=60)
            sleep(0.65)
            self.MotorLeft.off()
            self.MotorRight.off()
            
            # check if deposit successful
            distance = components.Get_Distance()
            if distance < 10:
                depositing = True
            else:   
                depositing = False
                self.led_orange.value(0)

        # raise fork
        self.LinAc.Fork_Lift(0, "long")

    # follows line until junction reached, then stop
    def Line_Follow(self,base=95):
        #sensors left to right
        s1 = self.s1
        s2 = self.s2
        s3 = self.s3
        s4 = self.s4
        MotorRight = self.MotorRight
        MotorLeft = self.MotorLeft

        sensor_state = f"{s1.value()},{s2.value()},{s3.value()},{s4.value()}"

        decision = navigation.truth_table[sensor_state]

        if decision == "straight":
            # move forwards
            MotorLeft.Forward(base)
            MotorRight.Forward(base)

        elif decision != "stop":
            # adjust left or right according to decision
            self.Adjust_Path(decision,0.4*base)

        else:
            # stop
            MotorLeft.off()
            MotorRight.off()
        return decision

    # coefficient ranges from 0 to 1000 but should be ballpark 10-100
    def Adjust_Path(self, direction, coefficient):
        if direction == "left":
            # adjust left
            MotorRight.Forward(100)
            MotorLeft.Forward(coefficient)

        elif direction == "right":
            # adjust right
            MotorLeft.Forward(100)
            MotorRight.Forward(coefficient)

# main function
if __name__ == "__main__":
    
    print("starting")
    MotorLeft = components.Motor(4,5)
    MotorRight = components.Motor(7,6)
    LinAc = components.Actuator(3,2)
    button = Pin(15,Pin.IN,Pin.PULL_DOWN)

    BmblB = Bumblebee(MotorLeft, MotorRight, LinAc, [0, 1, 8, 9], [18, 14])

    # detect button press to start run
    start = False
    while not start:
        if button.value() == 1:
            start = True
            sleep(0.5)
    BmblB.LinAc.Fork_Lift(0,"long")
    # hard code get off the initial black square
    MotorLeft.Forward()
    MotorRight.Forward()
    sleep(1)

    # follow line to first node "start_zone"
    BmblB.Line_Follow()

    # acknowledge position and initialize next bay value
    current_position = "start_zone"
    next_bay = 1
    port = 0
    while True:
        # follow line to next bay
        print(current_position)
        print(next_bay)
        BmblB.Traverse(current_position, f"bay{next_bay}")
        sleep(1)
        # hard coded box pickup, should also obtain QR reading as a str(node)
        dropoff_port = BmblB.Box_Approach()
        # dropoff_port = navigation.Translate_QR(qr_reading)

        # acknowledge position
        current_position = f"bay{next_bay}"

        # follow line to dropoff intersection
        BmblB.Traverse(current_position, dropoff_port[port])

        # hard coded box dropoff
        BmblB.Box_Deposit()
        BmblB.Turn("around")

        #acknowledge position
        current_position = dropoff_port[port]
        
        port+=1
        next_bay += 1
        next_bay = next_bay % 4