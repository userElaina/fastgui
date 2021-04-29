`pip install fastgui`

暂时只有两个函数: `testgui` `mtgui`.

可以用于快速测试 with GUI.

或者......可以用于快速打包一个带GUI的可执行程序?
毕竟写配置 `json` 可比画框框方便多了)

为了debug方便,颜色弄得很奇怪,可以自己改.

---
testgui
---

`eg_test.py` 的运行结果. `import fastgui` 并把根据你需要测试的函数写好的 `json` 扔进 `testgui()` ,然后 `exec()` 返回的字符串.大概就是这样.

![image](https://user-images.githubusercontent.com/80948381/116332908-2b518e00-a805-11eb-8807-df6f686e3d0f.png)
![image](https://user-images.githubusercontent.com/80948381/116332924-33a9c900-a805-11eb-9083-d67240ade064.png)

---
mtgui
---

`eg_mt.py` 的运行结果. `import fastgui` 并把你的 `json` 和函数扔进 `mtgui()` ,修改 `json` 即可修改gui中的显示内容.大概就是这样.

![image](https://user-images.githubusercontent.com/80948381/116553935-3a336000-a92d-11eb-88a3-d222a2ebc143.png)
