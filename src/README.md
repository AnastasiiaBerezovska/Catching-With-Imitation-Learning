## `src` Folder

1. **`another_test_file_running_env_robot_move.py`**
   - **Description**: Tests the environment to check if the robot's movement functions correctly. This script is used to verify basic environment interactions.

2. **`collect_human_demonstrations.py`**
   - **Description**: Collects human demonstration data to train the robot in imitation learning. Allows for collecting demonstrations to enhance model training.  
   _(Acquired from Robosuite GitHub)_

3. **`concat_hdf5.py`**
   - **Description**: Concatenates multiple HDF5 files into one.

4. **`data_conversion.py`**
   - **Description**: Handles data format conversions, created for converting raw data into an HDF5 file format needed for model training and analysis.

5. **`gym_training_tool.py`**
   - **Description**: Provides utilities for training models in a Gym environment.  
   _(Acquired from Robosuite GitHub)_

6. **`testing_gym.py`**
   - **Description**: Tests the Gym environment setup and functionality.  
   _(Acquired from Robosuite GitHub)_

7. **`updated_lift_env.py`**
   - **Description**: An updated version of the Lift environment setup, needed for lifting actions in robotic control.  
   _(Acquired from Robosuite GitHub and updated)_

8. **`visualize_trajectory.py`**
   - **Description**: Visualizes the robot's trajectory based on collected or simulated data. Created to analyze the path and behavior of the model during training or testing phases.

9. **`__init__.py`**
   - **Description**: Initializes the `src` directory as a Python module, allowing for easier imports within the project.  
   _(Acquired from Robosuite GitHub)_

10. **`make_reset_video.py`**
    - **Description**: Generates videos of the robot environment resetting, useful for debugging and visual verification of environment resets.  
    _(Acquired from Robosuite GitHub)_

11. **`manipulation_env.py`**
    - **Description**: Sets up the environment for manipulation tasks.  
    _(Acquired from Robosuite GitHub)_

12. **`robot_env.py`**
    - **Description**: Defines the main robot environment, including states, actions, and interactions.  
    _(Acquired from Robosuite GitHub)_

13. **`train_modified.py`**
    - **Description**: Modified training script that implements specific training configurations or adjustments tailored for this project.  
    _(Acquired from Robosuite GitHub and updated)_
