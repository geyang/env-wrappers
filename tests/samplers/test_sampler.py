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

    runner = runner_class([partial(rand_traj_gen, env_id="Reacher-v2", seed=i * 100) for i in range(n_envs)])
    with logger.time(f"Warmup: {n_envs} env"):
        for traj in tqdm(islice(runner.trajs(), 20)):
            assert traj['img'].shape == (50, 84, 84, 3)

    from time import sleep
    sleep(1.0)

    with logger.time(f"{n_envs} env"):
        for traj in tqdm(islice(runner.trajs(), 200)):
            assert traj['img'].shape == (50, 84, 84, 3)
    # testing the termination is important for making sure that we clean up
    del runner


def test_subproc_sampler():
    eval_sampler(SubprocRunner, 10)


def test_dummy_sampler():
    eval_sampler(DummyRunner, 10)


def test_message():
    pass
