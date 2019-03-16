# python-CI-template
Python CI template for EC500 Software Engineering

# User Story And Sprint Definition
Please see the [Trello Board](https://trello.com/b/PbjCmHFC/healthapp).

# Modularity Definition
![Modularity Definition](https://github.com/ec500-software-engineering/project-team14_Anime_Genration/blob/master/Team_14_Anime_GAN.png)

# API used in Sprint1.
```numpy```,```pandas``` to handle the data.<br/>
```matplotlib``` to visualize data.<br/>
```Keras``` to train the model.<br/>
```Ngix```,```Django``` to build a web.<br/>

## ACGAN with Resnet<br>
The result shows that the image at the same location generally has a same color of hair. It shows that ACGAN works to control the output.<br>
![image](https://github.com/WenjieLuo2333/Anime_Generator/blob/master/Res_ACGAN_Large/20400.png)
![image](https://github.com/WenjieLuo2333/Anime_Generator/blob/master/Res_ACGAN_Large/20600.png)
![image](https://github.com/WenjieLuo2333/Anime_Generator/blob/master/Res_ACGAN_Large/20800.png)<br>
But the images is not clear. More works need to be done.

## DRAGAN with out label<br>
Genrate Model trained. Controllable Version to be done.<br>

For Res_DRAGAN the result is generally good.<br>
![image](https://github.com/WenjieLuo2333/Anime_Generator/blob/master/Res_DRAGAN/Predict_2.png)<br>
And for Interpolation it seems that the entries of noise is realated to the feature of pictures.<br>
![image](https://github.com/WenjieLuo2333/Anime_Generator/blob/master/Res_DRAGAN/inter_2.png)<br>
