// Data provided by GamerPower: https://www.gamerpower.com/api-read
const api = "https://www.gamerpower.com/api/giveaways?platform=pc&type=game";
const storageKey = "quanx.gamerpower.announced.v1";

async function checkGames() {
  const res = await $task.fetch({url: api, method: "GET"});
  if (res.statusCode === 201 || res.statusCode === 204) return;
  if (res.statusCode !== 200) throw new Error("HTTP " + res.statusCode);
  const games = JSON.parse(res.body);
  if (!Array.isArray(games)) throw new Error("Unexpected response");
  const known = JSON.parse($prefs.valueForKey(storageKey) || "[]");
  const seen = new Set(known);
  const fresh = games.filter(game => Number.isInteger(game.id) && typeof game.title === "string" && !seen.has(game.id));
  if (!fresh.length) return;
  $notify("PC 游戏限免 · GamerPower", fresh.length + " 项可查看", fresh.slice(0, 3).map(game => game.title).join(" · "), {"open-url": "https://www.gamerpower.com/giveaways/pc"});
  const ids = [...new Set([...fresh.map(game => game.id), ...known])].slice(0, 1000);
  $prefs.setValueForKey(JSON.stringify(ids), storageKey);
}

checkGames().catch(error => console.log("GamerPower: " + error.message)).finally(() => $done());
