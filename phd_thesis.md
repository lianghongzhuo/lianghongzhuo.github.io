---
layout: default
title: Patents
---
# Multimodal Perception for Robotic Grasping and Pouring

## Abstract

Programming a modern service robot to implement daily tasks requires a thorough understanding of the environment. Inspired by everyday human experience and the multimodal processing mechanism of the human brain, engineers have developed various sensors to build robots with a near-human sensory system. However, extracting valuable data from noisy inputs and efficiently integrating the multiple signals is still challenging. This dissertation investigates the use of multimodal sensory perception for two of the most fundamental service robot tasks, grasping and pouring.

Regarding two-fingered grasping, several effective improvements, i.e., attentional sampling, three-dimensional grid search, and invalid candidate correction, are added to a state-of-the-art grasp candidate generation algorithm. Then a novel deep-learning-based grasp evaluation algorithm PointNetGPD is proposed. To the best of our knowledge, PointNetGPD is the first work that uses 3D point clouds directly as input for grasp pose evaluation. In parallel, a self-built grasp dataset labels 350K parallel-jaw grasps by meticulous scores based on force-closure quality and friction coefficient values.

To endow robots with the same dexterity as human hands, a closed-loop multifingered grasping framework based on multimodal reinforcement learning is presented. A dexterous grasping simulation environment is built to train a multifingered grasping agent. This agent uses fingertip tactile sensing, joint torques, and hand proprioception as observation and outputs the joint actions for a multifingered hand. To reduce the dimension of the target space, a PCA-based hand synergy is calculated based on a self-collected dataset with pairwise human hand and robot hand motions. In the real robot experiments, the improved grasp generation method and the PointNetGPD model are used to determine the initial grasp poses. Furthermore, real robot experiments show that the trained agent can be applied in the real world even if the model is trained purely in simulation.

To tackle the two major challenges, generalization and precision, in the perception for robotic pouring, two neural networks AP-Net and MP-Net, are proposed. The recurrent neural network AP-Net utilizes the audio vibration to estimate liquid height and generalizes well to different experiment settings (e.g., different target containers, different initial liquid heights, different liquid types) while the precision can still be guaranteed. However, the performance of the audio-only AP-Net model is limited in noisy environments. Therefore, the novel audio-haptic recurrent deep MP-Net is proposed to predict liquid height in real-time and is robust to different levels and types of noise. Moreover, a multimodal pouring dataset including audio-frequency recordings, liquid real-time weight, force-torque data, video of the pouring motion, and source container trajectories during the pouring is collected.

The system assessment and comparison across network evaluation and various robotic experiments show that the proposed multimodal neural networks can successfully solve the grasping and pouring related perception problem. Combining the proposed perception networks learned for grasping and pouring, a service robot can accomplish daily tasks like grasping, pouring, and serving a drink to human users.

## Download link

[https://ediss.sub.uni-hamburg.de/handle/ediss/9635](https://ediss.sub.uni-hamburg.de/handle/ediss/9635)
