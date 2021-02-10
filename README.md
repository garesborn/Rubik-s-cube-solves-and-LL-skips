# Rubik-s-cube-solves-and-LL-skips

This project is explores my personal Rubik's cube solve times and how my speed is dependant on LL skips. While I will go into a little detail on how these cubes work, if you're looking to learn how to actually solve one start to finish I recommend [this tutorial](https://www.youtube.com/watch?v=R-R0KrXvWbc&t=1109s). It explains a dumbed down version of the method most "speedcubers" use (don't worry people will still think you're smart) appropriately called "The Beginner's Method." This is the method I started with, albeit from a pdf I found browsing the internet a little more than a decade ago.

## Background

To understand what this project will explore, first you need a basic understanding of how to solve a rubik's cube.

A rubik's cube is made of 26 cubies (smaller cubes, sub cubes, etc.). Of these 26 cubies, there are 8 corners (each with 3 faces), 12 edges (each with 2 faces), and most importantly, 6 centers. These centers form axes for which all of the corners and edges can rotate around as seen below. These centers will always be in the exact same orientation (no matter how you rotate the sides) and therefore denote the face for that color. For example, the red, white, and blue centers/faces will always be oritented in a clockwise fashion as seen below. (NOTE: this also means that certain faces like the white and yellow faces, will always be on opposite sides of the cube)
![axis](https://user-images.githubusercontent.com/65193347/107472318-bb543580-6b3c-11eb-9d47-fb84f73b10b0.png)

Now that we know that the faces of a cube will always have the same orientation, we can move on to the second most important rule of the cube. Every cubie only has 1 location and 1 orientation in it's solved state. For example, the red and white edge must always go in the slot adjacent to both the red and white centers, oriented so the each face is aligned to the proper color.

![red_white_edge](https://user-images.githubusercontent.com/65193347/107471264-e047a900-6b3a-11eb-8ce1-c435b396f846.png)

This rule is where most people get tripped up when trying to solve a cube for the first (and usually last) time. If you have ever heard someone proudly exclaim "I finished one side once," they quite likely had it looking more like cube on the left than the right (seen below).

![one_side](https://user-images.githubusercontent.com/65193347/107471935-091c6e00-6b3c-11eb-8e24-9bbabfb52e4b.png)

Now that we have a basic understanding of the rules of the cube, you are ready to learn a little bit about the most common method of solving, CFOP.
CFOP is an acronym for the 4 steps used in solving a cube. In order these steps are:

-Cross

-First 2 Layers

-Orient the Last Layer

-Permute the Last Layer

Now lets look at these a little deeper

# Cross

First step is to choose 1 face and create the cross. I always start with the white cross. The fastest cubers are able to start with any color allowing them to choose which will create the cross with the fewest turns. A solved cross can be seen below.

![cross](https://user-images.githubusercontent.com/65193347/107473453-bee8bc00-6b3e-11eb-82c5-1f2326d237d5.png)

# F2L

Next we must solve the first 2 layers of a cube. In the beginners method, this is done in 2 parts; first solving the first layer corners, then the second layer edges. In the advanced CFOP method, these are done at the same time. A finished F2L can be seen below.

![F2L](https://user-images.githubusercontent.com/65193347/107474386-4125b000-6b40-11eb-89cf-c8b12b30ac78.png)

# OLL

The last two steps are the focus of this study. Orienting the last layer, in our case the yellow layer, means to orient the remaining 4 corners and 4 edges so that their yellow face is aligned with the yellow center. a properly oriented last layer can be seen below.

![OLL](https://user-images.githubusercontent.com/65193347/107474879-2b64ba80-6b41-11eb-8d79-105b327a7486.png)

# PLL

The very last step is Permuting the last layer. While all of the edges and corners in the last layer are oriented so that the their yellow faces are aligned correctly, their other faces may not be permuted so that they align with their corresponding centers. Here is an example of an unpermuted last layer versus a permuted last layer (and therefore fully solved cube).

![PLL](https://user-images.githubusercontent.com/65193347/107475339-f0af5200-6b41-11eb-8dae-393eeb994712.png)



