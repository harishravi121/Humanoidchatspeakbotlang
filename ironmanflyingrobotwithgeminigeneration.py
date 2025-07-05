WRITE A PYTHON CODE TO point 2 jets with 1KN per second thrust in choosable 360 directions 1 meter apart to fly in a curve

we must interface to head and keep generating gemini commands to fly in desired way.. no hand based direct control we can add a bit of joystick effect with more discussion

import time
import math
import random # Used for placeholder IK angles

# --- CONFIGURATION PARAMETERS ---
# These values would need to be precisely tuned for the Rassom robot's physical characteristics
# and desired walking gait.

SERVO_IDS = list(range(1, 51)) # Assuming 50 servo motors with IDs from 1 to 50
HOME_POSE_ANGLES = {id: 0 for id in SERVO_IDS} # Example: all servos at 0 degrees for a neutral stance.
                                            # In reality, this would be a specific set of angles for a stable standing pose.

STEP_LENGTH_X = 0.15    # meters (approximate forward/backward movement per step)
STEP_LENGTH_Y = 0.10    # meters (approximate sideways movement per step)
STEP_HEIGHT = 0.05      # meters (how high the swinging foot lifts off the ground)
STEP_DURATION = 1.0     # seconds (duration of a single complete step cycle, including swing and support phases)
TRAJECTORY_POINTS_PER_STEP = 100 # Number of intermediate points for smooth foot trajectory within one step.

TARGET_NORTH_M = 5.0    # Desired distance to walk North (forward)
TARGET_EAST_M = 10.0    # Desired distance to walk East (sideways)

# --- NEW: JET CONFIGURATION PARAMETERS ---
JET_THRUST_MAX_KN = 1.0 # Max thrust per jet in KiloNewtons (1000 Newtons)
JET_DISTANCE_APART_M = 1.0 # Distance between the two jets (e.g., along the robot's width)
FLY_SIMULATION_STEPS_PER_SECOND = 50 # How many times per second to update flight simulation

# --- GLOBAL ROBOT OBJECTS (Conceptual Placeholders) ---
# In a real application, these would be instances of classes from the Rassom Robot SDK
# that manage connection, kinematics, and direct servo control.
robot_controller = None # Represents the connection to the robot's hardware
robot_kinematic_model = None # Represents the robot's mathematical kinematic model

# --- HELPER FUNCTIONS (Conceptual Implementations) ---

def initialize_robot():
    """
    Conceptual function to initialize connection to the robot and set it to a home pose.
    In a real scenario, this would involve:
    1. Establishing communication with the robot's control board.
    2. Loading robot configuration (e.g., servo limits, offsets).
    3. Sending commands to move all 50 servos to a predefined, stable home position.
    4. Calibrating any sensors (IMU, force sensors).
    """
    print("Initializing robot connection and setting home pose...")
    # global robot_controller, robot_kinematic_model
    # try:
    #     robot_controller = rassom_robot_api.connect() # Placeholder for actual API call
    #     robot_kinematic_model = rassom_robot_api.load_kinematic_model() # Placeholder for actual API call
    #     send_servo_commands(HOME_POSE_ANGLES)
    #     time.sleep(2) # Give robot time to reach initial pose
    #     print("Robot initialized successfully.")
    # except Exception as e:
    #     print(f"Error initializing robot: {e}")
    #     # Handle error, e.g., exit program or retry
    print("Robot initialization (conceptual) complete.")


