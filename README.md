# Improving My Rubik's Cube Solve Times

This project explores my personal Rubik's cube solve times and how much I can improve my speed. While I will go into a little detail on how these cubes work, if you're looking to learn how to actually solve one start to finish I recommend [this tutorial](https://www.youtube.com/watch?v=R-R0KrXvWbc&t=1109s). It explains a dumbed down version of the method most "speedcubers" use (don't worry people will still think you're smart) appropriately called "The Beginner's Method." This is the method I started with, albeit from a pdf I found browsing the internet a little more than a decade ago.

## Background

To understand what this project will explore, first you need a basic understanding of the rules a rubik's cube.

A rubik's cube is made of 26 cubies (smaller cubes, sub cubes, etc.). Of these 26 cubies, there are 8 corners (each with 3 faces), 12 edges (each with 2 faces), and most importantly, 6 single-faced centers. These centers form axes for which all of the corners and edges can rotate around as seen below. 

This brings us to Rule #1: The centers will always be in the exact same orientation (no matter how you rotate the sides) and therefore denote the face for that color. 

For example, the red, white, and blue centers/faces will always be oritented in a clockwise fashion as seen below. NOTE: this also means that certain faces (white/yellow, red/orange, blue/green) will always be on opposite sides of the cube.
![axis](https://user-images.githubusercontent.com/65193347/108000123-2bd4d980-6fb7-11eb-84e8-5f613fd00978.png)

Now we can move onto Rule #2: Every cubie only has 1 location and 1 orientation in it's solved state. 

For example, the red and white edge must always go in the slot adjacent to both the red and white centers, oriented so that each face is aligned to the proper color.

![edge examples](https://user-images.githubusercontent.com/65193347/108000134-30998d80-6fb7-11eb-86b7-8e848044e721.png)

This rule is where most people get tripped up when trying to solve a cube for the first (and usually last) time. If you have ever heard someone proudly exclaim "I finished one side once," they quite likely had it looking more like cube on the left than the right (seen below).

![one_side](https://user-images.githubusercontent.com/65193347/108000136-33947e00-6fb7-11eb-8377-eff887b41901.png)

Now that we have a basic understanding of the rules of the cube, you are ready to learn a little bit about the most common method of solving, CFOP.
CFOP is an acronym for the 4 steps used in solving a cube. In order these steps are:

-Cross

-First 2 Layers

-Orient the Last Layer

-Permute the Last Layer

Each of these steps can be broken down further into algorithms. Algorithms are sequences of rotations or moves that place certain cubies into their proper locations and orientaions based on their starting point. Now lets look at these a little deeper.

## CFOP

### Cross

First step is to choose 1 face and create the cross. I always start with the white cross. The fastest cubers are able to start with any color allowing them to choose which will create the cross with the fewest turns. A solved cross can be seen below. A cross on any cube can be solved in, at most, 8 rotations.

![cross](https://user-images.githubusercontent.com/65193347/108000161-46a74e00-6fb7-11eb-9112-015961d3a76c.png)

### F2L

Next we must solve the first 2 layers of a cube. In the beginners method, this is done in 2 parts; first solving the first layer corners, then the second layer edges. In the advanced CFOP method, these are done at the same time. The fastest cubers can solve F2L with 4 algorithms, one for each edge/corner pair. A finished F2L can be seen below. NOTE: this cube is the same cube from the cross phase, but flipped over.

![F2L](https://user-images.githubusercontent.com/65193347/108000165-48711180-6fb7-11eb-96e7-7126ed236fce.png)

### OLL

Orienting the last layer, in our case the yellow layer, means to orient the remaining 4 corners and 4 edges so that their yellow face is aligned with the yellow center. The fastest cubers can orient the last layer with only one algorithm. Personally, it takes me between 1-3 algorithms to orient the last layer. Rarely, performing the last algorithm of the F2L stage will orient the last layer without the need for an OLL algorithm, known as an OLL skip. The odds of this happening is 1/216. A properly oriented last layer can be seen below.

![OLL](https://user-images.githubusercontent.com/65193347/108000169-49a23e80-6fb7-11eb-8ef6-bc22ecae390d.png)

### PLL

The very last step is Permuting the last layer. While all of the edges and corners in the last layer are oriented so that the their yellow faces are aligned correctly, their other faces may not be permuted (located) so that they align with their corresponding centers. The fastest cubers can permute the last layer with only one algorithm. I can permute the last layer of a cube with 1-2 algorithms. Once again, there is a small chance (1/76) that orienting the last layer will also permute it, known as a PLL skip. Here is an example of an unpermuted last layer versus a permuted last layer (and therefore fully solved cube).

![PLL](https://user-images.githubusercontent.com/65193347/108000171-4ad36b80-6fb7-11eb-8362-6033fe1a2cd5.png)

## How Can I Improve and How Much Will it Help?

Simply put, the goal of any speedcubing method is to limit the amount of turns to solve a cube. A [study by computer scientists](https://youtu.be/SUopbexPk3A?t=595) discovered that any cube, no matter the scamble, can be solved in at most 20 rotations. This is known as God's Number. However, for the human mind to solve a cube in 20 moves or less takes an immense amount of studying and pre-planning of a scramble, making this an unrealistic way to speed solve. The most reliable way to speed solve is to learn algorithms. A lot of algorithms. 

The beginner's method, a subset of about 10 CFOP method algorithms, allows you to solve the cube in about 120 moves. When I first started using this method, it took me over a minute to solve a cube. My first ever recorded time clocked in at 2 minutes and 5 seconds.

The full CFOP method has an algorithm for over 120 individual cases that can arise between the 4 steps of a solve (as described above). This will allow the best cubers to solve a cube in as little as 50 moves, still 30 moves more than God's Number. Currently, I have memorized about 70 of these algorithms, including all 41 F2L algorithms, with a current average time just over 25 seconds.

Below is a histogram of my last 600 timed solves.

![Solve_hist](https://user-images.githubusercontent.com/65193347/107996864-66d30f00-6faf-11eb-98b2-c44093cd5d11.png)

Looking further into the data, I noticed many of my fastest solves have either OLL or PLL skips, including 2 of my 3 fastest solves and 4 of my top 10. 

Fun Fact: The odds of a full last layer skip is about 1/15,000. I have had 2 in my more than 10 years of cubing. One was untimed. The other was a long standing personal best of just under 23 seconds when I was averaging around 35 seconds.

### Last Layer

Seeing my reliance on LL skips, I decided to run a set of solves where I tracked how many algorithms I required to solve the last layer. Below is a heatmap depicting 250 solves sorted into bins by number of last layer algorithms and solve time. The red lines denote the average solve time for each of the 4 Y axis bins. The green line denotes the average time of the 250 solves.

![ll_hist](https://user-images.githubusercontent.com/65193347/108001576-cc78c880-6fba-11eb-9904-44512bf7a431.png)

Any last layer can be finished in at most 2 algorithms. Currently, the 18 OLL algorithms and 11 PLL algorithms I have memorized only allow me to solve around 10% of last layers with 2 algorithms. The more I memorize the more I will cut down the gap of 2.8 seconds between my current average and my 2 look LL average.

### Cross

Lastly, I wanted to check the other step I am most uncomfortable with, the cross. Solving the cross is dissimilar to other steps in that it requires more intuition and less memorization. There are two goals I aim for when solving the cross. Firstly, no cross should take more than 8 moves to solve. Secondly, to aim for a sub 20 average, you should be able to solve the cross in 4 seconds. To examine these, I ran two different test sets. 

First, I ran a set of 50 untimed solves, counting the amount of moves to complete the cross each time. This yeilded an average of 7.12 moves. Of these 50, 10 required more than 8 moves to complete.

Next, I ran a set of 75 timed cross solves which yeilded an average time of 3.84 seconds. These results can be seen below.

![cross solves](https://user-images.githubusercontent.com/65193347/107986513-38970480-6f9a-11eb-8d12-850bd354d8d2.png)

While there is a pretty alarming range in these solves, I don't think I will spend much time improving on my crosses. Currently my average is better than my 4 second goal, but I am imperfect 1/5th of the time I solve the cross. I am confident I will continue to be more comfortable solving crosses with time. 

### Overview

Overall, I think the most important way to improve is to simply continue learning last layer algorithms. Below is plot of my last 600 timed solves. 

![600_solves](https://user-images.githubusercontent.com/65193347/107989320-0e484580-6fa0-11eb-8454-9369dfa28b74.png)

Over the course of these 600 solves, I memorized about 10 new LL algorithms. As the regression line illustrates, my averages have improved. There is a 2.6 second difference between the averages of my first and last 200 solves. 

There are a number of other ways to improve my times including becoming color independent, improving my inspection phase to begin setting up F2L pairs, and impoving skills like recognition or finger tricks. Assuming I can trim down an additional 3 seconds on my average by learning the rest of the LL algorithms, I can explore these other avenues to get my average under 20 seconds. But for now, I need to accept that knowledge is, in fact, power

