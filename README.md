# Heterogeneous Multi-Robot Collaboration for Covered Path Planning in Partially Known Dynamic Environments

This repository holds a simulation in a substation environment using ROS together with px4 and husky packages. The example above simulated two UAVs and one husky, but its pretty simple to escalate the simulation to use more agents or even to change the robots.

______________________________________________________________________

<details open>
<summary><b>Dependences:</b></summary> 

- Husky - https://github.com/husky/husky.git
- Mavros - https://github.com/mavlink/mavros.git
- PX4-Autopilot - https://github.com/PX4/PX4-Autopilot.git 
- Map_server - https://github.com/ros-planning/navigation.git
- Motion_planning - https://github.com/ros-planning/navigation.git


</details>

<details open>

<summary><b>Install :</b></summary> 
 
~~~
mkdir -p ~/catkin_mixed/src
cd ~/catkin_mixed 
catkin_make
cd src/ 
git clone  https://github.com/husky/husky.git
git clone  https://github.com/PX4/PX4-Autopilot.git
git clone https://github.com/mavlink/mavros.git
sudo apt install ros-melodic-map-server

~~~~
> ⚠️  Fell free to install all the <a href="https://github.com/ros-planning/navigation.git">ROS Navigation Stack</a> multi-package, indeed we assume that you already have it as a default.
~~~
git clone https://github.com/gelardrc/mixed_mission.git
cd ..
catkin_make
~~~
> ⚠️  Px4 is a complex package, we suggest that if you want to run this code, first make sure that everything in <a href="https://docs.px4.io/main/en/dev_setup/getting_started.html"> Px4 </a> is full functioning and then continue running the next sections. The same for husky, but it is much easier to install.
> 
> ⚠️ Instead of Husky package you can use a version of <a href="https://github.com/RBinsonB/nexus_4wd_mecanum_simulator.git">Nexus robot</a>, modified by the same team that produces this work <a href="">Modified Nexus</a>.
~~~
git clone src/https://github.com/gelardrc/tatiana_nexus.git
~~~
</details>

<details open>

<summary><b>Testing systems</b></summary> 

</details>


