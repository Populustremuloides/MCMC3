# Gibbs Tweaks

## Results from learning the faculty data

The following are figures representing the learning process for the faculty data.
The legend in each figure represents the number of hyperparameters that were used in generating the learning run.
You will notice the bug that variance estimates go off to inifinity over time.
Perhaps a bug. Or perhaps a manifestation of the second law of thermodynamics????
I decided to show the values throughout the training process because it allowed you to see the mixing as well as a rough estimate of the mean.
The main difference introduced by hyperparameters is that the variability of the mixing in the mean estimates is slightly tighter with more hyperparameters.

Variance Parameter:

![plot](Figures/Figure_1_faculty_estimated_sigmas.png)

Mean Parameter:

![plot](Figures/Figure_2_faculty_estimated_mus.png)

## Adjustments to the number of data points per estimated node:

![plot](Figures/Figure_3_marygivenA_samples.png) 

![plot](Figures/Figure_3_marygivenNotA_samples.png)
