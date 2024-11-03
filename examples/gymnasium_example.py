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
