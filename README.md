# 🚗 AI Safe Overtake — Reinforcement Learning Project

An AI-driven reinforcement learning project that trains an autonomous vehicle agent to **safely overtake other cars** in a highway environment using **Deep Q-Networks (DQN)**.
Built with **PyTorch**, **Stable Baselines3**, and **Highway-Env**, this project demonstrates safe, realistic driving behavior through a custom reward system and GPU-accelerated learning.

---

## 🧩 Features

* 🧠 **Custom Reward Function** — encourages smooth, collision-free, and realistic overtaking.
* ⚙️ **GPU Acceleration** — optimized using CUDA for faster training.
* 🎮 **Real-Time Demo** — renders a live simulation using Matplotlib.
* 🧱 **Modular Design** — separate scripts for training and demo execution.
* 💾 **Auto Model Detection** — automatically loads the latest trained `.zip` model file.

---

## 🗂️ Project Structure

```
📦 AI_Safe_Overtake/
│
├── main.py                  # Train the RL agent (DQN model)
├── demo_final_autoload.py   # Run the trained model and visualize behavior
├── rl_overtake_safe_realistic_v2.zip   # Trained model (auto-generated)
├── output.jpg               # Optional demo screenshot
└── README.md
```

---

## ⚙️ Installation

Make sure you have Python **3.9+** and CUDA-enabled GPU (optional but recommended).

```bash
# Clone the repository
git clone https://github.com/<your-username>/AI_Safe_Overtake.git
cd AI_Safe_Overtake

# Install dependencies
pip install torch stable-baselines3 highway-env gymnasium matplotlib numpy
```

---

## 🚀 How to Run

### 🧠 Train the Model

```bash
python main.py
```

This script:

* Configures the highway environment.
* Trains a DQN agent for 150,000 timesteps.
* Saves the model as `rl_overtake_safe_realistic_v2.zip`.

---

### 🎬 Run the Demo

After training (or if a model already exists):

```bash
python demo_final_autoload.py
```

The script will:

* Auto-detect the model `.zip` file.
* Load it on GPU.
* Launch a real-time driving simulation.
* Show live rewards per timestep.

Press **Ctrl + C** to stop the demo anytime.

---

## 🧠 Technical Details

| Component       | Description                                                      |
| --------------- | ---------------------------------------------------------------- |
| **Algorithm**   | DQN (Deep Q-Network)                                             |
| **Framework**   | Stable Baselines3                                                |
| **Environment** | highway-env (`highway-v0`)                                       |
| **Observation** | Kinematics                                                       |
| **Key Rewards** | Safe distance, smooth driving, overtaking success, crash penalty |

---

## 📊 Outputs

* ✅ `rl_overtake_safe_realistic_v2.zip` — Trained model
* 🎥 Real-time simulation window
* 🖥️ Step-by-step console rewards and episode summaries

---

## 🧑‍💻 Author

**Prem Sharma**
B.Tech CSE (III Year – V Semester)
Department of Computer Engineering and Applications
GLA University, Mathura
📧 [premnsharma2005@outlook.com](mailto:premnsharma2005@outlook.com)

---

## 🏁 Notes

* Modify environment parameters in `make_env()` for experimentation.
* To skip training, download and use the provided `.zip` model.
* Works best on GPU-enabled systems.

---

> 💡 *This project highlights the integration of AI and autonomous driving through safe, reinforcement learning–based overtaking behavior.*

---

Would you like me to add **GitHub badges** (like Python version, license, or “Made with ❤️”) at the top for a more aesthetic look?
