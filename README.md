# Road-extraction
Semi supervised Approach to extract road maps from aerial images using Generative adversarial networks in keras.


## Abstract
Road extraction from aerial image, stands as a quintessential node for the development of rudimentary layers in innumerable fields. From GIS, to Unmanned Aerial vehicles, road maps pave the foundation for data accumulation. This significant process is a result of number of mechanisms devised over the years through iterative experiments and research.  However, the glut of methods available often pose as a hurdle in the selection process. In this project we implement a novel approach to solve the extraction problem, by incorporating generative algorithm using conditional adversarial networks. We investigate conditional adversarial networks as a general-purpose solution to image-to-image translation problems. These networks not only learn the mapping from input image to output image, but also learn a loss function to train this mapping. This makes it possible to apply the same generic approach to problems that traditionally would require very different loss formulations. The U-Network incorporated essentially convolves and de-convolves over the generative model, thus producing a pixel to pixel image translation, the result of which is the vector road map of its corresponding aerial image. The entire model is trained on a 990 MS GPU for computational ease.  

## Introduction
-This project is about detecting roads in remotely sensed data using a novel generative approach with a GAN model. 
-The form of learning differs from discriminative/ predictive algorithm by aiming for image- image translation
-Instead of predicting a label given certain features, GANs attempt to predict features given a certain label