def calculate_inverse_kinematics(target_foot_position, support_leg_side, current_robot_state):
    """
    Conceptual function to calculate joint angles for all 50 servos using Inverse Kinematics (IK).
    This is the most complex and critical part of humanoid walking.
    It needs to consider:
    1. The desired 3D position (x, y, z) and orientation (roll, pitch, yaw) for the swinging foot.
    2. The current state of the robot (e.g., torso orientation, CoM position).
    3. Maintaining balance by adjusting the support leg and other joints (torso, arms).
    4. Avoiding joint limits and self-collisions.

    Args:
        target_foot_position (tuple): (x, y, z) coordinates for the swing foot in the robot's coordinate frame.
        support_leg_side (str): 'left' or 'right', indicating which leg is currently supporting the robot.
        current_robot_state (dict): A dictionary representing the robot's current estimated state (e.g., CoM, orientation).

    Returns:
        dict: A dictionary of {servo_id: angle_in_degrees} for all 50 servos.
              Returns None if IK solution is not found or invalid.
    """
    print(f"  Calculating Inverse Kinematics for swing foot at {target_foot_position} "
          f"with {support_leg_side} leg as support...")

    # --- PLACEHOLDER FOR ACTUAL INVERSE KINEMATICS SOLVER ---
    # In a real system, this would involve:
    # - Using a sophisticated IK library (e.g., PyKDL, custom solver).
    # - Considering the robot's full kinematic chain.
    # - Incorporating balance control algorithms (e.g., ZMP, CoM projection).
    # - Iteratively solving for joint angles until the target is met and balance is maintained.

    # For demonstration, return random angles within a plausible range.
    # This is NOT how a real IK solver works!
    try:
        # Simulate some computation time
        time.sleep(0.001)
        # Generate random angles for all 50 servos
        # Angles typically range from -180 to 180 or -90 to 90 depending on servo type
        angles = {id: random.uniform(-90, 90) for id in SERVO_IDS}
        return angles
    except Exception as e:
        print(f"  IK calculation error: {e}")
        return None


def send_servo_commands(angles_dict):
    """
    Conceptual function to send calculated joint angles to the robot's servo motors.
    This would use the Rassom Robot API to communicate with the hardware.

    Args:
        angles_dict (dict): A dictionary of {servo_id: angle_in_degrees}.
    """
    # print(f"  Sending servo commands (conceptual): {angles_dict}")
    # In a real system:
    # try:
    #     robot_controller.set_servo_angles(angles_dict) # Placeholder for actual API call
    # except Exception as e:
    #     print(f"  Error sending servo commands: {e}")
    #     # Handle communication errors
    pass # No actual hardware interaction in this conceptual code


def generate_foot_trajectory(start_pos, end_pos, height, num_points):
    """
    Generates a smooth 3D trajectory for the swinging foot.
    This creates a simple parabolic arc for the foot lift.

    Args:
        start_pos (tuple): (x, y, z) start coordinates of the foot.
        end_pos (tuple): (x, y, z) end coordinates of the foot.
        height (float): Maximum height the foot should lift during the step.
        num_points (int): Number of discrete points to generate along the trajectory.

    Returns:
        list: A list of (x, y, z) tuples representing the trajectory points.
    """
    trajectory = []
    for i in range(num_points):
        t = i / (num_points - 1) # Normalized time from 0 to 1
        # Linear interpolation for X and Y coordinates
        x = start_pos[0] + t * (end_pos[0] - start_pos[0])
        y = start_pos[1] + t * (end_pos[1] - start_pos[1])
        # Parabolic lift for Z coordinate (foot lift)
        z = start_pos[2] + height * (1 - (2*t - 1)**2) # Parabola peaking at t=0.5
        trajectory.append((x, y, z))
    return trajectory


def walk_step(current_robot_pos, target_delta_x, target_delta_y, swing_leg_side):
    """
    Performs a single walking step for the robot. This involves:
    1. Defining the swing foot's start and end positions.
    2. Generating a smooth trajectory for the swing foot.
    3. Iteratively calculating IK and sending servo commands for each point in the trajectory.
    4. Updating the robot's conceptual position.

    Args:
        current_robot_pos (tuple): (x, y, z) of the robot's base/center of mass (conceptual).
        target_delta_x (float): Desired forward/backward movement for this step.
        target_delta_y (float): Desired left/right movement for this step.
        swing_leg_side (str): 'left' or 'right', indicating which leg will swing.

    Returns:
        tuple: The new conceptual (x, y, z) position of the robot after the step.
    """
    print(f"\nPerforming {swing_leg_side} swing step: dx={target_delta_x:.2f}m, dy={target_delta_y:.2f}m")

    # Determine the support leg
    support_leg_side = 'right' if swing_leg_side == 'left' else 'left'

    # Define the start and end positions for the swing foot relative to the robot's base.
    # These would be more sophisticated calculations in a real robot,
    # involving the robot's current pose and gait parameters.
    swing_foot_start_pos = (0, 0, 0) # Relative to robot's current base/CoM
    swing_foot_end_pos = (target_delta_x, target_delta_y, 0) # Relative to robot's current base/CoM

    # Generate the trajectory for the swinging foot
    foot_trajectory = generate_foot_trajectory(
        swing_foot_start_pos, swing_foot_end_pos, STEP_HEIGHT, TRAJECTORY_POINTS_PER_STEP
    )

    # Time delay between each trajectory point
    time_per_point = STEP_DURATION / TRAJECTORY_POINTS_PER_STEP

    # Iterate through the trajectory points and command the servos
    for i, point in enumerate(foot_trajectory):
        # In a real robot, `current_robot_state` would be read from sensors (IMU, encoders)
        # and updated dynamically. Here, it's a placeholder.
        current_robot_state = {"CoM": current_robot_pos, "orientation": (0, 0, 0)} # Conceptual state

        # Calculate the required joint angles for all 50 servos
        joint_angles = calculate_inverse_kinematics(point, support_leg_side, current_robot_state)

        if joint_angles: # If IK calculation was successful
            send_servo_commands(joint_angles)
        else:
            print(f"  Warning: IK failed for trajectory point {i}. Robot might lose balance.")
            # Implement error recovery or emergency stop here

        time.sleep(time_per_point) # Pause for smooth motion

    # Update the robot's conceptual position after the step is completed
    new_robot_pos = (
        current_robot_pos[0] + target_delta_x,
        current_robot_pos[1] + target_delta_y,
        current_robot_pos[2]
    )
    print(f"  Step complete. Conceptual robot position: ({new_robot_pos[0]:.2f}m North, {new_robot_pos[1]:.2f}m East)")
    return new_robot_pos


