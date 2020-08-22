
# Metaworld Environment Wrappers

> This document, including the embedded video, is generated 
> by [[cmx]](./__init__.py)

This module includes wrappers that are required to work 
with `metaworld` [link](https://github.com/rlworkgroup/metaworld).
In particular, we implemented a camera wrapper that directly
taps into the underlying `env.sim.render` function as opposed
to the gym environment `env.render` which is not implemented
in metaworld [L:111-113](https://github.com/rlworkgroup/metaworld/blob/master/metaworld/envs/mujoco/mujoco_env.py#L109-L111).

This wrapper makes it easy.

# Usage Example

We register single task metaworld environments under the 
`env_wrappers.metaworld` module, so that you can use `gym
.make` to create the environments without have to import
`metaworld` manually.


```python
import gym
from env_wrappers.metaworld import ALL_ENVS

for env_id in ALL_ENVS[:]:
    env = gym.make(f'env_wrappers.metaworld:{env_id}')
    frames = []
    for i in range(10):
        env.reset()
        env.step(env.action_space.sample())
        frames.append(env.render("rgb", width=240, height=240))
    row.video(frames, f"videos/{env_id}.gif", caption=env_id)
```

