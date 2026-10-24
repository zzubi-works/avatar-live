# 版本与许可

Avatar Live 的使用权、外部程序的使用权、角色·道具的使用权各不相同。

## 版本

| 项目 | Basic | Pro |
|---|---|---|
| 使用范围 | 个人·非公开使用 | 直播·视频公开·商业使用 |
| 价格 | 1,990日元 | 3,980日元 |
| 追踪·角色菜单 | 支持 | 支持 |
| OBS·相机输出 | 支持 | 支持 |
| 基本画面效果 | 支持 | 支持 |
| 照片保存 | 支持 | 支持 |
| 最大输出 | 1080p | 4K |
| 水印 | 有 | 无 |
| 姿势·动作 | — | 支持 |
| 道具·额外共享素材 | — | 支持 |
| 多角色·多相机 | — | 支持 |
| 远程会话·MP4录制 | — | 支持 |
| 额外画面效果 | — | 支持 |
| 直播联动·简易设置 测试版 (Beta) | — | 支持 |
| 节点编辑器 测试版 (Beta) | 仅查看 | 支持 |
| 内置房间·房间部件编辑 | — | 支持 |
| DLC 房间包 | 另行购买 | 另行购买 |

价格和销售条件以 BOOTH 商品页面的显示为准。

OBS·相机输出包含 Spout2·NDI·虚拟摄像头。基本画面效果为后期处理，额外画面效果包括后处理效果和环境光遮蔽。

## 激活与升级

- 一个许可供 1 人在 1 台电脑上使用。
- 激活和许可确认需要网络连接。
- 可以直接迁移到另一台电脑一次，之后的迁移请通过咨询处理。
- Basic → Pro：购买升级后，在设置 → 许可证 → 输入其他代码中输入。
- 体验中购买：在设置 → 许可证 → 输入其他代码中输入许可证。
- DLC 房间包：在同一个输入其他代码中输入 BOOTH 订单号。许可证保持不变，这台电脑即可下载房间包。可以迁移到另一台电脑一次。

不允许重新分发、出租、共享、修改程序或许可代码，或绕过保护措施。详细内容请遵循[使用条款](legal-terms.md)。

## NDI

NDI®是Vizrt NDI AB的注册商标。[NDI 官方网站](https://ndi.video/)

用于网络视频传输的外部技术。

- Avatar Live中包含的NDI Runtime遵循NDI SDK许可证。
- 许可证全文位于程序的 `AvatarLive_Data/Plugins/x86_64/Processing.NDI.Lib.Licenses.txt` 中。
- [NDI 工具](https://ndi.video/tools/)是需要单独下载的程序，不包含在 Avatar Live 中。
- 在 OBS 接收的 [DistroAV](https://github.com/DistroAV/DistroAV) 是独立的项目，并遵循该项目的许可证。

[NDI SDK 使用条件](https://docs.ndi.video/all/developing-with-ndi/sdk/licensing) · [NDI 连接方法](09-output.md#ndi)

## Spout2

在同一台 Windows PC 上用于程序之间传输视频的外部技术。

- Avatar Live 与 Spout2 集成使用的 [KlakSpout](https://github.com/keijiro/KlakSpout) 遵循 Unlicense。可以在发布版的第三方声明中查看全文。
- [OBS Spout2 Capture 插件](https://github.com/Off-World-Live/obs-spout2-plugin) 是单独的安装程序，并遵循该项目的 GPL v2 条件。
- 购买 Avatar Live 并不转让 OBS 插件的版权或其他权利。

[Spout2 连接方法](09-output.md#spout2)

## VB-CABLE

由 [VB-Audio Software](https://vb-audio.com/Cable/) 制作的独立虚拟音频驱动程序。

- VB-CABLE 是捐赠软件，其使用、分发和许可条件由 VB-Audio 决定。
- 安装按钮是安装 VB-Audio 原始驱动程序的路径。这不是 Avatar Live 开发的驱动程序。
- 所需的许可证和赞助请查看 [VB-Audio 官方许可证指南](https://vb-audio.com/Services/licensing.htm)。
- Avatar Live 的购买或 Pro 升级并不替代授予 VB-CABLE 的单独许可。

## 角色与道具

角色、服装、纹理、着色器、姿势、3D道具等内容的权利归各原作者所有。

在用于广播时，请确认以下事项以及各原制作人的使用规定后再使用。

| 考虑事项 | 需确认的协议 |
|---|---|
| 直播·视频公开 | 请确认原作者是否允许用于直播或商业用途。 |
| 文件修改·转换 | 请确认原作者的改造·转换条件。 |
| 远程会话传输 | 确认是否允许将数据传输到其他电脑并进行临时保存。 |
| 提供给他人 | 确认是否允许再分发或提供给第三方。 |

在使用角色和道具之前，请确认各原作者的权利和使用规定。获得必要的使用许可并遵守规定的责任由使用者承担。

购买或使用 Avatar Live 的功能并不代表获取内容的使用许可。Avatar Live 及其开发者不对用户使用、修改、传输或分发内容所引发的权利侵害或争议承担责任。

## 开源与独立性

所包含的开源组件遵循各自的许可证。请查看附带程序和导出器的说明。

Avatar Live 和 Avatar Exporter 是 Curious Bobby Co. 的独立产品。不会分发 VRChat SDK、NDMF、Modular Avatar 或 VRCFury，也不是各开发公司的官方产品或获授权产品。不访问 VRChat 账户和服务器。

## 实验性功能

应用中实验性显示的功能可能因设备和环境不同而表现不同。购买前请确认所需设备及[支持范围](12-troubleshooting.md#支持范围)。

## 相关文档

[使用条款](legal-terms.md) · [隐私政策](legal-privacy.md) · [退款政策](legal-refund.md) · [卖家信息](legal-seller.md)
