import robosuite as suite
import numpy as np

# Create environment
env = suite.make(
        env_name="Lift",       # Choose environment (e.g., Lift or custom)
        has_renderer=False,    # No visualization needed here
        use_camera_obs=False,  # Disable camera observations

)

# Reset environment
obs = env.reset()

# Apply force or control to the cube (assuming cube is a movable object in your setup)
action = np.array([0.0, 0.0, 1.0])  # Example force vector in Cartesian coordinates
for i in range(100):
        obs, reward, done, info = env.step(action)  # Simulate the cube dynamics
            cube_position = env.sim.data.body_xpos[env.sim.model.body_name2id("cube_body_name")]

                print(f"Step {i}: Cube position: {cube_position}")

