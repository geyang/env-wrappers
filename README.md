# `gym-wrappers`, a collection of wrappers for OpenAI Gym environments

This repository make available variants of the `baselines.common.vec_env` environment wrapers, so that you can run multi-process sampling without installing tensorflow. 

We make additionoally available an experimental multi-threaded sample generator. For details, take a look at the specs folder [[tests]](./tests).

Current release at `v0.1.21`.

## Installation

To install:
```bash
pip install env-wrappers
```
or
```bash
pip install git+https://github.com/geyang/env-wrappers
```

## Usage Example

```python
import gym
from env_wrappers.vec_env import SubprocVecEnv, DummyVecEnv
from env_wrappers.vec_env import make_env

dummy_wrappers = [lambda env: env] * 10

env = SubprocVecEnv([make_env("Reacher-v2", 100 * rank, *dummy_wrappers, ) for rank in range(3)])
img = env.render('rgb_array', width=10, height=10)
doc.print(f"env.num_envs = {env.num_envs}")
doc.print(f"image is {type(img)} len:{img.__len__()} of shape: {img[0].shape}")
```

```
python
env.num_envs = 3
image is <class 'list'> len:3 of shape: (10, 10, 3)
```

| Attribute         | Unnamed: 1                     |
| ----------------- | ------------------------------ |
| action space      | Box(-1.0, 1.0, (2,), float32)  |
| observation space | Box(-inf, inf, (11,), float64) |

## Experimental Multi-process Sampler

This amazing sampler allows you to use python to write sequential logic, inside a multi-process sampler. The speedup is sublinear, which is why it remains experimental.

```python
import gym
import numpy as np
from collections import defaultdict
from tqdm import tqdm
from functools import partial
from itertools import islice

from env_wrappers.samplers.subproc_runner import SubprocRunner
from env_wrappers.samplers.dummy_runner import DummyRunner


def rand_traj_gen(env_id, seed, limit=None, **context_args):
    env = gym.make(env_id)
    env.seed(seed)

    yield "ready"

    while True:
        obs = env.reset()
        traj = defaultdict(list, obs=[obs])
        act, done = env.action_space.sample(), False
        for step in range(limit or 1_000):
            # you can add a print statement here to visualize timing
            # currently this does not benefit from async execution.
            # We need a FIFO
            obs, r, done, info = env.step(act)
            traj['obs'].append(obs)
            traj['r'].append(r)
            traj['info'].append(info)
            img = env.render("rgb_array", width=84, height=84)
            traj['img'].append(img)
            if done:
                break

        new_limit = yield {k: np.stack(v, axis=0) for k, v in traj.items()}
        if new_limit is not None:
            limit = new_limit


def eval_sampler(runner_class, n_envs=5, ):
    from ml_logger import logger
    from time import sleep

    runner = runner_class([partial(rand_traj_gen, env_id="Reacher-v2", seed=i * 100) for i in range(n_envs)])

    iter = runner.trajs()
    sleep(15)
    with logger.time(f"Warm-up: {n_envs} env"):
        for traj in tqdm(islice(iter, 20)):
            assert traj['img'].shape == (50, 84, 84, 3)

    sleep(1.0)

    iter = runner.trajs()
    with logger.time(f"{n_envs} env"):
        for traj in tqdm(islice(iter, 200)):
            assert traj['img'].shape == (50, 84, 84, 3)
    # testing the termination is important for making sure that we clean up
    del runner


def test_subproc_sampler():
    eval_sampler(SubprocRunner, 10)


def test_dummy_sampler():
    eval_sampler(DummyRunner, 10)
```



Ge Yang © 2020

