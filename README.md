# Senior Research
Welcome to Avik's senior research project repository!

![Screenshot 2021-08-11 120430](https://user-images.githubusercontent.com/66737209/129063945-218a03af-127b-43a1-a220-23b57edb122d.png)


# Project Abstract
Years of space activity and missile tests have led to the accumulation of more than 1,000,000 pieces of space debris that orbit the earth at speeds of 17,500 mph. This highspeed debris can damage expensive space infrastructure and inhibit future space travel. Current solutions to space debris, termed Active Debris Removal (ADR), are yet to be implemented; as such, this study seeks to determine the feasibility of a comprehensive ADR Mission through the development of a physical 3D printed CubeSat model, simulated ADR Mechanisms, and selection of a potential mission orbit. The physical CubeSat model was developed using CAD and contains select subsystems interfacing with a Raspberry Pi. Python code was developed to collect telemetry data from several sensors connected to the Pi and upload it to a cloud platform. Next, a debris detection program was created by training a model on a compiled dataset of 365 images of space debris objects. The model was implemented on the Pi to detect the objects in live video. Testing of the final program yielded results that partially met the average expected 95% confidence value for each detection. Beyond physical prototyping, robotic arm and tether-net ADR mechanisms were developed and simulated in Inventor. Dynamic motion and stress analysis of these systems upheld their feasibility for real-world implementation. Following simulation, considerations for the mission’s concept of operations led to the selection of a 500-600 km elliptical orbit with the point of deployment being the International Space Station.  

## Engineering Goals
1. The simulation of the tether net launch system shall collect stress analysis data to accurately simulate the ADR system. The net shall have a minimum range of 1m and a diagonal of 2m.  

2. The simulation of the dual-robotic gripper arms shall showcase a small "Chaser" CubeSat with robotic arms that are capable of at least four degrees of freedom. The "Chaser" CubeSat gripper arms shall sufficiently grip the debris. The Cubesat with robotic arms shall undergo dynamic motion analysis.

4. The telemetry data (e.g. temperature, altitude, roll, pitch, yaw) from the Raspberry Pi Sense HAT shall be within 5% of true values.   

5. The image algorithm detection software shall detect space debris with an accuracy of 95%.    

6. The orbital path defined in MATLAB & SIMULINK for the CubeSat shall target dense areas of space debris containing debris that is at least 1m in diameter. 
 

# Research Paper
Here is a link to my research paper: <https://docs.google.com/document/d/1pEW-YvyMPYnvBk7dPMFZDnh8s0JQTRVL-Tm5LXFrZAw/edit?usp=sharing>

Science & Engineering Fair Documents
## Presentation
https://drive.google.com/file/d/1q3D0fl7o08JFdv-ublt1_3PxmefS0VA7/view?usp=sharing
## Quad Chart
https://drive.google.com/file/d/17tT_Lp1UKl6S5kARIaOhyH_IVumxtoDL/view?usp=sharing
## Video
https://drive.google.com/file/d/10r5_0sDWk8axDxte4FRlRki9nOwvmL-M/view?usp=sharing
