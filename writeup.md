# Writeup: Track 3D-Objects Over Time

## Compute Lidar Point-Cloud from Range Image
![range_image_screenshot_23 05 2023](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/e82dfc2d-be5d-4914-b6df-d239db55f8b7)

### Display 10 examples of vehicles
- Find and display 10 examples of vehicles with varying degrees of visibility in the point-cloud
- Identify vehicle features that appear as a stable feature on most vehicles (e.g. rear-bumper, tail-lights) and describe them briefly. Also, use the range image viewer from the last example to underpin your findings using the lidar intensity channel.
![PCL-1](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/007c270f-4127-4ef0-b70a-9d9922cdbf38)
![PCL-2](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/fdac6584-7e0e-4a4a-afe4-6f4d5f3fe7f4)
![PCL-3](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/233431e0-b833-4c51-8c1a-fbe7b763df9b)
![PCL-4](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/72542dee-5aca-457f-add0-a4fb7eaff0bc)
<img width="600" alt="PCL-5" src="https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/f4db178a-0941-4016-ac94-3b2cb9699830">
<img width="600" alt="PCL-6" src="https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/06e028cd-7ec7-4635-9ab3-8f55d0589e54">
<img width="595" alt="PCL-7" src="https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/c12f1b1c-7645-445f-8935-2818b946f01b">
<img width="593" alt="PCL-8" src="https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/1c14236e-1b9e-48bf-a319-b8ba7878d352">
<img width="595" alt="PCL-9" src="https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/cd799b8d-0064-4599-a945-1bf26bb09905">
<img width="585" alt="PCL-10" src="https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/a92b0d00-886c-4c58-8279-0a2635b4b358">

### Stable Vehicle features
Upon inspection the point-cloud images above with multiple examples of different verhicles, we can see that the following features 
- Windshield/windows: this feature is visible in the point-cloud clearly as we can see they have gap in the rect shape of the car
- Mirrors: this is a distinct feature since we can see from the point-cloud image the 'ear' like shape from the rect
- Truck-bed: this is also very visible but only applies to pick-up truck
- Overal-car-shape: the most distinctive shape of a vehicle is the overall box shape and this shape can also be visible from the intensity channel.

## Create Birds-Eye View from Lidar PCL

![intensity-height](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/95794ec8-7f55-4dbe-b47c-68d478a4911f)
![intensity-height-zoomed-in](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/f7943c82-c24a-4e00-9d72-ac80b82ea61a)

## Model-based Object Detection in BEV Image

![bbox](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/5ffec4b2-b7c3-4899-920d-3d22f863dfba)

## Performance Evaluation for Object Detection

![evaluation](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/cd1098a7-4dce-4b9f-b473-5f50a7e7ea6b)
![Eval-true](https://github.com/ghost-qb/SDE-project2-sensor-fusion/assets/58492405/6f916d8b-ae69-41d2-ba44-88c36779c640)