# --- NEW: JET CONTROL FUNCTIONS ---

def control_jets(jet1_thrust_kn, jet1_angle_degrees, jet2_thrust_kn, jet2_angle_degrees):
    """
    Conceptual function to send thrust and angle commands to two jets.
    In a real robot, this would translate to controlling actuators
    (e.g., servos for nozzle vectoring, motor controllers for thrust).

    Args:
        jet1_thrust_kn (float): Thrust for Jet 1 in KiloNewtons (0 to JET_THRUST_MAX_KN).
        jet1_angle_degrees (float): Angle for Jet 1 relative to robot's forward direction (0-360 degrees).
        jet2_thrust_kn (float): Thrust for Jet 2 in KiloNewtons (0 to JET_THRUST_MAX_KN).
        jet2_angle_degrees (float): Angle for Jet 2 relative to robot's forward direction (0-360 degrees).
    """
    # Ensure thrust values are within limits
    jet1_thrust_kn = max(0, min(jet1_thrust_kn, JET_THRUST_MAX_KN))
    jet2_thrust_kn = max(0, min(jet2_thrust_kn, JET_THRUST_MAX_KN))

    # Normalize angles to 0-360
    jet1_angle_degrees = jet1_angle_degrees % 360
    jet2_angle_degrees = jet2_angle_degrees % 360

    print(f"  Jet 1: Thrust={jet1_thrust_kn:.2f}KN, Angle={jet1_angle_degrees:.1f}° | "
          f"Jet 2: Thrust={jet2_thrust_kn:.2f}KN, Angle={jet2_angle_degrees:.1f}°")

    # In a real system, these commands would be sent to the jet's control hardware.
    # This might involve mapping angles to specific servo positions for nozzle vectoring.
    pass # No actual hardware interaction in this conceptual code


