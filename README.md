# Quantumult X 合并配置

把 GitHub 上**目前仍在维护、确认可用**的 Quantumult X 规则、重写和脚本合到一份配置里，一键导入。

- 每天由 GitHub Actions 自动：重新拉取上游规则 → 合并去重 → 检查所有链接 → 结果写入 [STATUS.md](STATUS.md)
- 重写和脚本**直接引用原作者的链接**，作者更新你也跟着更新，不会因为复制而过时
- 不包含会员破解、Cookie 获取 / 薅羊毛类脚本，也不含混淆过、来源不明的脚本

## 一键导入

```
https://raw.githubusercontent.com/blacksheep81/quanx/main/QuantumultX.conf
```

1. 先在 Quantumult X 里备份原来的配置（导入会**覆盖**全部内容）
2. 风车 → 配置文件 → 下载 → 粘贴上面的地址
3. 节点 → 引用（订阅）→ 添加你自己的机场订阅，或者写到配置里的 `[server_remote]`
4. 风车 → MitM → 生成证书 → 安装描述文件 → 设置 › 通用 › 关于本机 › 证书信任设置 里打开信任
5. 打开 **重写** 和 **MitM** 开关

## 目录结构

| 路径 | 说明 |
|---|---|
| `QuantumultX.conf` | 主配置（一键导入用这个） |
| `rules/AdBlock.list` | 广告拦截合并规则（约 3.9 万条，fmz200 + blackmatrix7 AdvertisingLite + app2smile） |
| `rules/AI.list` | AI 合并规则：ChatGPT、Claude、Gemini、Copilot 等 |
| `rules/Streaming.list` | 国际流媒体合并规则：Disney+、HBO、Prime Video、Spotify、Twitch、巴哈姆特 |
| `rules/Social.list` | 海外社交合并规则：Twitter/X、Instagram、Facebook、Discord、Reddit、WhatsApp、Line |
| `scripts/sources.json` | 合并规则用到的上游来源，想加来源就在这里加一行 |
| `scripts/build.py` | 合并 + 链接检查脚本（只用 Python 标准库） |
| `STATUS.md` | 自动生成的链接健康报告 |

## 策略组

| 策略组 | 默认 | 说明 |
|---|---|---|
| 🚀 节点选择 | ♻️ 自动选择 | 总出口 |
| 🤖 AI 服务 | 🇺🇸 美国节点 | OpenAI / Claude 不支持香港节点，所以列表里没有香港 |
| 📺 YouTube / 🎬 Netflix / 🌍 国际媒体 | 🚀 节点选择 | |
| 🎵 TikTok | 🇯🇵 日本节点 | |
| 📲 电报 / 💬 海外社交 / 🔍 谷歌 / 🐙 GitHub | 🚀 节点选择 | |
| Ⓜ️ 微软 / 🍎 苹果 | direct | |
| 🏠 大陆服务 | direct | **人在海外**时，可以切到 🇨🇳 回国节点，用来看 B 站、网易云等限制大陆地区的内容 |
| 🛑 广告拦截 | reject | |
| 🐟 漏网之鱼 | 🚀 节点选择 | 没命中任何规则的流量 |

地区组（香港、台湾、日本、狮城、美国、韩国、澳洲、回国）会按节点名称里的关键词自动归类，并选延迟最低的节点。

## 重写（去广告与工具）

默认开启：fmz200 去广告合集（约 730 款 App）、微博&国际版、YouTube、哔哩哔哩、高德地图。

我逐条比对过这些重写（详见 [docs/rewrite-compare.md](docs/rewrite-compare.md)）：fmz200 合集里**没有** YouTube、哔哩哔哩、高德的完整规则，这三份单项重写和合集是互补关系、没有冲突，所以一起开。贴吧（已被合集完全覆盖）、知乎（有 3 条与合集冲突）、微信小程序（2023 年后未更新）默认关闭。

> YouTube 去广告需要禁用 QUIC，配置里已经加了 `udp_drop_list=443`。

工具：BoxJs、Sub-Store（订阅管理）、Script-Hub（把 Surge / Loon 模块转换成 QX 重写）。

## 节点页脚本

在“节点”页**长按某个节点**就可以运行：流媒体解锁查询、Google 送中检测、节点信息查询、策略流量查询、节点详情、测速。

## 本地运行

```bash
python3 scripts/build.py          # 合并规则 + 检查链接
python3 scripts/build.py --check  # 只检查链接
```

## 来源与致谢

本仓库只做整理、合并和可用性检查，规则与脚本的版权归原作者所有：

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)：分流规则
- [fmz200/wool_scripts](https://github.com/fmz200/wool_scripts)：去广告规则与重写、节点脚本
- [ddgksf2013/Rewrite](https://github.com/ddgksf2013/Rewrite)：单项去广告重写
- [app2smile/rules](https://github.com/app2smile/rules)：哔哩哔哩 / 贴吧去广告
- [KOP-XIAO/QuantumultX](https://github.com/KOP-XIAO/QuantumultX)：资源解析器、节点检测脚本
- [chavyleung/scripts](https://github.com/chavyleung/scripts)：BoxJs
- [sub-store-org/Sub-Store](https://github.com/sub-store-org/Sub-Store)
- [Script-Hub-Org/Script-Hub](https://github.com/Script-Hub-Org/Script-Hub)
- [getsomecat/Qx](https://github.com/getsomecat/Qx)：测速脚本
- [Koolson/Qure](https://github.com/Koolson/Qure)：图标

仅供学习交流，请遵守当地法律法规。
