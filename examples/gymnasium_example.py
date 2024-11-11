import gymnasium as gym

from generals.agents import RandomAgent, ExpanderAgent

# Initialize agents
agent = RandomAgent()
npc = ExpanderAgent()

# Create environment
env = gym.make("gym-generals-v0", agent=agent, npc=npc, render_mode="human")
# code_embedder:meow start
# Run the game
env.reset()
env.render()
env.close()
# code_embedder:meow end
