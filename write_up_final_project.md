# Track objects over time with a Kalman Filter
- EKF helps to track object accurately for each iteration of time steps
- EKF works by performing prediction and update steps for each of the time step iteration
![Screen Shot 2023-05-24 at 7 54 55 PM](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/bcc754ef-9972-4425-ac92-29d41b7e497a)

# Track Management
- Track management is a strategy engineers use to manage the tracked objects
- Using the pre-defined of experimental thresholds will help improving the system and accurately track the desired object, delete old tracks, and updating the state of each tracks thru time.
![Track Management](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/a74e3e46-dcb0-411b-9cf1-5814de7f048d)

# Association
- For multi-tracking, association strategy will help engineers to handle multiple objects in the field of view.
- Association will help identify the which measurement associates with which object by using the Mahalanobis distance.
![Association](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/09b66ec9-2cfe-40f9-8540-5ccc9f892e48)

# Sensor Fusion
- Sensor fusion enhance the capability of the tracking system by combining multiple sensors (Lidar and Camera in this case)
![Sensor Fusion](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/57985f53-c7c0-481a-9a49-3e6a9d03bbbe)

- Tracking movie (frame by frame) can be found in the tracking_movie folder


# Camera + Lidar benefits
- In theory, sensor fusion with multiple source of measurements (camera + lidar) would generate better tracking resutls since we have more data
- In practice, from the RMSE graph shown for lidar-only and lidar+camera tracking, the RMSE is observed to be slightly better but not significantly. 

# Challenges will a sensor fusion system face in real-life scenarios
- The system faces challenge when there is an object suddenly appear and disappear, since the EKF and the track management would take a couple of time iteration (i.e. frame) to improve the track score or changing the track state. 

# Ways to improve your tracking results in the future
- Perhaps, we can have a strategy to fine-tune the thresholds for track deletion, changing states, etc.
- Also, experiment with other system configurations like camera + lidar + radar or different kind of cameras. 
