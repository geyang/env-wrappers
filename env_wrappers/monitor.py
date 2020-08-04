import time
from gym.core import Wrapper


class Monitor(Wrapper):

    def __init__(self, env, prefix, allow_early_resets=False):
        Wrapper.__init__(self, env=env)
        from ml_logger import logger

        self.prefix = prefix
        self.logger = logger
        self.allow_early_resets = allow_early_resets
        self.t0 = time.time()
        self.rewards = []
        # self.episode_rewards = []
        # self.episode_lengths = []
        self.total_steps = 0
        self.additional_key_values = {}  # extra info that gets injected into each log entry
        # Useful for metalearning where we're modifying the environment externally
        # But want our logs to know about these modifications

    def __getstate__(self):
        return self.__dict__.copy()

    def __setstate__(self, d):
        self.__dict__ = d

    def reset(self):
        if not self.allow_early_resets and self.rewards:
            raise RuntimeError(
                "Tried to reset an environment before done. If you want to allow early "
                "resets, wrap your env with Monitor(env, path, allow_early_resets=True)")
        return self.env.reset()

    def step(self, action):
        ob, rew, done, info = self.env.step(action)
        self.rewards.append(rew)
        if done:
            self.rewards = []
            eprew = sum(self.rewards)
            eplen = len(self.rewards)
            epinfo = {"r": eprew, "l": eplen, "t": round(time.time() - self.t0, 6)}
            epinfo.update(self.additional_key_values)
            epinfo["total_steps"] = self.total_steps

            with self.logger.PrefixContext(self.prefix):
                self.logger.log_metrics(epinfo, flush=True, silent=True)

            # self.episode_rewards.append(eprew)
            # self.episode_lengths.append(eplen)
            info['episode'] = epinfo

        self.total_steps += 1
        return ob, rew, done, info
