# Webots Setup and SLAM Robot Integration Guide

## Introduction
This guide provides step-by-step instructions on setting up Webots, adding a SLAM-enabled robot, integrating sensors (e.g., LIDAR), and troubleshooting common issues.

---
## 1. Installing Webots
1. Download Webots from the official website: [https://cyberbotics.com/](https://cyberbotics.com/)
2. Install Webots and ensure all dependencies are installed.

---
## 2. Creating a New Simulation World
1. Open Webots.
2. Click **File → New World**.
3. Save the world as `my_world.wbt`.

---
## 3. Adding a Robot to the Scene
1. Open the **Scene Tree** (If missing, press `Ctrl + Shift + T`).
2. Right-click on `WORLD_INFO` → **Add New** → `Robot`.
3. Select a generic robot or import a custom **PROTO** robot.

### **Manually Adding a Robot**
1. Click `BaseNodes` → `Robot`.
2. Name your robot and set its properties (e.g., translation, rotation).
3. Click **Add** to insert it into the scene.

---
## 4. Adding LIDAR Sensor
1. Right-click on the robot in the **Scene Tree**.
2. Select **Add New** → `Device` → `Lidar`.
3. Configure LIDAR properties (resolution, field of view, etc.).

**If Lidar is missing:**
- Ensure **PROTO files are enabled**: `Tools → Preferences → General → Show PROTO files in Scene Tree`.

---
## 5. Importing External PROTO Files
1. Go to **File → Import → External PROTO**.
2. Select the desired `.proto` file and add it to the scene.

---
## 6. Running the Simulation
1. Click the **Play** button (`▶`) to start the simulation.
2. Use the Webots console to debug sensor data.

---
## 7. Troubleshooting
### **Missing Scene Tree**
- Press `Ctrl + Shift + T`.
- Go to `View → Restore Layout` (if available).
- Reinstall Webots if necessary.

### **Missing Lidar in Add Device**
- Enable PROTO files: `Tools → Preferences → General → Show PROTO files in Scene Tree`.
- Manually edit the `.wbt` world file to include the Lidar node.

### **Webots Not Recognizing the Robot**
- Check the **robot's PROTO file** for errors.
- Verify the **robot controller script** is correctly assigned.

---
## 8. Additional Resources
- **Webots Documentation**: [https://cyberbotics.com/doc/](https://cyberbotics.com/doc/)
- **Webots GitHub**: [https://github.com/cyberbotics/webots](https://github.com/cyberbotics/webots)
- **Webots Discord Community**: Join for live support!

---
## 9. Future Enhancements
- Implement real-time SLAM integration.
- Add ROS2 compatibility for advanced control.
- Simulate multi-robot coordination for fleet management.

---
### **Author**: Jehan B, Siddharth S, Shreeya R, SSM Keerthna 
@jehan26
@siidharth10ss
@rjspark 
@keerthnasathish
