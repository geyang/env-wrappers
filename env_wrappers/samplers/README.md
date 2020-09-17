# Multi-process Sampling

The subprocess sampling running in this module provides a good abstraction around multiprocess RL sampling, in the form of a trajectory generator.

It returns full trajectories which do not need to be of the same length. For details, look at the `__main__` scripts in each file.

## Performance Characteristics

Initializing each environment is practically blocking and sequential, therefore to measure the sampling performance we need to first warm up the sampler. The speed improvement is about 1.6 times with 10 environments. 

