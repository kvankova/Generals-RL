## 🌱 Getting Started
Creating an agent is very simple. Start by subclassing an `Agent` class just like
[`RandomAgent`](./generals/agents/random_agent.py) or [`ExpanderAgent`](./generals/agents/expander_agent.py).
You can specify your agent `id` (name) and `color` and the only thing remaining is to implement the `act` function,
that has the signature explained in sections down below.


### Usage Example (🤸 Gymnasium)
The example loop for running the game looks like this
```python:examples/gymnasium_example.py
import gymnasium as gym

from generals.agents import RandomAgent, ExpanderAgent
# code_embedder:A start
# Initialize agents
agent = RandomAgent()
npc = ExpanderAgent()
# code_embedder:A end
# Create environment
env = gym.make("gym-generals-v0", agent=agent, npc=npc, render_mode="human")

observation, info = env.reset()
terminated = truncated = False
while not (terminated or truncated):
    action = agent.act(observation)
    observation, reward, terminated, truncated, info = env.step(action)
    env.render()


def main():
    """Main function to run the game."""
    # Initialize agents
    agent = RandomAgent()
    npc = ExpanderAgent()
    # Create environment

    env = gym.make("gym-generals-v0", agent=agent, npc=npc, render_mode="human")
    return env

```

```python:examples/gymnasium_example.py:A
# Initialize agents
agent = RandomAgent()
npc = ExpanderAgent()
```

```python:examples/gymnasium_example.py:main
def main():
    """Main function to run the game."""
    # Initialize agents
    agent = RandomAgent()
    npc = ExpanderAgent()
    # Create environment

    env = gym.make("gym-generals-v0", agent=agent, npc=npc, render_mode="human")
    return env
```
