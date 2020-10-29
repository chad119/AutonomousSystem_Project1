# AutonomousSystem_Project1 @ University of California, Irvine
This project has three parts:<br />
- Part_1 my_teleop_node:<br />
    1. Create a node (under the scripts folder) named “​my_teleop_node​”. 
    2. This node will subscribe to the topic “/turtle1/cmd_vel”. 
    3. Writing Python code that takes input from the keyboard. Whenever the user hits the “w” key, the turtle should move forward. Whenever the user hits        the “s” key, the turtle should move backwards. Whenever the user hits the key “a” then the turtle should rotate to the left without moving.       
       Finally, when the user hits the key “d” the turtle should rotate to the right without moving. 
- Part_2 swim_node: 
    1. Create a new node in the same package and named swim_node under the scripts folder. 
    2. Upon initialization, this node should pick some random linear velocity and some random angular velocity. 
    3. The turtle then swims in a figure 8 shape using these random velocities. 
- Part_3 swim_to_goal: 
    1. Create a new node in the same package and named swim_to_goal under the scripts folder. 
    2. Upon initialization, this node will ask the user to enter two numbers called x_goal and y_goal 
    3. Calculate the error between the turtle current position (current_x, current_y) and the goal(x_goal,y_goal). The turtle pose can be retrieved by          subscribing to /turtle1/pose topic. 
       This error can be computed as: 
         - Error_position = Euclidean distance between (current_x, current_y) and (x_goal,y_goal) 
         - Error_angle = atan2(Error_position) 
    4. Set the turtle velocity to be proportional to the error, i.e., when the turtle is far away from the goal it should move faster than when the              turtle is near the goal, and should not move when it arrives to the goal. Once you calculate the velocities, you can publish them on the                  /turtle1/cmd_vel topic. 
    5. Check if Error_position is smaller than 0.5, then you can stop moving the turtle. Else, go to Step 3. 6. When the turtle arrives to the final            goal, it should ask the user for a new x_goal and y_goal and then move the turtle accordingly.
