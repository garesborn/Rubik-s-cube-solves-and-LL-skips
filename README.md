# Rubik-s-cube-solves-and-LL-skips

This project is explores my personal Rubik's cube solve times and how my speed is dependant on LL skips.

## Background

To understand what this project will explore, first you need a basic understanding of how to solve a rubik's cube.

A rubik's cube is made of 26 cubies (smaller cubes, sub cubes, etc.). Of these 26 cubies, there are 8 corners (each with 3 faces), 12 edges (each with 2 faces), and most importantly, 6 centers. These centers form axes for which all of the corners and edges can rotate around as seen below. These centers will always be in the exact same orientation (no matter how you rotate the sides) and therefore denote the face for that color. For example, the red, white, and blue centers/faces will always be oritented in a clockwise fashion as seen below.
![axis](https://user-images.githubusercontent.com/65193347/107469737-4bdc4700-6b38-11eb-953c-996b526e9529.png)

Now that we know that the faces of a cube will always have the same orientation, we can move on to the second most important rule of the cube. Every cubie only has 1 location and 1 orientation. For example, the red and white edge must always go in the slot adjecent to both the red and white centers, oriented so the each face is aligned to the proper color.

![red_white_edge](https://user-images.githubusercontent.com/65193347/107471264-e047a900-6b3a-11eb-8ce1-c435b396f846.png)

This rule is where most people get tripped up when trying to solve a cube for the first (and usually last) time. If you have ever heard someone proudly exclaim "I finished one side once" the quite likely had it looking more like cube on the left than the right (seen below).

![one_side](https://user-images.githubusercontent.com/65193347/107471935-091c6e00-6b3c-11eb-8e24-9bbabfb52e4b.png)
