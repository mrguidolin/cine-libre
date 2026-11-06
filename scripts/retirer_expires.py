"""Retire du catalogue les titres dont la date de fin (expIso) est passée."""
import datetime, json

path = "catalog.json"
c = json.load(open(path, encoding="utf-8"))
today = datetime.date.today().isoformat()
before = len(c["items"])
c["items"] = [i for i in c["items"] if not (i.get("expIso") and i["expIso"] < today)]
removed = before - len(c["items"])
if removed:
    c["updatedAt"] = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    json.dump(c, open(path, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
print(f"{removed} titre(s) expiré(s) retiré(s)")
