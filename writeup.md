# Writeup: Track 3D-Objects Over Time
- Find and display 10 examples of vehicles with varying degrees of visibility in the point-cloud
- Identify vehicle features that appear as a stable feature on most vehicles (e.g. rear-bumper, tail-lights) and describe them briefly. Also, use the range image viewer from the last example to underpin your findings using the lidar intensity channel.
## Display 10 examples of vehicles
![PCL-1](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/007c270f-4127-4ef0-b70a-9d9922cdbf38)
![PCL-2](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/fdac6584-7e0e-4a4a-afe4-6f4d5f3fe7f4)
![PCL-3](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/233431e0-b833-4c51-8c1a-fbe7b763df9b)
![PCL-4](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/72542dee-5aca-457f-add0-a4fb7eaff0bc)

## Stable Vehicle features
Upon inspection the point-cloud images above with multiple examples of different verhicles, we can see that the following features 
- Windshield/windows: this feature is visible in the point-cloud clearly as we can see they have gap in the rect shape of the car
- Mirrors: this is a distinct feature since we can see from the point-cloud image the 'ear' like shape from the rect
- Truck-bed: this is also very visible but only applies to pick-up truck
- Overal-car-shape: the most distinctive shape of a vehicle is the overall box shape and this shape can also be visible from the intensity channel.
