# python-CI-template
Python CI template for EC500 Software Engineering

# Implemention Proposal
1. Convert the model into tensor js type and then run the model in viewer's local browser.
2. Deploy the model in AWS ML agent and give out the result to viewers.

# Basic Sturcture and 
The basic theory and structure of our project can be seen from [the ppt](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/EC500_Team_14.ppt)<br>

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
```Keras```,```pytorch```to train the model.<br/>
```ngrok```,```Ngix```,```Django``` to build a web.<br/>

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


## DRAGAN with labels<br>
We've made it to generate anime images with controllable features.
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/Conditional_GAN/fake_samples_epoch_048.png)<br>
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/Conditional_GAN/real_samples_epoch_048.png)<br>
The second picture is the groundtruth images.<br>
The first picture is geneated with labels of the second picture.<br>


## API for controllable GAN is uploaded<br>
Simply call the ```load_model``` and ```get_by_label``` function in ```api_example.py``` can generate images.
With the API only one line is needed to generate specific images.<br>
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/Green.jpg)
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/Silver.jpg)
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/Red.jpg)
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/Blue.jpg)

### FrontEnd Website for Model Demo
We build a website for users to try our website.<br>
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/Make_Anime_Home.png)
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/Anime2.png)
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/anime3.png)<br>
And for deploy it to cloud server, we use ngrok to map the port on our local server to a public domain.
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/ngrok.png)<br>
as it shows in picture, we can visit  https://cfdfbf21.ngrok.io/polls (only works when I start the local server to run the model) to visit the website and generate anime images like the following picture.<br>
![image](https://github.com/ec500-software-engineering/project-14_Anime_Genration/blob/master/web_demo/result.png)
