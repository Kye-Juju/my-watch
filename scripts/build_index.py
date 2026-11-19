"""Rebuild data/index.json from the brief files in data/scans/."""
import json, pathlib, datetime
root = pathlib.Path(__file__).resolve().parent.parent / "data"
dates = sorted((p.stem for p in (root / "scans").glob("????-??-??.json")), reverse=True)
index = {"updated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), "dates": dates}
(root / "index.json").write_text(json.dumps(index, indent=1) + "\n")
print(f"index.json: {len(dates)} briefs, newest {dates[0] if dates else 'none'}")
