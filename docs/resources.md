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

## Spotify 独立分流与可选签到提醒

仓库的 Streaming 规则已经覆盖 Spotify。需要不同出口时，在现有配置的 `[filter_remote]` 段中，将以下条目置于国际媒体合并规则之前，并把策略名改为自己的策略组。

```ini
https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX/Spotify/Spotify.list, tag=Spotify, force-policy=proxy, enabled=true
```

若只需每天提醒，可在现有 `[task_local]` 段加入下方条目，并设置 `enabled=true`。脚本仅发送本机通知，签到与领取在官方 App 或小程序内手动完成。

```ini
0 9 * * * https://raw.githubusercontent.com/blacksheep81/quanx/main/tasks/checkin-reminder.js, tag=每日签到提醒, enabled=false
```

定时语法参考 [Quantumult X 官方任务示例](https://github.com/crossutility/Quantumult-X/blob/master/gallery.json)。可在任务界面手动运行一次并确认系统允许通知。
