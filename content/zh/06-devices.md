# 6. 设备

## 摄像头与麦克风

<div class="shot" markdown="1">

![设备页面](img/devices.png)

- 打开 **摄像头** 开关，即开始面部和手部追踪。
- 在摄像头列表中选择要使用的摄像头。
- **正面校准** — 将当前的面部朝向设为正面。
- **追踪质量** — 与游戏同时使用时，建议选择 **均衡** 或 **节能**。
- 打开 **麦克风** 开关后，说话时嘴巴就会动。
- **噪声门** — 让嘴巴不会因键盘声等杂音而动。
- **检测背景噪声** — 保持安静时点击此按钮，即可自动设定噪声基准。

</div>

## 追踪来源

<div class="shot" markdown="1">

![追踪来源](img/sources.png)

- 为面部、手臂、手、手指、嘴分别选择用什么来驱动。
- 将 **嘴** 设为 **面部 + 麦克风** 后，说话时跟随声音，不说话时跟随嘴形。
- **面部应用连接** — 不使用摄像头，而是从 iPhone（iFacialMocap）等应用接收面部数据。
- **Ultraleap 手部追踪** — 使用 Leap Motion 设备追踪手部。
- **外部追踪** — 通过 OSC · VMC 与其他应用连接。

</div>

> 💡 Ultraleap 和 OSC · VMC 是实验性功能。预计可以正常运行，但尚未在开发者环境中使用所有设备和应用进行测试。

## 用 iPhone 进行面部追踪（iFacialMocap）

<div class="steps" markdown="1">

1. 将 iPhone 和电脑连接到同一个 Wi-Fi。
2. 在 **面部应用连接** 中将来源选为 **iFacialMocap**，然后 **复制** **本机地址**。
3. 在 iPhone 的 iFacialMocap 应用中，点击齿轮 › **Destination IP address**（目标 IP 地址），输入该地址。
4. 打开开关后，iPhone 的表情就会应用到角色上。

</div>

> 💡 **iPhone地址（可选）** 栏可以留空。仅在 iFacialMocap 应用中不使用 Destination IP address 时才需要填写。
