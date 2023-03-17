## run this with python3 plot_rl_rewards.py --m train
### and python3 plot_rl_rewards.py --m test

import matplotlib.pyplot as plt
import numpy as np
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-m','--mode',type=str, required=True,
                        help='either "train" or "test"') 
args=parser.parse_args()

a=np.load(f'rl_trader_rewards/{args.mode}.npy')

#print(f'average reward: {a.mean():.2f},min:{a.min():.2f},max:{a.max():.2f}')
if len(a) > 0:
    print(f'average reward: {a.mean():.2f},min:{a.min():.2f},max:{a.max():.2f}')
else:
    print("The array 'a' is empty.")

if args.mode == 'train':
  # show the training progress
  plt.plot(a)
else:
  # test - show a histogram of rewards
  plt.hist(a, bins=20)


#plt.hist(a,bins=20)
plt.title(args.mode)
plt.show()
