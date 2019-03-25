# python-CI-template
Python CI template for EC500 Software Engineering

# Implemention Proposal
1. Convert the model into tensor js type and then run the model in viewer's local browser.
2. Deploy the model in AWS ML agent and give out the result to viewers.

# User Story And Sprint Definition
Please see the [Trello Board](https://trello.com/b/PbjCmHFC/healthapp).<br>
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/Trello.png)<br>
Model Training is almost done.<br>
Local Web is almost done.<br>
Thing to be done:<br>
Convert model into JS style.<br>
Deploy cloud platform.<br>

# Modularity Definition
![Modularity Definition](https://github.com/ec500-software-engineering/project-team14_Anime_Genration/blob/master/Team_14_Anime_GAN.png)

# API used in Sprint1.
```numpy```,```pandas``` to handle the data.<br/>
```matplotlib``` to visualize data.<br/>
```Keras``` to train the model.<br/>
```Ngix```,```Django``` to build a web.<br/>

## Large GAN with resnet module<br>
performs worse than smaller sized model in similar structure.<br>

## WGAN-GP<br>
Conditional WGAN-GP works for mnist but not anime images.<br>
Normal WGAN-GP generates unclear anime images.<br>
![image](https://github.com/WenjieLuo2333/Anime_Generator/blob/master/WGAN-gp/WGAN-gp.png)<br>
Method to conditional :<br> G_input = multiply(noise,embedding_label)<br> D_input = multiply(flatten image,embedding_label)<br>
Way too easy,not work for complex images.<br>

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
