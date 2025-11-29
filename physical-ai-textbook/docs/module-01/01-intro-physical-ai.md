---
sidebar_position: 1
---

# Introduction to Physical AI

## Learning Outcomes
By the end of this chapter, you should be able to:
- Understand the concept of Embodied Intelligence.
- Differentiate between Digital AI and Physical AI.
- Identify common types of sensors used in Physical AI systems.

## What is Physical AI?
Physical AI refers to artificial intelligence systems that interact with the real world through a physical body. Unlike purely digital AIs that operate in simulated environments or process abstract data, Physical AIs perceive, act, and learn within the complexities of the physical realm.

### Embodied Intelligence
Embodied intelligence is the idea that an intelligent agent's intelligence is deeply tied to its physical body and its interactions with the environment. For a robot, its body shape, sensor placement, and motor capabilities all influence how it can learn and perform tasks.

### Digital AI vs. Physical AI
| Feature        | Digital AI (e.g., ChatGPT)      | Physical AI (e.g., Tesla Bot)   |
|----------------|---------------------------------|---------------------------------|
| **Domain**     | Virtual, data-centric           | Physical world, real-time       |
| **Interaction**| Text, images, abstract data     | Sensors, actuators, environment |
| **Learning**   | Patterns in data, simulations   | Real-world experience, physics  |
| **Goals**      | Information processing, predictions | Physical tasks, navigation, manipulation |
| **Challenges** | Data bias, computational scale  | Safety, robustness, real-time processing, energy |

### Sensors
Sensors are the "eyes" and "ears" of a Physical AI system, providing crucial data about the environment.
- **LiDAR (Light Detection and Ranging)**: Uses pulsed laser to measure distances to the target. Creates 3D maps for navigation and object detection.
- **Depth Cameras (e.g., Intel RealSense, Azure Kinect)**: Capture depth information along with color images. Used for 3D perception, object recognition, and human-robot interaction.
- **IMUs (Inertial Measurement Units)**: Combine accelerometers, gyroscopes, and magnetometers to measure orientation, velocity, and gravitational forces. Essential for balancing and motion control.

:::danger Hardware Safety Warning
Always exercise caution when working with physical robotics hardware. Ensure proper power procedures, be aware of moving parts, and follow manufacturer safety guidelines to prevent injury or damage.
:::

## Assessments

---

### Next Section

Ready to dive deeper? Continue to [ROS 2 Fundamentals](./02-ros2-basics.md) to explore the core concepts of the Robotic Operating System.


1. Explain in your own words what Embodied Intelligence means and why it's important for Physical AI.
2. Provide an example of a task where Digital AI excels, and another where Physical AI is indispensable, explaining the reasons for each.
3. Describe how a robot might use data from a LiDAR sensor, a depth camera, and an IMU in combination to navigate a complex room.
