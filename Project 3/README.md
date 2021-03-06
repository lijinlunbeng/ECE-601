# Project 3 (Unity)

## Game Machine Learning

This project applies to machine learning and has interesting practical applications in a game. All the open source projects come from this site ：[Unity-ML](https://github.com/Unity-Technologies/ml-agents)
and thanks to the work of the developers, I plan to implement their latest seventh generation product in this project.

This project is very suitable for students who are new to machine AI learning, and I have learned a lot from it. It seems like a very complex project, but it's very useful for us to understand and understand how robots work and give them the ability to learn. In this sharing, I will actually use this machine learning, and put the experimental results of a game in this file. In addition, I will describe in details how I conducted this experiment.

Reinforcement learning can be viewed as a form of learning for sequential decision making that is commonly associated with controlling robots (but is, in fact, much more general). Consider an autonomous firefighting robot that is tasked with navigating into an area, finding the fire and neutralizing it. At any given moment, the robot perceives the environment through its sensors (e.g. camera, heat, touch), processes this information and produces an action (e.g. move to the left, rotate the water hose, turn on the water). In other words, it is continuously making decisions about how to interact in this environment given its view of the world (i.e. sensors input) and objective (i.e. neutralizing the fire). Teaching a robot to be a successful firefighting machine is precisely what reinforcement learning is designed to do.
