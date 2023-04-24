# PINN-Stresss

## Physics Informed Neural Network for Dynamic Stress Prediction

##### Code release for the paper: Physics Informed Neural Network for Dynamic Stress Prediction, preprint avilable on [arXiv](https://arxiv.org/abs/2211.16190)

#### Authors: [Hamed Bolandi](https://bolandih.github.io/), Gautam Sreekumar, Xuyang Li, Nizar Lajnef, Vishnu Boddeti

### Abstract

 Structural failures are often caused by catastrophic events such as earthquakes and winds. As a result, it is crucial
to predict dynamic stress distributions during highly disruptive events in real time. Currently available high-fidelity
methods, such as Finite Element Models (FEMs), super from their inherent high complexity. Therefore, to reduce
computational cost while maintaining accuracy, a Physics Informed Neural Network (PINN), PINN-Stress model,
is proposed to predict the entire sequence of stress distribution based on Finite Element simulations using a partial
diferential equation (PDE) solver. Using automatic diferentiation, we embed a PDE into a deep neural network’s loss
function to incorporate information from measurements and PDEs. The PINN-Stress model can predict the sequence
of stress distribution in almost real-time and can generalize better than the model without PINN.


### PINN-Stress

![overview_fig_PINN](https://user-images.githubusercontent.com/78941477/234051535-3c2f4610-d4e6-4a0e-9634-2381f7cc268c.png)

###  Comparisson of PINN-Stress(Physics Informed model) and NeuroStress(Non-Physics Informed Model)

![PINN-Neuro](https://user-images.githubusercontent.com/78941477/234069024-e308fb28-b5a4-44ae-94c9-6192b099f7d9.png)





