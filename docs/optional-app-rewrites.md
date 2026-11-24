# 应用功能重写核对记录

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
