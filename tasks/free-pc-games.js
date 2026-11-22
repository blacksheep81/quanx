// Data provided by GamerPower: https://www.gamerpower.com/api-read
const api = "https://www.gamerpower.com/api/giveaways?platform=pc&type=game";
const storageKey = "quanx.gamerpower.announced.v1";

async function checkGames() {
  const res = await $task.fetch({url: api, method: "GET"});
  if (res.statusCode === 201 || res.statusCode === 204) return;
  if (res.statusCode !== 200) throw new Error("HTTP " + res.statusCode);
  const games = JSON.parse(res.body);
  if (!Array.isArray(games)) throw new Error("Unexpected response");
  const stored = $prefs.valueForKey(storageKey);
  const valid = games.filter(game => Number.isInteger(game.id) && typeof game.title === "string");
  // 第一次运行只记录当前限免列表，不一次性推送全部
  if (!stored) {
    $prefs.setValueForKey(JSON.stringify(valid.map(game => game.id).slice(0, 1000)), storageKey);
    console.log("GamerPower: 首次运行，已记录 " + valid.length + " 项，之后只通知新增限免");
    return;
  }
  const known = JSON.parse(stored);
  const seen = new Set(known);
  const fresh = valid.filter(game => !seen.has(game.id));
  if (!fresh.length) return;
  $notify("PC 游戏限免 · GamerPower", fresh.length + " 项可查看", fresh.slice(0, 3).map(game => game.title).join(" · "), {"open-url": "https://www.gamerpower.com/giveaways/pc"});
  const ids = [...new Set([...fresh.map(game => game.id), ...known])].slice(0, 1000);
  $prefs.setValueForKey(JSON.stringify(ids), storageKey);
}

checkGames().catch(error => console.log("GamerPower: " + error.message)).finally(() => $done());