def fly_in_curve(current_robot_pos, current_robot_orientation_degrees,
                 curve_radius_m, total_angle_degrees, flight_duration_s):
    """
    Conceptual function to make the robot fly in a curve using two jets.
    This simplifies complex flight dynamics. It assumes the jets can provide
    the necessary forward and turning forces.

    Args:
        current_robot_pos (tuple): (x, y, z) of the robot's base/center of mass.
        current_robot_orientation_degrees (float): Current heading of the robot in degrees (0-360, North=0).
        curve_radius_m (float): Radius of the desired curve in meters.
        total_angle_degrees (float): Total angle to turn along the curve in degrees.
        flight_duration_s (float): Total duration of the flight in seconds.

    Returns:
        tuple: (new_pos, new_orientation_degrees) after the flight.
    """
    print(f"\n--- Flying in a curve: Radius={curve_radius_m:.2f}m, "
          f"Total Angle={total_angle_degrees:.1f}°, Duration={flight_duration_s:.1f}s ---")

    if flight_duration_s <= 0:
        print("  Flight duration must be positive.")
        return current_robot_pos, current_robot_orientation_degrees

    num_simulation_steps = int(flight_duration_s * FLY_SIMULATION_STEPS_PER_SECOND)
    if num_simulation_steps == 0:
        num_simulation_steps = 1 # Ensure at least one step

    time_per_step = flight_duration_s / num_simulation_steps
    angular_speed_rad_per_s = math.radians(total_angle_degrees) / flight_duration_s
    tangential_speed_mps = curve_radius_m * angular_speed_rad_per_s # Speed required to maintain curve

    # Calculate required forward thrust (simplified: proportional to desired speed)
    # This would be highly dependent on robot mass, drag, etc.
    # Here, we just ensure it's within max thrust.
    # Let's assume a base forward thrust for movement
    base_forward_thrust_kn = min(JET_THRUST_MAX_KN * 0.5, 0.5) # Example: 50% of max thrust for forward motion

    # Calculate differential thrust/angle for turning.
    # For a curve, one jet will push slightly more or at a slightly different angle
    # to create a net turning force/torque.
    # Simplification: A constant small angle difference between jets for turning.
    # A positive `total_angle_degrees` implies turning counter-clockwise (left turn).
    # A negative `total_angle_degrees` implies turning clockwise (right turn).
    
    # The magnitude of this differential angle would depend on curve_radius and speed.
    # For simplicity, let's use a fixed small differential angle for turning.
    # In a real system, this would be derived from control laws.
    
    differential_angle_base = 10.0 # degrees, max differential angle
    turn_factor = total_angle_degrees / (abs(total_angle_degrees) + 0.001) if total_angle_degrees != 0 else 0
    
    # Jet1 (left) and Jet2 (right) are assumed to be symmetric.
    # For a right turn (total_angle_degrees < 0, turn_factor = -1):
    #   Jet1 (left) angles more positive (e.g., +5 deg from forward)
    #   Jet2 (right) angles more negative (e.g., -5 deg from forward)
    # For a left turn (total_angle_degrees > 0, turn_factor = +1):
    #   Jet1 (left) angles more negative (e.g., -5 deg from forward)
    #   Jet2 (right) angles more positive (e.g., +5 deg from forward)
    jet1_angle_offset = -differential_angle_base * turn_factor / 2
    jet2_angle_offset = differential_angle_base * turn_factor / 2

    current_pos_x, current_pos_y, current_pos_z = current_robot_pos
    current_orientation_rad = math.radians(current_robot_orientation_degrees)

    for i in range(num_simulation_steps):
        # Calculate current target orientation for this step
        step_angle_degrees = total_angle_degrees / num_simulation_steps
        
        # Apply thrusts and angles (conceptual)
        # Both jets provide base_forward_thrust_kn.
        # Angles are relative to the robot's current forward direction.
        jet1_command_angle = jet1_angle_offset
        jet2_command_angle = jet2_angle_offset
        
        control_jets(base_forward_thrust_kn, jet1_command_angle,
                     base_forward_thrust_kn, jet2_command_angle)

        # Update conceptual robot position and orientation based on simplified physics
        # Assuming constant speed along the arc for simulation
        distance_moved_this_step = tangential_speed_mps * time_per_step
        angle_turned_this_step_rad = angular_speed_rad_per_s * time_per_step

        # Update position based on current orientation and distance moved
        # Movement is along the current heading
        current_pos_x += distance_moved_this_step * math.cos(current_orientation_rad + angle_turned_this_step_rad / 2)
        current_pos_y += distance_moved_this_step * math.sin(current_orientation_rad + angle_turned_this_step_rad / 2)
        # Z position (height) could be controlled by net vertical thrust, keeping it constant for now
        # current_pos_z remains constant for horizontal flight

        current_orientation_rad += angle_turned_this_step_rad
        current_robot_orientation_degrees = math.degrees(current_orientation_rad) % 360

        print(f"  Sim Step {i+1}/{num_simulation_steps}: Pos=({current_pos_x:.2f}N, {current_pos_y:.2f}E), "
              f"Orient={current_robot_orientation_degrees:.1f}°")
        time.sleep(time_per_step)

    new_robot_pos = (current_pos_x, current_pos_y, current_pos_z)
    new_robot_orientation_degrees = current_robot_orientation_degrees

    print(f"  Flight complete. Final conceptual position: ({new_robot_pos[0]:.2f}N, {new_robot_pos[1]:.2f}E), "
          f"Orientation: {new_robot_orientation_degrees:.1f}°")
    return new_robot_pos, new_robot_orientation_degrees


# --- MAIN PROGRAM EXECUTION ---

