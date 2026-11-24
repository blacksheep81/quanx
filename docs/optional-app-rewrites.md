# 应用功能重写核对记录

## 追加项目（2026-11-24）

以下五项已加入主配置，均为 `enabled=false`。仅核对配置与底层源码可读取，未实测新版 App；按需单项开启，异常时关闭。

| 项目 | 原始来源 | 已知范围和限制 |
| --- | --- | --- |
| Picsart | [配置](https://github.com/Marol62926/Quantumultx/blob/main/picsart.conf) · [脚本](https://github.com/Marol62926/MarScrpt/blob/main/picsart.js) | 配置标注测试版本 24.9.1；修改购买状态及 premium_tools_standard 权限，不能据此确认云端 AI 功能可用。 |
| Smallpdf | [配置](https://github.com/deezertidal/QuantumultX-Rewrite/blob/master/rewrite/smallpdf.conf) · [脚本](https://github.com/Marol62926/MarScrpt/blob/main/smallpdf.js) | 替换整个账户响应，可能改变账户信息显示；不代表服务端订阅或网页版权限。 |
| Alarmy | [配置](https://github.com/deezertidal/QuantumultX-Rewrite/blob/master/rewrite/alarmy.conf) · [脚本](https://github.com/Marol62926/MarScrpt/blob/main/alarmy.js) | 修改订阅数组，实际效果取决于 App 版本。 |
| 百度网盘 | [脚本](https://github.com/NobyDa/Script/blob/master/Surge/JS/BaiduCloud.js) | 在线视频倍速/清晰度用途，不提供下载加速或容量。本仓库提供窄域名 QX 包装。 |
| MIX | [脚本](https://github.com/NobyDa/Script/blob/master/Surge/JS/MIX.js) | 上游要求恢复购买；合集与脚本注释域名不同，本仓库包装兼容 bmall 与 cdn-bm 两个明确主机。 |

Bazaart 未接入：规则作用于多个 App 共用的 buy.itunes.apple.com/verifyReceipt，容易冲突。一木记账未接入：配置引用的底层脚本读取失败。

2026-11-24 核对。链接和源码可读取不代表当前 App 实测有效。节点订阅、Token 和个人证书不写入仓库。

| 项目 | 接入情况 | 限制与来源 |
| --- | --- | --- |
| CamScanner | 主配置启用，使用本仓库窄域名包装 | [NobyDa 原脚本](https://github.com/NobyDa/Script/blob/master/Surge/JS/CamScanner.js)替换 query_property 的部分高级权限返回值，未验证当前版本，不提供云端额度。仅处理 api.intsig.net 与 api-cs.intsig.net。 |
| Spotify | 主配置启用 | [app2smile 配置](https://github.com/app2smile/rules/blob/master/module/spotify.conf)：去播放广告、列表显示和取消强制随机；先登录再启用并重启 App。不支持超高音质，不等同于服务端 Premium。 |
| 海豚记账本 | 加为可选重写，默认关闭 | [Telegram 线索](https://t.me/gitbig/2018) → [配置](https://github.com/deezertidal/QuantumultX-Rewrite/blob/master/rewrite/htjzb.conf) → [脚本](https://github.com/deezertidal/shadowrocket-rules/blob/main/js/htjzb.js)。脚本替换 VIP 状态响应；帖子仅声称旧版 3.5.1 可用，未实测新版。 |
| Spotify 歌词翻译 | 仅列入索引，未直接启用 | [原脚本](https://github.com/app2smile/rules/blob/master/js/spotify-lyric.js)要求自行申请百度翻译 App ID/密钥；QX 用户需编辑本地副本。会把歌词提交百度翻译，不要把密钥写进公开仓库。 |
| 幻休 | 不接入 | [Telegram](https://t.me/gitbig/2099)引用的配置仍可读取，但其底层 HX.js 为混淆代码，且说明针对旧版，未纳入主配置。 |
| 起伏 | 不接入 | [Telegram](https://t.me/gitbig/2030)引用的配置存在，底层 deezertidal/private/js-backup/Crack/qifu.js 核对返回 404。 |
| CamScanner 另一版本 | 不接入 | [Telegram](https://t.me/gitbig/855)引用 chxm1023/Rewrite/main/CamScanner.js，核对返回 404；采用上面的 NobyDa 版本。 |

胖虎频道近期 CamScanner 与 Spotify 帖子也包含 Android APK，它们不是 iOS Quantumult X 重写，未加入配置。Quantumult X 群中亦有 Spotify 播放跳曲、插件可用性的反馈，因此不保证新版有效。

更新手机时建议单独添加这几项重写资源；整份重新下载会覆盖本机节点订阅和 MitM 证书，务必先备份。启用海豚记账本前先检查日志，异常时关闭该项。与同类重写不要重复开启。
