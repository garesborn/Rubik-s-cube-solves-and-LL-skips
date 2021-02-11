# Rubiks-cube-solves-and-LL-skips

This project is explores my personal Rubik's cube solve times and how improve my speed. While I will go into a little detail on how these cubes work, if you're looking to learn how to actually solve one start to finish I recommend [this tutorial](https://www.youtube.com/watch?v=R-R0KrXvWbc&t=1109s). It explains a dumbed down version of the method most "speedcubers" use (don't worry people will still think you're smart) appropriately called "The Beginner's Method." This is the method I started with, albeit from a pdf I found browsing the internet a little more than a decade ago.

## Background

To understand what this project will explore, first you need a basic understanding of the rules a rubik's cube.

A rubik's cube is made of 26 cubies (smaller cubes, sub cubes, etc.). Of these 26 cubies, there are 8 corners (each with 3 faces), 12 edges (each with 2 faces), and most importantly, 6 centers. These centers form axes for which all of the corners and edges can rotate around as seen below. 

This brings us to Rule #1: The centers will always be in the exact same orientation (no matter how you rotate the sides) and therefore denote the face for that color. 

For example, the red, white, and blue centers/faces will always be oritented in a clockwise fashion as seen below. NOTE: this also means that certain faces (white/yellow, red/orange, blue/green) will always be on opposite sides of the cube.
![axis](https://user-images.githubusercontent.com/65193347/107472318-bb543580-6b3c-11eb-9d47-fb84f73b10b0.png)

Now we can move onto Rule #2: Every cubie only has 1 location and 1 orientation in it's solved state. 

For example, the red and white edge must always go in the slot adjacent to both the red and white centers, oriented so the each face is aligned to the proper color.

![edge examples](https://user-images.githubusercontent.com/65193347/107482087-3a516a00-6b4d-11eb-8b40-53995552e17f.png)

This rule is where most people get tripped up when trying to solve a cube for the first (and usually last) time. If you have ever heard someone proudly exclaim "I finished one side once," they quite likely had it looking more like cube on the left than the right (seen below).

![one_side](https://user-images.githubusercontent.com/65193347/107471935-091c6e00-6b3c-11eb-8e24-9bbabfb52e4b.png)

Now that we have a basic understanding of the rules of the cube, you are ready to learn a little bit about the most common method of solving, CFOP.
CFOP is an acronym for the 4 steps used in solving a cube. In order these steps are:

-Cross

-First 2 Layers

-Orient the Last Layer

-Permute the Last Layer

Each of these steps can be broken down further into algorithms. Algorithms are sequences of rotations that place certain cubies into their proper locations and orientaions based on their starting point. Now lets look at these a little deeper.

# Cross

First step is to choose 1 face and create the cross. I always start with the white cross. The fastest cubers are able to start with any color allowing them to choose which will create the cross with the fewest turns. A solved cross can be seen below. A cross on any cube can be solved in, at most, 8 rotations.

![cross](https://user-images.githubusercontent.com/65193347/107485872-5c99b680-6b52-11eb-8c22-aa833a4327b3.png)

# F2L

Next we must solve the first 2 layers of a cube. In the beginners method, this is done in 2 parts; first solving the first layer corners, then the second layer edges. In the advanced CFOP method, these are done at the same time. The fastest cubers can solve F2L with 4 algorithms, one for each edge/corner pair. A finished F2L can be seen below. NOTE: this cube is the same cube from the cross phase, but flipped over.

![F2L](https://user-images.githubusercontent.com/65193347/107474386-4125b000-6b40-11eb-89cf-c8b12b30ac78.png)

# OLL

The last two steps are the focus of this study. Orienting the last layer, in our case the yellow layer, means to orient the remaining 4 corners and 4 edges so that their yellow face is aligned with the yellow center. The fastest cubers can orient the last layer with only one algorithm. Personally, it takes me between 1-3 algorithms to orient the last layer. A properly oriented last layer can be seen below.

![OLL](https://user-images.githubusercontent.com/65193347/107474879-2b64ba80-6b41-11eb-8d79-105b327a7486.png)

# PLL

The very last step is Permuting the last layer. While all of the edges and corners in the last layer are oriented so that the their yellow faces are aligned correctly, their other faces may not be permuted (located) so that they align with their corresponding centers. The fastest cubers can permute the last layer with only one algorithm. I can permute the last layer of a cube with 1-2 algorithms. Here is an example of an unpermuted last layer versus a permuted last layer (and therefore fully solved cube).

![PLL](https://user-images.githubusercontent.com/65193347/107476057-20ab2500-6b43-11eb-95a5-b1c25092c179.png)

UH OH! This is a work in progress... Come back soon!




