# 圈叉资源索引

2026-11-22 核对。分流链接适合按服务单独选出口。已有合并规则时，先在请求记录中查看命中情况；需要独立控制时，再把细分规则放在综合规则之前。整份配置请先备份再比较。

## 按应用分流

- [Telegram](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Telegram/Telegram.list)
- [Apple](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Apple/Apple.list)
- [Google](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Google/Google.list)
- [OpenAI](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/OpenAI/OpenAI.list)
- [Gemini](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Gemini/Gemini.list)
- [YouTube](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/YouTube/YouTube.list)
- [Spotify](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Spotify/Spotify.list)
- [WeChat](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/WeChat/WeChat.list)
- [Whatsapp](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Whatsapp/Whatsapp.list)
- [Baidu](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Baidu/Baidu.list)
- [DouYin](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/DouYin/DouYin.list)
- [HBO](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/HBO/HBO.list)
- [TikTok](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/TikTok/TikTok.list)
- [Twitter](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Twitter/Twitter.list)
- [Ubisoft](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Ubisoft/Ubisoft.list)
- [Weibo](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Weibo/Weibo.list)
- [Speedtest](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Speedtest/Speedtest.list)
- [Tencent](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Tencent/Tencent.list)

## 综合规则与其他分流

- [Global](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Global/Global.list)
- [ChinaMax](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/ChinaMax/ChinaMax.list)
- [ChinaIPs](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/ChinaIPs/ChinaIPs.list)
- [Binance](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Binance/Binance.list)
- [PikPak](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/PikPak/PikPak.list)
- [SystemOTA](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/SystemOTA/SystemOTA.list)
- [Hijacking](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Hijacking/Hijacking.list)
- [AWAvenue 广告过滤](https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/Filters/AWAvenue-Ads-Rule-QuantumultX.list)
- [Telegram 备选](https://raw.githubusercontent.com/Repcz/Tool/X/QuantumultX/Rules/Telegram.list)

## 整份配置参考

- [官方语法示例](https://raw.githubusercontent.com/crossutility/Quantumult-X/master/sample.conf)
- [Orz-3 入门配置](https://raw.githubusercontent.com/Orz-3/QuantumultX/master/Orz-3.conf)
- [Repcz](https://raw.githubusercontent.com/Repcz/Tool/X/QuantumultX/QuantumultX.conf)
- [耳东橙](https://raw.githubusercontent.com/erdongchanyo/Rules/main/Quantumult%20X/LazyConf/QuantumultX_EDC-Lazy.conf)
- [KOP-XIAO](https://raw.githubusercontent.com/KOP-XIAO/QuantumultX/master/QuantumultX_Profiles.conf)
- [fmz200](https://raw.githubusercontent.com/fmz200/wool_scripts/main/QuantumultX/config/QuanX.conf)

## 工具与特定版本资源

- [KOP-XIAO 格式解析器](https://raw.githubusercontent.com/KOP-XIAO/QuantumultX/master/Scripts/resource-parser.js)
- [虎扑广告过滤测试版（上游标注 8.2.67 和 8.2.68）](https://raw.githubusercontent.com/akaagiao1/quantumult-x-scripts/main/hupu/hupu-ad.conf)

## 主配置与上游对照

| 功能 | 主配置中的选择 | 原因 |
| --- | --- | --- |
| Telegram | 启用 blackmatrix7 独立分流，排在社交合并规则之前 | 核对时 blackmatrix7 有 40 条，Repcz 有 51 条。后者含共享分析域名 api.mixpanel.com，可能连其他 App 的分析请求也走电报策略。Repcz 保留为备选。 |
| Spotify | 启用独立策略组，初始跟随国际媒体 | 可单独切换出口。已有 Streaming 合并订阅的用户可直接更新主配置，无需手工再加一份。 |
| Apple Music | 可选，默认关闭 | 上游有 10 条细分规则。需要让音乐与其他 Apple 服务走不同出口时启用。[原始规则](https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/AppleMusic/AppleMusic.list) |
| 每日签到提醒 | 本地时间 09:00，默认关闭 | 在任务列表启用并允许通知；提醒后自行前往 App 领取。脚本只调用本地通知。[任务脚本](../tasks/checkin-reminder.js) · [官方任务格式](https://github.com/crossutility/Quantumult-X/blob/master/gallery.json) |

更新前备份当前个人配置。更新后可在请求记录中检查 Spotify 和 Telegram 的实际匹配策略。
