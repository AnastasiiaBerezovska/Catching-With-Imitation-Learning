## src Folder Descriptions

1. **AnotherTestFileforRunningIfHasEnvForRobotMove.py**  
   *Description:* Tests the environment to check if the robot's movement functions correctly. This script is used to verify basic environment interactions.

2. **Collect_Human_Demonstrations.py**  
   *Description:* Collects human demonstration data to train the robot in imitation learning. Allows for collecting demonstrations to enhance model training.  
   *(Acquired from Robosuite GitHub)*

3. **Concat_hdf5.py**  
   *Description:* Concatenates multiple HDF5 files into one.

4. **DataConversion.py**  
   *Description:* Handles data format conversions, created for converting raw data into an HDF5 file format needed for model training and analysis.

5. **GymTrainingTool.py**  
   *Description:* Provides utilities for training models in a Gym environment.  
   *(Acquired from Robosuite GitHub)*

6. **TestingGym.py**  
   *Description:* Tests the Gym environment setup and functionality.  
   *(Acquired from Robosuite GitHub)*

7. **Updated_Lift_Env.py**  
   *Description:* An updated version of the Lift environment setup, needed for lifting actions in robotic control.  
   *(Acquired from Robosuite GitHub and updated)*

8. **Visualize_Trajectory.py**  
   *Description:* Visualizes the robot's trajectory based on collected or simulated data. Created to analyze the path and behavior of the model during training or testing phases.

9. **\_\_init\_\_.py**  
   *Description:* Initializes the `src` directory as a Python module, allowing for easier imports within the project.  
   *(Acquired from Robosuite GitHub)*

10. **make_reset_video.py**  
    *Description:* Generates videos of the robot environment resetting, useful for debugging and visual verification of environment resets.  
    *(Acquired from Robosuite GitHub)*

11. **manipulation_env.py**  
    *Description:* Sets up the environment for manipulation tasks.  
    *(Acquired from Robosuite GitHub)*

12. **robot_env.py**  
    *Description:* Defines the main robot environment, including states, actions, and interactions.  
    *(Acquired from Robosuite GitHub)*

13. **trainModified.py**  
    *Description:* Modified training script that implements specific training configurations or adjustments tailored for this project.  
    *(Acquired from Robosuite GitHub and updated)*
