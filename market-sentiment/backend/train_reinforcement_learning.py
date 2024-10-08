import pandas as pd
from stable_baselines3 import PPO
from reinforcement_learning import TradingEnv

# Load merged sentiment and stock data
merged_data = pd.read_csv('sentiment_data.csv')  # Ensure it contains necessary features

# Initialize the trading environment
env = TradingEnv(merged_data)

# Initialize the model
model = PPO('MlpPolicy', env, verbose=1)

# Train the model
model.learn(total_timesteps=10000)

# Save the model
model.save("trading_model")
