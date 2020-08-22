
# Meta-world Environment Wrapper

To instantiate a single task, do this:


```python
task_name = "box-close-v1"
env = MWEnv(task_name)
frames = []
for i in range(200):
    obs = env.reset()
    a = env.action_space.sample()
    env.step(a)
    frames.append(env.render('rgb', width=100, height=100))

doc.video(frames, f"videos/{task_name}.gif")
```

<img style="align-self:center;" src="videos/box-close-v1.gif" />
