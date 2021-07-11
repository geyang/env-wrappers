from cmx import doc

doc @ """
# Simple Example for using the Subprocess Parallel Environment Wrapper
"""

with doc:
    import gym
    from env_wrappers.vec_env import SubprocVecEnv, DummyVecEnv

    env_id = "Reacher-v2"
    seed = 100


    def make_env(rank):
        def _thunk():
            env = gym.make(env_id)
            env.seed(seed + rank)
            return env

        return _thunk

doc @ """
the spawning needs to happen after `__main__` according to this 
[link](https://github.com/hill-a/stable-baselines/issues/483)
"""

if __name__ == '__main__':
    with doc:
        vecenv = DummyVecEnv([make_env(rank) for rank in range(3)])

doc @ """
We provide a convenient factory function in this distribution of vector 
environments. It also takes additional positional arguments as
environment wrappers, reducing boiler plate.
"""

if __name__ == '__main__':
    with doc:
        from env_wrappers.vec_env import make_env

        dummy_wrappers = [lambda env: env] * 100

        env = DummyVecEnv([make_env("Reacher-v2", 100 * rank, *dummy_wrappers, ) for rank in range(3)])
        img = env.render('rgb_array', width=10, height=10)
        doc.print(f"env.num_envs = {env.num_envs}")
        doc.print(f"image is {type(img)} len:{img.__len__()} of shape: {img[0].shape}")

    table = ["Attribute;"]
    table.append(f"action space;{env.action_space}")
    table.append(f"observation space;{env.observation_space}")
    doc.csv(csv="\n".join(table), sep=";")
    doc.flush()
