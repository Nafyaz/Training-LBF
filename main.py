import time

import gymnasium as gym
from argparse import ArgumentParser

import lbforaging

import numpy as np


def parse_args():
    parser = ArgumentParser()
    parser.add_argument( "--env", type=str, default="Foraging-16x16-4p-8f-v3", help="Environment to use")
    parser.add_argument("--episodes", type=int, default=1, help="How many episodes to run")
    parser.add_argument("--display_info", action="store_true", help="Display agent info per step")
    parser.add_argument("--render", action="store_true", help="Render the environment")

    return parser.parse_args()

def _game_loop(env, render):
    obss, info = env.reset()

    print(obss)

    done = False

    total_rewards = np.zeros(env.n_agents)

    if render:
        env.render()
        time.sleep(100)

    while not done:
        actions = env.action_space.sample()

        obss, rewards, done, _, _ = env.step(actions)
        total_rewards += rewards

        if render:
            env.render()
            time.sleep(0.5)

    print(f"Total reward: {total_rewards}")


def main(env_str="Foraging-16x16-4p-8f-v3", episodes=1, render=False):
    env = gym.make(env_str)

    for episode in range(episodes):
        _game_loop(env, render)

if __name__ == "__main__":
    args = parse_args()

    main(args.env, args.episodes, args.render)
