
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
        frames.append(env.render("rgb", width=240, height=240))
    row.video(frames, f"videos/{env_id}.gif", caption=env_id)
```

<div style="flex-wrap:wrap; display:flex; flex-direction:row; item-align:center;"><div><div style="text-align: center">Reach-v1</div><img style="margin:0.5em;" src="videos/Reach-v1.gif" /></div><div><div style="text-align: center">Push-v1</div><img style="margin:0.5em;" src="videos/Push-v1.gif" /></div><div><div style="text-align: center">Pick-place-v1</div><img style="margin:0.5em;" src="videos/Pick-place-v1.gif" /></div><div><div style="text-align: center">Door-open-v1</div><img style="margin:0.5em;" src="videos/Door-open-v1.gif" /></div><div><div style="text-align: center">Drawer-open-v1</div><img style="margin:0.5em;" src="videos/Drawer-open-v1.gif" /></div><div><div style="text-align: center">Drawer-close-v1</div><img style="margin:0.5em;" src="videos/Drawer-close-v1.gif" /></div><div><div style="text-align: center">Button-press-topdown-v1</div><img style="margin:0.5em;" src="videos/Button-press-topdown-v1.gif" /></div><div><div style="text-align: center">Peg-insert-side-v1</div><img style="margin:0.5em;" src="videos/Peg-insert-side-v1.gif" /></div><div><div style="text-align: center">Window-open-v1</div><img style="margin:0.5em;" src="videos/Window-open-v1.gif" /></div><div><div style="text-align: center">Window-close-v1</div><img style="margin:0.5em;" src="videos/Window-close-v1.gif" /></div><div><div style="text-align: center">Door-close-v1</div><img style="margin:0.5em;" src="videos/Door-close-v1.gif" /></div><div><div style="text-align: center">Reach-wall-v1</div><img style="margin:0.5em;" src="videos/Reach-wall-v1.gif" /></div><div><div style="text-align: center">Pick-place-wall-v1</div><img style="margin:0.5em;" src="videos/Pick-place-wall-v1.gif" /></div><div><div style="text-align: center">Push-wall-v1</div><img style="margin:0.5em;" src="videos/Push-wall-v1.gif" /></div><div><div style="text-align: center">Button-press-v1</div><img style="margin:0.5em;" src="videos/Button-press-v1.gif" /></div><div><div style="text-align: center">Button-press-topdown-wall-v1</div><img style="margin:0.5em;" src="videos/Button-press-topdown-wall-v1.gif" /></div><div><div style="text-align: center">Button-press-wall-v1</div><img style="margin:0.5em;" src="videos/Button-press-wall-v1.gif" /></div><div><div style="text-align: center">Peg-unplug-side-v1</div><img style="margin:0.5em;" src="videos/Peg-unplug-side-v1.gif" /></div><div><div style="text-align: center">Disassemble-v1</div><img style="margin:0.5em;" src="videos/Disassemble-v1.gif" /></div><div><div style="text-align: center">Hammer-v1</div><img style="margin:0.5em;" src="videos/Hammer-v1.gif" /></div><div><div style="text-align: center">Plate-slide-v1</div><img style="margin:0.5em;" src="videos/Plate-slide-v1.gif" /></div><div><div style="text-align: center">Plate-slide-side-v1</div><img style="margin:0.5em;" src="videos/Plate-slide-side-v1.gif" /></div><div><div style="text-align: center">Plate-slide-back-v1</div><img style="margin:0.5em;" src="videos/Plate-slide-back-v1.gif" /></div><div><div style="text-align: center">Plate-slide-back-side-v1</div><img style="margin:0.5em;" src="videos/Plate-slide-back-side-v1.gif" /></div><div><div style="text-align: center">Handle-press-v1</div><img style="margin:0.5em;" src="videos/Handle-press-v1.gif" /></div><div><div style="text-align: center">Handle-pull-v1</div><img style="margin:0.5em;" src="videos/Handle-pull-v1.gif" /></div><div><div style="text-align: center">Handle-press-side-v1</div><img style="margin:0.5em;" src="videos/Handle-press-side-v1.gif" /></div><div><div style="text-align: center">Handle-pull-side-v1</div><img style="margin:0.5em;" src="videos/Handle-pull-side-v1.gif" /></div><div><div style="text-align: center">Stick-push-v1</div><img style="margin:0.5em;" src="videos/Stick-push-v1.gif" /></div><div><div style="text-align: center">Stick-pull-v1</div><img style="margin:0.5em;" src="videos/Stick-pull-v1.gif" /></div><div><div style="text-align: center">Basketball-v1</div><img style="margin:0.5em;" src="videos/Basketball-v1.gif" /></div><div><div style="text-align: center">Soccer-v1</div><img style="margin:0.5em;" src="videos/Soccer-v1.gif" /></div><div><div style="text-align: center">Faucet-open-v1</div><img style="margin:0.5em;" src="videos/Faucet-open-v1.gif" /></div><div><div style="text-align: center">Faucet-close-v1</div><img style="margin:0.5em;" src="videos/Faucet-close-v1.gif" /></div><div><div style="text-align: center">Coffee-push-v1</div><img style="margin:0.5em;" src="videos/Coffee-push-v1.gif" /></div><div><div style="text-align: center">Coffee-pull-v1</div><img style="margin:0.5em;" src="videos/Coffee-pull-v1.gif" /></div><div><div style="text-align: center">Coffee-button-v1</div><img style="margin:0.5em;" src="videos/Coffee-button-v1.gif" /></div><div><div style="text-align: center">Sweep-v1</div><img style="margin:0.5em;" src="videos/Sweep-v1.gif" /></div><div><div style="text-align: center">Sweep-into-v1</div><img style="margin:0.5em;" src="videos/Sweep-into-v1.gif" /></div><div><div style="text-align: center">Pick-out-of-hole-v1</div><img style="margin:0.5em;" src="videos/Pick-out-of-hole-v1.gif" /></div><div><div style="text-align: center">Assembly-v1</div><img style="margin:0.5em;" src="videos/Assembly-v1.gif" /></div><div><div style="text-align: center">Shelf-place-v1</div><img style="margin:0.5em;" src="videos/Shelf-place-v1.gif" /></div><div><div style="text-align: center">Push-back-v1</div><img style="margin:0.5em;" src="videos/Push-back-v1.gif" /></div><div><div style="text-align: center">Lever-pull-v1</div><img style="margin:0.5em;" src="videos/Lever-pull-v1.gif" /></div><div><div style="text-align: center">Dial-turn-v1</div><img style="margin:0.5em;" src="videos/Dial-turn-v1.gif" /></div><div><div style="text-align: center">Bin-picking-v1</div><img style="margin:0.5em;" src="videos/Bin-picking-v1.gif" /></div><div><div style="text-align: center">Box-close-v1</div><img style="margin:0.5em;" src="videos/Box-close-v1.gif" /></div><div><div style="text-align: center">Hand-insert-v1</div><img style="margin:0.5em;" src="videos/Hand-insert-v1.gif" /></div><div><div style="text-align: center">Door-lock-v1</div><img style="margin:0.5em;" src="videos/Door-lock-v1.gif" /></div><div><div style="text-align: center">Door-unlock-v1</div><img style="margin:0.5em;" src="videos/Door-unlock-v1.gif" /></div></div>

The full list of environments are

```yaml
- Reach-v1
- Push-v1
- Pick-place-v1
- Door-open-v1
- Drawer-open-v1
- Drawer-close-v1
- Button-press-topdown-v1
- Peg-insert-side-v1
- Window-open-v1
- Window-close-v1
- Door-close-v1
- Reach-wall-v1
- Pick-place-wall-v1
- Push-wall-v1
- Button-press-v1
- Button-press-topdown-wall-v1
- Button-press-wall-v1
- Peg-unplug-side-v1
- Disassemble-v1
- Hammer-v1
- Plate-slide-v1
- Plate-slide-side-v1
- Plate-slide-back-v1
- Plate-slide-back-side-v1
- Handle-press-v1
- Handle-pull-v1
- Handle-press-side-v1
- Handle-pull-side-v1
- Stick-push-v1
- Stick-pull-v1
- Basketball-v1
- Soccer-v1
- Faucet-open-v1
- Faucet-close-v1
- Coffee-push-v1
- Coffee-pull-v1
- Coffee-button-v1
- Sweep-v1
- Sweep-into-v1
- Pick-out-of-hole-v1
- Assembly-v1
- Shelf-place-v1
- Push-back-v1
- Lever-pull-v1
- Dial-turn-v1
- Bin-picking-v1
- Box-close-v1
- Hand-insert-v1
- Door-lock-v1
- Door-unlock-v1
```
