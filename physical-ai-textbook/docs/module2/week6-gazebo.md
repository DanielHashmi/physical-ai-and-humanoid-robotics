---
sidebar_position: 1
---

# Robot Simulation with Gazebo

## Learning Outcomes
By the end of this chapter, you should be able to:
- Set up and configure the Gazebo simulation environment
- Understand URDF and SDF robot description formats
- Simulate physics, gravity, and collisions
- Create custom simulation worlds

## Introduction to Gazebo

Gazebo is a powerful 3D robotics simulator that provides accurate physics simulation, sensor simulation, and a rich set of tools for robot development. It's widely used in the robotics community for testing algorithms before deploying them on real hardware.

### Why Simulation Matters

:::tip Cost-Effective Development
Simulation allows you to test dangerous or expensive scenarios without risking real hardware. You can crash your robot thousands of times in simulation without any real-world consequences!
:::

### Key Features of Gazebo

1. **Physics Engine**: Supports multiple physics engines (ODE, Bullet, Simbody, DART)
2. **Sensor Simulation**: Cameras, LiDAR, IMU, GPS, and more
3. **ROS 2 Integration**: Seamless integration with ROS 2 through `ros_gz` packages
4. **Plugin System**: Extensible architecture for custom functionality

## Setting Up Gazebo

### Installation (Ubuntu 22.04)

```bash
# Install Gazebo Harmonic (recommended for ROS 2 Humble)
sudo apt-get update
sudo apt-get install ros-humble-ros-gz

# Verify installation
gz sim --version
```

### Your First Simulation

```bash
# Launch an empty world
gz sim empty.sdf

# Launch with a robot
gz sim -r robot_world.sdf
```

## URDF vs SDF

| Feature | URDF | SDF |
|---------|------|-----|
| **Purpose** | Robot description | World + Robot description |
| **Physics** | Basic | Advanced |
| **Sensors** | Limited | Comprehensive |
| **Use Case** | ROS robot models | Gazebo simulations |

### Converting URDF to SDF

```bash
# Convert URDF to SDF
gz sdf -p robot.urdf > robot.sdf
```

## Physics Simulation

Gazebo simulates real-world physics including:

- **Gravity**: Objects fall realistically
- **Collisions**: Accurate collision detection and response
- **Friction**: Surface interactions
- **Inertia**: Mass distribution effects

```xml
<!-- Example physics configuration in SDF -->
<physics type="ode">
  <max_step_size>0.001</max_step_size>
  <real_time_factor>1.0</real_time_factor>
  <gravity>0 0 -9.81</gravity>
</physics>
```

:::warning Performance Tip
Lower `max_step_size` values increase accuracy but reduce simulation speed. Find the right balance for your application.
:::

## Assessments

1. Explain the difference between URDF and SDF formats. When would you use each?
2. What are the advantages of testing robot algorithms in simulation before real-world deployment?
3. Describe how you would set up a Gazebo world with custom gravity (e.g., simulating Mars gravity).
4. List three types of sensors that can be simulated in Gazebo and their typical use cases.
