# Object-Avoidance-Robot-
This repository contains the implementation of an Autonomous Finite State Machine (AFSM) for a robot that can autonomously navigate its environment while avoiding obstacles. The robot integrates multiple behaviors, such as line following, obstacle detection, and recovery, to dynamically respond to its surroundings.
🛠 Features
AFSM Logic: A flexible state-based system for managing robot behavior.
Obstacle Detection: Uses ultrasonic sensors for accurate distance measurement.
Line Following: Utilizes IR sensors to stay on predefined paths.
Random Movement: Incorporates Levy flight algorithms for exploratory motion.
Recovery Mechanism: Ensures the robot can recover from unexpected scenarios.
Modular Design: Easy to expand or modify robot behavior.


🖥 Hardware Components
Microcontroller: Raspberry Pi Pico.
Motors: Servo Motors.
Sensors:
Ultrasonic Sensors: Used for obstacle detection.
IR Sensors: Used for line-following tasks.
Power Source: Rechargeable battery or other suitable power supply.
Robot Chassis: A basic two-wheel or custom 3D-printed design.

⚙️ Software Setup
Prerequisites
Python-based microcontroller firmware (e.g., MicroPython ).
Install required libraries:
machine for PWM control.
utime for handling delays and time-based operations.

Flash the code to your microcontroller:
For Raspberry Pi Pico:
Copy Practical 1 Implementing AFSM code.py to the device.
Use a serial interface or REPL to run the program.
🧠 How It Works
This robot leverages an Autonomous Finite State Machine (AFSM) to handle different behaviors dynamically:

States
Search Mode (State 2):

Default state where the robot scans its environment for obstacles or lines.
Moves forward and switches to other states as needed.
Safe Behavior (State 6):

Activated when the robot encounters obstacles close to its sensors.
Executes pre-programmed avoidance maneuvers.
Recovery Mode (State 8):

Engaged when the robot gets stuck.
Uses small reversing and turning maneuvers to regain mobility.
Levy Flight Motion (State 7):

Implements a random motion algorithm for exploration, simulating natural search patterns.
Line Following (State 1):

Detects IR signals to follow predefined paths.
Random Behavior (State 5):

Moves randomly in different directions when no clear path or obstacle is detected.
Key Functions
IRsensor(): Reads data from IR sensors for line detection.
distancesensor(trigger, echo): Calculates distances using ultrasonic sensors.
levy_flight(): Generates random steps for exploratory motion.
power(left, right): Controls motor speed and direction using PWM.


📂 Directory Structure

object-avoidance-robot/
│
├── Practical 1 Implementing AFSM code.py   # Main codebase implementing the AFSM
├── docs/                                   # Documentation files
│   ├── setup_guide.md                      # Setup and wiring guide
│   ├── troubleshooting.md                  # Common issues and solutions
│
├── hardware/                               # Hardware-related files
│   ├── schematics/                         # Circuit diagrams
│   ├── 3d_models/                          # 3D printable parts
│
└── README.md                               # This file


🧪 Future Enhancements
Integrate Camera: Use computer vision to improve obstacle detection and pathfinding.
Add GPS: Enable outdoor navigation capabilities.
Optimize Motion: Refine algorithms for smoother transitions between states.
Remote Control: Integrate WiFi/Bluetooth for manual control and telemetry.