def main():
    print("--- Starting Rassom Robot Simulation (Conceptual) ---")

    # 1. Initialize the robot (conceptual)
    initialize_robot()

    # Initialize robot's conceptual position and movement tracking
    current_robot_pos = (0.0, 0.0, 0.0) # (North_coord, East_coord, Height_coord)
    current_robot_orientation_degrees = 90.0 # Start facing East (90 degrees from North)
    total_distance_north = 0.0
    total_distance_east = 0.0
    step_count = 0
    current_swing_leg = 'left' # Start with the left leg swinging first

    print(f"\nTarget path: {TARGET_NORTH_M}m North, {TARGET_EAST_M}m East (Walking).")

    # 2. Walk North
    print("\n--- Walking North ---")
    while total_distance_north < TARGET_NORTH_M:
        # Calculate the remaining distance to walk North
        dx = min(STEP_LENGTH_X, TARGET_NORTH_M - total_distance_north)
        # Perform a forward step (dx, 0 for dy)
        current_robot_pos = walk_step(current_robot_pos, dx, 0, current_swing_leg)
        total_distance_north += dx
        # Alternate the swinging leg for the next step
        current_swing_leg = 'right' if current_swing_leg == 'left' else 'left'
        step_count += 1
        print(f"  Current North distance: {total_distance_north:.2f}m / {TARGET_NORTH_M:.2f}m")

    # 3. Conceptual Turn to East
    print("\n--- Robot conceptually turns East (actual turning gait not implemented) ---")
    # For walking, a real robot would execute a series of small turning steps or a pivot.
    # For simplicity in this simulation, we just update the orientation conceptually.
    current_robot_orientation_degrees = 90.0 # Now facing East
    print(f"  Robot orientation updated to {current_robot_orientation_degrees:.1f}° (East).")


    # 4. Walk East
    print("\n--- Walking East ---")
    while total_distance_east < TARGET_EAST_M:
        # Calculate the remaining distance to walk East
        dy = min(STEP_LENGTH_Y, TARGET_EAST_M - total_distance_east)
        # Perform a lateral step (0 for dx, dy for sideways movement).
        # Note: The walk_step function assumes movement relative to robot's forward.
        # If robot is facing East, dx would be East-West movement, dy would be North-South.
        # To simplify, we'll keep dx as 'forward' and dy as 'sideways' relative to the *initial* North/East frame.
        # A more robust walking system would account for robot's current heading.
        # For this conceptual walk, we'll assume it handles North/East directly.
        current_robot_pos = walk_step(current_robot_pos, 0, dy, current_swing_leg)
        total_distance_east += dy
        # Alternate the swinging leg for the next step
        current_swing_leg = 'right' if current_swing_leg == 'left' else 'left'
        step_count += 1
        print(f"  Current East distance: {total_distance_east:.2f}m / {TARGET_EAST_M:.2f}m")


    print(f"\n--- Walking complete! ---")
    print(f"Total steps taken: {step_count}")
    print(f"Final conceptual robot position after walking: "
          f"({current_robot_pos[0]:.2f}m North, {current_robot_pos[1]:.2f}m East), "
          f"Orientation: {current_robot_orientation_degrees:.1f}°")

    # --- NEW: Demonstrate Flying in a Curve ---
    print("\n--- Demonstrating Flying in a Curve ---")
    # Let's assume the robot is now at the end of its walk, and we want it to fly from there.
    # It will fly in a curve (e.g., a right turn) for a certain angle and duration.
    
    # Example 1: Fly in a right turn (clockwise)
    fly_curve_radius = 5.0 # meters
    fly_total_angle = -90.0 # degrees (negative for right turn)
    fly_duration = 5.0 # seconds
    
    current_robot_pos, current_robot_orientation_degrees = fly_in_curve(
        current_robot_pos, current_robot_orientation_degrees,
        fly_curve_radius, fly_total_angle, fly_duration
    )

    print(f"\n--- Flight demonstration complete! ---")
    print(f"Final conceptual robot position after flight: "
          f"({current_robot_pos[0]:.2f}m North, {current_robot_pos[1]:.2f}m East), "
          f"Orientation: {current_robot_orientation_degrees:.1f}°")

    # 5. Terminate: Bring robot to a stable standing pose (conceptual)
    print("Robot returning to stable standing pose.")
    # send_servo_commands(HOME_POSE_ANGLES) # Send home pose commands
    # time.sleep(1) # Allow time to settle
    print("Program finished.")


if __name__ == "__main__":
    main()

