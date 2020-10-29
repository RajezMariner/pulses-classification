# Pulses Classification
 
<p align="center">

  [![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

  [![GitHub contributors](https://img.shields.io/github/contributors/rstak/pulses-classification)](https://github.com/RsTaK/pulses-classification/graphs/contributors/)
  [![GitHub license](https://img.shields.io/github/license/rstak/pulses-classification)](https://github.com/RsTaK/pulses-classification/blob/master/LICENSE)
</p>  

<img src="static/img/background.jpg"/>


# About
Leveraging the power of Deep-learning, deployed a Flask based Web application successfully capable of identifying the type of pulse with 98% accuracy on validation dataset.

Currently supports 14 commonly used Pulses in Indian households, namely :
* Adzuki Beans
* Black Gram
* Chickpeas
* Dew Bean
* Green Chickpeas
* Green Gram
* Pinto Beans
* Red Kidney Beans
* Red Lentils
* Split & Skinned Black Gram
* Split Black Gram
* Split Green Gram
* White Kidney Beans
* Yellow Lentils

Refer to [pulse_list.txt](req_files/pulses_list.txt) to get Hindi/Regional Conversion of given Pulses names

To use this app, [Click here](https://pulses-classification.herokuapp.com/) 

<center>or</center> 

Visit : https://pulses-classification.herokuapp.com/

# Demo Video

<video width="320" height="240" controls>
  <source src=req_files/Demo(mobile).mp4 type="video/mp4">
</video>

# Inspiration
Thanks to all of my friends and the comedy skits uploaded on youtube that decribes how difficult it is for them to recogninze the type of pulse there in front of them (I'm one of them too).  

So, one day I came up with the idea why don't I develop something that will solve this issue. I guess no one would like to call their family every minute just to know difference between Urad Dal and Urad Dal chilka.

# Data Collection
1. Used [bing_image_downloader](https://pypi.org/project/bing-image-downloader/) package to download 1000 images of each pulse in my list.
2. After downloading, manually cleaned the dataset, removing unwanted or wrong images.

Dataset composition after manually cleaning :

| Pulse Name      | Image Count |
| ----------- | ----------- |
| Pinto Beans      | 765       |
| Yellow Lentils    | 664        |
| Adzuki Beans      | 632       |
| Chickpeas   | 622        |
| Red Lentils      | 586       |
| Red Kidney Beans     | 577        |
| White Kidney Beans      | 575       |
| Green Gram    | 564        |
| Split & Skinned Black Gram      | 557       |
| Green Chickpeas    | 551        |
| Black Gram     | 527       |
| Split Black Gram    | 488        |
| Dew Bean     | 398       |
| Split Green Gram     | 220        |

# Training

* Training performed on 12GB NVIDIA Tesla K80, on Google Colab

* EfficientNet B0 with Image Size 224 used for training 

* Optimizer : AdamW

* Scheduler : ReducedPlateau

* Early Stopping with 5 Patience 
 
* 5 - Fold Cross Validation Used
          


Fold 0            |  Fold 1
:-------------------------:|:-------------------------:
<img src="req_files/training_graph/Fold0.png"/>  |  <img src="req_files/training_graph/Fold1.png"/> 

Fold 2            |  Fold 3| Fold4
:-------------------------:|:-------------------------:|:-------------------------:
<img src="req_files/training_graph/Fold2.png"/>  |  <img src="req_files/training_graph/Fold3.png"/> |<img src="req_files/training_graph/Fold4.png"/> 

# Evaulation

Feel free to go through the Classification Report for details.

<img src="req_files/classification_report.png"> 
                  
In brief, Our model gives around 98 % accuracy with different classes

# Deployment
Used Heroku for the deployment. Feel free to visit https://pulses-classification.herokuapp.com/ to experience the Web application

# License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/RsTaK/pulses-classification/blob/master/LICENSE) file for details.

Contact back if you want to access the dataset.