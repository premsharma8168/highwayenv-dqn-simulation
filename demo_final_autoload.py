import os, glob, torch, warnings
warnings.filterwarnings("ignore")

import gymnasium as gym
import highway_env
from stable_baselines3 import DQN
import matplotlib.pyplot as plt


# ---------------------------------------------------------
# AUTO-DETECT MODEL FILE
# ---------------------------------------------------------
# find any .zip model in current directory
candidates = glob.glob("*.zip")
if not candidates:
    raise FileNotFoundError(" No .zip model file found in this folder.")
MODEL_PATH = candidates[0]  # pick the first one
print(f" Found model file: {MODEL_PATH}")

# ---------------------------------------------------------
# LOAD MODEL (GPU)
# ---------------------------------------------------------
try:
    model = DQN.load(MODEL_PATH, device="cuda")
    print(" Model loaded successfully on GPU.")
except Exception as e:
    print(f" Direct load failed ({e}). Attempting safe load...")
    import zipfile, io
    with zipfile.ZipFile(MODEL_PATH, "r") as z:
        if "policy.pth" in z.namelist():
            params = torch.load(io.BytesIO(z.read("policy.pth")), map_location="cuda")
        elif "parameters.pt" in z.namelist():
            params = torch.load(io.BytesIO(z.read("parameters.pt")), map_location="cuda")
        else:
            raise RuntimeError(" No model weights found inside zip.")

    env_temp = gym.make("highway-v0")
    model = DQN("MlpPolicy", env_temp, device="cuda")
    model.policy.load_state_dict(params, strict=False)
    print(" Model weights loaded manually on GPU.")

# ---------------------------------------------------------
# ENVIRONMENT SETUP
# ---------------------------------------------------------
env = gym.make("highway-v0", render_mode="rgb_array")
env.unwrapped.configure({
    "observation": {"type": "Kinematics"},
    "policy_frequency": 15,
    "duration": 30,
    "lanes_count": 3,
    "vehicles_count": 20,
    "simulation_frequency": 25,
    "controlled_vehicles": 1,
})
obs, _ = env.reset()

# ---------------------------------------------------------
# MATPLOTLIB LIVE RENDERER
# ---------------------------------------------------------
plt.ion()
fig, ax = plt.subplots(figsize=(8, 6))
img = ax.imshow(env.render())
ax.axis("off")
plt.title("AI Safe-Overtake Demo (Reinforcement Learning)", fontsize=12)
print("\n Demo started — press Ctrl+C to stop\n")
step, total_reward = 0, 0

try:
    while True:
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, truncated, info = env.step(action)
        total_reward += reward

        frame = env.render()
        img.set_data(frame)
        plt.pause(0.01)

        step += 1
        print(f"Step {step:04d} | Reward: {reward:6.2f} | Total: {total_reward:7.2f}", end="\r")

        if done or truncated:
            obs, _ = env.reset()
            print(f"\n Episode complete | Total Reward: {total_reward:.2f}\n")
            total_reward = 0

except KeyboardInterrupt:
    print("\n Demo stopped manually.")
finally:
    plt.ioff()
    plt.show()
    env.close()
    print(" Environment closed successfully.")
