import numpy as np
import matplotlib.pyplot as plt

# Define Thought and Kinetic as normalized ranges
thought = np.linspace(0, 1, 100) # do ratio of thought
kinetic = np.linspace(0, 2, 100) # do ratio of exercise

# Calculate Reward1 (XOR) and Reward2 (AND) with float operations
reward1 = np.abs(thought - kinetic)
reward2 = thought * kinetic

# Define decay function based on dopamine balance (absolute difference)
decay = np.exp(-10 * np.abs(thought - kinetic))

# Calculate combined reward transitioning from Reward1 to Reward2 via decay
combined_reward = decay * reward2 + (1 - decay) * reward1

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(thought, reward1, label='Reward1 = Thought ⊕ Kinetic (XOR)', linestyle='--')
plt.plot(thought, reward2, label='Reward2 = Thought ∧ Kinetic (AND)', linestyle='--')
plt.plot(thought, decay, label='Decay (Dopamine Balance)', linestyle=':')
plt.plot(thought, combined_reward, label='Combined Reward (Transition)', linewidth=2)

plt.xlabel('Thought')
plt.ylabel('Value')
plt.title('Decay function transitioning Reward1 to Reward2 based on dopamine balance')
plt.legend()
plt.grid(True)
plt.show()

# Print some key values for analysis
print("Key Analysis Points:")
print(f"Maximum Reward1 (XOR): {np.max(reward1):.3f}")
print(f"Maximum Reward2 (AND): {np.max(reward2):.3f}")
print(f"Maximum Combined Reward: {np.max(combined_reward):.3f}")
print(f"Decay at perfect balance (0.5, 0.5): {np.exp(-10 * np.abs(0.5 - 0.5)):.3f}")
print(f"Decay at maximum imbalance (0, 1): {np.exp(-10 * np.abs(0 - 1)):.6f}")
