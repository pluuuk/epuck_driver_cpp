from sensor_msgs.msg import Imu
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry
import time
import rospy
import numpy


def storeMesg(mes):
    global index, elapsed
    lacc =  mes.linear_acceleration
    omg = mes.angular_velocity
    s = elapsed
    x = lacc.x
    y = lacc.y
    z =  lacc.z
    ox = omg.x
    oy = omg.y
    oz = omg.z
    for i,v in enumerate([s,x,y,z,ox,oy,oz]):
        store[index][i] = v
    index+=1
    print(index)


index = 0
max_samples = 99999
store = numpy.ndarray(shape=(max_samples,7))


pub = rospy.Subscriber("/epuck_robot_1/accel", Imu, storeMesg)



captureTime = 100 # seconds

epoch = time.time()
elapsed = 0
while elapsed < captureTime:
    elapsed += time.time() - epoch
    print(elapsed)

store = store[0:index,:]
numpy.savetxt("calibration.csv", store, delimiter=",")
 