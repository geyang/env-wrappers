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
the spawning needs to happen after `__main__` according to this [link](https://github.com/hill-a/stable-baselines/issues/483)
"""

if __name__ == '__main__':
    with doc:
        vecenv = SubprocVecEnv([make_env(rank) for rank in range(3)])

doc @ """
We provide a convenient factory function in this distribution of vector 
environments. It also takes additional positional arguments as
environment wrappers, reducing boiler plate.
"""

if __name__ == '__main__':
    with doc:
        from env_wrappers.vec_env import make_env

        dummy_wrappers = [lambda env: env] * 100

        env = SubprocVecEnv([make_env("Reacher-v2", 100 * rank, *dummy_wrappers, ) for rank in range(3)])

    table = [["Attribute", ""]]
    table.append(["action space", env.action_space])
    table.append(["observation space", env.observation_space])
    doc.csv("\n".join([";".join([str(i) for i in row]) for row in table]), sep=";")
    doc.flush()
