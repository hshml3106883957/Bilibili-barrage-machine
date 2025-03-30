# Bilibili-barrage-machine
一个把bilibili弹幕通过rcon转发到我的世界聊天框

将B站直播间弹幕和礼物实时转发到《我的世界》服务器的工具，通过RCON协议实现跨平台互动。

## 功能特性

- 🎯 **双向互动**：实时同步B站弹幕到游戏内聊天栏
- 🎁 **礼物播报**：自动感谢观众赠送的礼物
- 🛡️ **安全连接**：使用官方API和RCON协议
- 🖥️ **图形界面**：简单易用的配置窗口
- 🌈 **彩色消息**：支持Minecraft颜色代码格式化

## 常见问题
- ❓ **如何获取B站Cookie？**：
-浏览器登录B站后，通过开发者工具(F12)获取：
-SESSDATA 和 bili_jct 来自Cookies

- ⚠️ **RCON连接失败？**：
-确认服务器已开启RCON
-检查防火墙是否放行RCON端口
### server.properties
```bash
enable-rcon=true
rcon.port=your_port
rcon.password=your_password
```

##贡献指南
- 欢迎提交Issue或PR！建议改进方向：

- 添加Twitch/抖音直播支持

- 实现Web控制面板

- 开发消息队列系统
## 快速开始

### 环境要求
```bash
pip install -r requirements.txt
