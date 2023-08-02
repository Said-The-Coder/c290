"""one_arm_robot controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot,Keyboard

# create the Robot instance.
bot = Robot()


# get the time step of the current world.
timestep = 64

shoulder_lift=bot.getDevice('shoulder_lift_joint')
shoulder_pan=bot.getDevice('shoulder_pan_joint')
elbow=bot.getDevice('elbow_joint')

wrist_1=bot.getDevice('wrist_1_joint')
wrist_2=bot.getDevice('wrist_2_joint')
wrist_3=bot.getDevice('wrist_3_joint')

finger_1=bot.getDevice('palm_finger_1_joint')
finger_1_lower_knuckle=bot.getDevice('finger_1_joint_1')
finger_1_middle_knuckle=bot.getDevice('finger_1_joint_2')
finger_1_upper_knuckle=bot.getDevice('finger_1_joint_3')

finger_2=bot.getDevice('palm_finger_2_joint')
finger_2_lower_knuckle=bot.getDevice('finger_2_joint_1')
finger_2_middle_knuckle=bot.getDevice('finger_2_joint_2')
finger_2_upper_knuckle=bot.getDevice('finger_2_joint_3')

finger_3_lower_knuckle=bot.getDevice('finger_middle_joint_1')
finger_3_middle_knuckle=bot.getDevice('finger_middle_joint_2')
finger_3_upper_knuckle=bot.getDevice('finger_middle_joint_3')

sensor=bot.getDevice('distance_sensor')
sensor.enable(timestep)



def move_bot(a=0,b=0,c=0,d=0,e=0,f=0,g=0.17,h=0.05,i=0,j=-0.06):
    shoulder_lift.setPosition(a)
    shoulder_pan.setPosition(b)
    elbow.setPosition(c)
    wrist_1.setPosition(d)
    wrist_2.setPosition(e)
    wrist_3.setPosition(f)
    
    finger_1.setPosition(g)
    finger_2.setPosition(g)
    
    finger_1_lower_knuckle.setPosition(h)
    finger_2_lower_knuckle.setPosition(h)
    finger_3_lower_knuckle.setPosition(h)
    
    finger_1_middle_knuckle.setPosition(i)
    finger_2_middle_knuckle.setPosition(i)
    finger_3_middle_knuckle.setPosition(i)
    
    finger_1_upper_knuckle.setPosition(j)
    finger_2_upper_knuckle.setPosition(j)
    finger_3_upper_knuckle.setPosition(j)
   
move_bot()

def add_delay(delay_time_steps):
    time_counter=0
    while bot.step(timestep)!=-1:
        if(time_counter>=delay_time_steps):
            break
        time_counter+=1
        
while bot.step(timestep)!=-1:
    val=sensor.getValue()
    if(val<400):
        move_bot(0.15,1.57,-0.1,-0.04,h=0.3,i=0.3)
        add_delay(10)
        
        move_bot(-0.1,1.57,0,0,h=0.3,i=0.3)
        add_delay(10)
        
        move_bot(-0.1,-0.1,0,0,h=0.3,i=0.3)
        add_delay(10)
        
        move_bot(-0.1,-0.1,0,0,h=0.05,i=0)
        add_delay(10)
        
        move_bot(-0.1,1.57)
        add_delay(10)
        
     else:
         move_bot(0.15,1.57,-0.1,-0.04)
  
# shoulder_lift_pos=0
# shoulder_pan_pos=0
# elbow_pos=0
# wrist_1_pos=0
# wrist_2_pos=0
# wrist_3_pos=0)

# finger_pos=0.17
# lower_knuckle_pos=0.05
# middle_knuckle_pos=0
# upper_knuckle_pos=-0.06


 # motor = robot.getDevice('motorname')
 # ds = robot.getDevice('dsname')
 # ds.enable(timestep)
# Main loop:
# - perform simulation steps until Webots is stopping the controller
# while bot.step(timestep) != -1:
    # keypressed=keyboard.getKey()
    # if(keypressed==317):#downkey
        # shoulder_lift_pos+=0.01
    # elif(keypressed==315):#uparrow
        # shoulder_lift_pos-=0.01
    # elif(keypressed==314):#leftarrow
        # shoulder_pan_pos+=0.01
    # elif(keypressed==316):#rightarrow
        # shoulder_pan_pos-=0.01
    # elif(keypressed==87):#Wkey
        # elbow_pos-=0.01
    # elif(keypressed==83):#Skey
        # elbow_pos+=0.01
    # elif(keypressed==65):#Akey
        # wrist_1_pos+=0.01
    # elif(keypressed==68):#Dkey
        # wrist_1_pos-=0.01
    # elif(keypressed==49):#1
        # wrist_2_pos+=0.01
    # elif(keypressed==50):#2
        # wrist_2_pos-=0.01
    # elif(keypressed==51):#3
        # wrist_3_pos+=0.01
    # elif(keypressed==52):#4
        # wrist_3_pos-=0.01
        
    # elif(keypressed==53):#5
        # finger_pos+=0.01
    # elif(keypressed==54):#6
        # finger_pos-=0.01
    # elif(keypressed==55):#7
        # lower_knuckle_pos+=0.01
    # elif(keypressed==56):#8
        # lower_knuckle_pos-=0.01
    # elif(keypressed==57):#9
        # middle_knuckle_pos+=0.01
    # elif(keypressed==48):#0
        # middle_knuckle_pos-=0.01   
    # elif(keypressed==45):#-
        # upper_knuckle_pos+=0.01
    # elif(keypressed==61):#+
        # upper_knuckle_pos-=0.01
        
    # move_bot(0.15,1.57,-0.1,wrist_2_pos,wrist_3_pos,finger_pos,0.3,0.3,upper_knuckle_pos)
