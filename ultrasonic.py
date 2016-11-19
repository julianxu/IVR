import ev3dev.ev3 as ev3
import time
import utilities as util

def rotateUltraSonic():
    print("Rotate ultrasonic")

    medMotor = ev3.MediumMotor('outA')
    medMotor.connected

    #medMotor.run_to_abs_pos(position_sp=0)
    #time.sleep(1)
    #medMotor.run_to_abs_pos(duty_cycle_sp=25, position_sp=180)
    #time.sleep(1)
    medMotor.run_to_rel_pos(position_sp=180)
    time.sleep(1)
    medMotor.run_to_rel_pos(position_sp=180)
    time.sleep(1)

#    medMotor.run_timed(duty_cycle_sp=-25, time_sp=2000)
#    time.sleep(1)
#    medMotor.run_timed(duty_cycle_sp=-25, time_sp=1000)
#    time.sleep(1)
