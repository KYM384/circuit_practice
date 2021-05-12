from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm
import numpy as np
import os

import warnings
warnings.simplefilter("ignore")


def plot(R_gen, L_gen, C_gen, save_path):
  # N パターン試す
  N = 100

  fig = plt.figure()
  frames = []

  # ラベル設定
  plt.xlim([-1.2, 1.2])
  plt.ylim([-1.2, 1.2])
  plt.xlabel("I")
  plt.ylabel("V")
  plt.grid()


  for theta in tqdm(range(N+1)):
    # R, L, C は θ の関数で変化していくとする

    R = max( R_gen(theta/N * 2*np.pi), 0.0001) # 0除算を防ぐ
    L = max( L_gen(theta/N * 2*np.pi), 0.0001) # 0除算を防ぐ
    C = max( C_gen(theta/N * 2*np.pi), 0.0001) # 0除算を防ぐ


    # 各値の記述
    frame0 = plt.text(x=0.7, y=0.8, s=f"θ={theta/N*2*np.pi:.5f}\nR={R:.5f}\nL={L:.5f}\nC={C:.5f}", bbox={"facecolor":"white"})


    # 微分方程式を解く
    M = np.array([[-R/L, -1/L], [1/C, 0]])
    def prob(x, t):
      return M @ x

    ts = np.linspace(0, 100, 10000)
    init = np.array([1, 0]).T

    vcn = odeint(prob, init, ts)


    # 相平面
    frame1 = plt.plot(vcn[:,0], vcn[:,1], c="r")

    frames.append([frame0] + frame1)

  # GIF で保存
  ani = animation.ArtistAnimation(fig, frames, interval=10)
  ani.save(save_path, writer="pillow")


if __name__ == "__main__":
  for variable in "RLC":
    for idx, other in enumerate([(1, 1), (1, 0.1), (0.1, 1), (0.1, 0.1)]):
      if variable == "R":
        R_gen = lambda x: np.abs(np.sin(x))
        L_gen = lambda x: other[0]
        C_gen = lambda x: other[1]
      elif variable == "L":
        R_gen = lambda x: other[0]
        L_gen = lambda x: np.abs(np.sin(x))
        C_gen = lambda x: other[1]
      elif variable == "C":
        R_gen = lambda x: other[0]
        L_gen = lambda x: other[1]
        C_gen = lambda x: np.abs(np.sin(x))

      save_path = os.path.join("gifs", variable + "_" + str(idx+1) + ".gif")

      plot(R_gen, L_gen, C_gen, save_path)
      print(save_path)