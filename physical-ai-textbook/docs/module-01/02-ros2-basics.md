---
sidebar_position: 2
---

### Previous Section

Before diving into ROS 2, make sure you've covered the [Introduction to Physical AI](./01-intro-physical-ai.md) to understand the foundational concepts.

# ROS 2 Fundamentals

## Learning Outcomes
By the end of this chapter, you should be able to:
- Understand the core concepts of ROS 2 (Nodes, Topics, Services).
- Explain the "Nervous System" analogy for ROS 2.
- Write basic ROS 2 Python (`rclpy`) Publisher and Subscriber nodes.
- Describe a robot's physical structure using URDF.
- Interpret Mermaid.js diagrams for ROS 2 node visualization.

## The Robotic Nervous System: An Analogy for ROS 2
Imagine a human body: a complex system of organs, muscles, and nerves. Each part has a specific function, but they all communicate and coordinate to achieve overall goals like walking, talking, or eating. ROS 2 (Robot Operating System 2) provides a similar framework for robots.

Just as your brain sends signals to your legs to walk, a robot's navigation system sends commands to its motor controllers. Just as your eyes provide sensory input, a robot's cameras and LiDARs feed data into its perception modules. ROS 2 acts as the "nervous system" that enables these disparate components to communicate seamlessly and work together.

## ROS 2 Core Concepts

### Nodes
In ROS 2, a **Node** is an executable process that performs computation. Think of nodes as the "organs" or "functional units" of your robot. Each node should be responsible for a single, modular purpose (e.g., a camera driver node, a navigation node, a motor control node).

### Topics
**Topics** are the main mechanism for nodes to exchange data in a publish-subscribe messaging pattern. If nodes are organs, topics are the "blood vessels" carrying information. One node can **publish** data to a topic, and other nodes can **subscribe** to that topic to receive the data. This is a one-to-many communication model, ideal for streaming sensor data or continuous commands.

### Services
**Services** provide a request-response communication pattern between nodes. Unlike topics, which are asynchronous and one-way, services are synchronous and bidirectional. They are like a "doctor's appointment" – you make a request, and you expect a specific response back. This is useful for tasks that require a clear result, such as asking a robot to perform a specific action and confirm its completion.

## Python (`rclpy`) Code Snippets

Here are basic examples of a ROS 2 Python publisher and subscriber using `rclpy`.

**1. Simple Publisher (`minimal_publisher.py`)**

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello ROS 2: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

**2. Simple Subscriber (`minimal_subscriber.py`)**

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## URDF: Describing a Robot's Body

**URDF (Unified Robot Description Format)** is an XML format used in ROS to describe all aspects of a robot. This includes its visual appearance, collision properties, inertial properties, and how its various links (rigid bodies) are connected by joints. URDF allows ROS 2 to understand the robot's kinematics and dynamics.

**Example URDF Snippet:**

```xml
<?xml version="1.0"?>
<robot name="my_simple_robot">

  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.6 0.4 0.2" />
      </geometry>
    </visual>
  </link>

  <joint name="base_to_wheel_right" type="continuous">
    <parent link="base_link"/>
    <child link="wheel_right_link"/>
    <origin xyz="-0.2 0.2 0" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
  </joint>

  <link name="wheel_right_link">
    <visual>
      <geometry>
        <cylinder radius="0.1" length="0.05"/>
      </geometry>
    </visual>
  </link>

  <!-- ... other links and joints ... -->

</robot>
```

## Visualizing ROS 2 Node Connections with Mermaid.js

Mermaid.js can be used to create diagrams directly from text in Markdown. This is incredibly useful for visualizing the relationships between ROS 2 nodes and topics.

```mermaid
graph TD
    A[LiDAR Node] -->|/scan topic| B(Mapping Node)
    B -->|/map topic| C{Navigation Node}
    D[Motor Control Node] <--|/cmd_vel topic| C
    E[Camera Node] -->|/image_raw topic| F(Object Detection Node)
    F -->|/detected_objects topic| C
```

:::warning Hardware Safety Warning
When experimenting with ROS 2 and physical robots, always ensure you have an emergency stop mechanism. Be mindful of the robot's movements, especially during development, to prevent unexpected behavior or accidents. Test code in simulation first whenever possible.
:::

## Assessments
1. Describe the difference between ROS 2 Topics and Services, and provide a real-world robotics scenario where each would be most appropriate.
2. Explain why modularity (using separate nodes for different functionalities) is a core principle in ROS 2 development.
3. Using the provided URDF snippet, identify the parent and child links for the `base_to_wheel_right` joint.
4. Draw a simple Mermaid.js graph illustrating a robot with two nodes: one publishing IMU data to a topic, and another subscribing to that topic to estimate the robot's pose.
