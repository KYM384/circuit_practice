# 素子の値を変化させた時の相平面のアニメーション生成

[sample_top](samples/sample_top.gif)

## 環境
 - Python >= 3.6
 - Numpy
 - Matplotlib
 - Pillow
 - tqdm

## 実行
`graph_animation.py`を実行するとR,L,Cそれぞれの値のみを変化させた時のアニメーションを生成します．

[sample0](gifs/L_1.gif)

`plot`関数に渡す引数を変えてあげることで自由にアニメーションを生成できます．

----------------
### サンプル例

```
R_gen = lambda x: np.abs(np.sin(x + np.pi/4))
L_gen = lambda x: np.abs(np.sin(x))
C_gen = lambda x: np.abs(np.cos(x))
```

[sample1](samples/sample1.gif)

```
R_gen = lambda x: np.abs(np.cos(x))
L_gen = lambda x: np.abs(np.sin(x + np.pi/6))
C_gen = lambda x: np.abs(np.sin(x))
```
[sample2](samples/sample2.gif)