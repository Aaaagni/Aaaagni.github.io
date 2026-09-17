#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WU_JIAXU.com 本地服务器
=======================
- 提供静态页面服务（index.html / guestbook.html / 图片）
- 留言板持久化 API：
    GET  /api/notes            读取全部便签
    POST /api/notes            {name, text} 写入 guestbook-data.json
- 运行：python server.py  （默认端口 8623，可用环境变量 PORT 覆盖）
"""
import json
import os
import threading
from datetime import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(ROOT, "guestbook-data.json")
PORT = int(os.environ.get("PORT", "8623"))
HOST = os.environ.get("HOST", "127.0.0.1")

COLORS = ["c-yellow", "c-pink", "c-mint", "c-white"]

# 首次运行时的站长欢迎便签
SEED = [{
    "id": "seed-1",
    "name": "WU_JIAXU",
    "text": "欢迎光临毛毡板！贴张便签再走吧 (´｡• ω •｡`)\n这条是站长钉下的第一张。",
    "time": "站长の第一張",
    "color": "c-mint",
    "rot": "-2"
}]

_lock = threading.Lock()


def load_notes():
    with _lock:
        if not os.path.exists(DATA_FILE):
            return list(SEED)
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            return data if isinstance(data, list) and data else list(SEED)
        except Exception:
            return list(SEED)


def save_notes(notes):
    with _lock:
        tmp = DATA_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(notes, f, ensure_ascii=False, indent=2)
        os.replace(tmp, DATA_FILE)


class Handler(SimpleHTTPRequestHandler):
    """静态文件 + 留言板 API"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    # ---------- 工具 ----------
    def _json(self, obj, code=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    # ---------- GET ----------
    def do_GET(self):
        if urlparse(self.path).path == "/api/notes":
            self._json({"ok": True, "notes": load_notes()})
            return
        super().do_GET()

    # ---------- POST ----------
    def do_POST(self):
        if urlparse(self.path).path != "/api/notes":
            self._json({"ok": False, "error": "not found"}, 404)
            return

        length = int(self.headers.get("Content-Length", 0) or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            data = json.loads(raw.decode("utf-8") or "{}")
        except Exception:
            data = {}
        name = str(data.get("name", "")).strip()[:20]
        text = str(data.get("text", "")).strip()[:200]
        if not name or not text:
            self._json({"ok": False, "error": "name and text required"}, 400)
            return

        now = datetime.now()
        note = {
            "id": now.strftime("%Y%m%d%H%M%S%f"),
            "name": name,
            "text": text,
            "time": "%d/%d %02d:%02d" % (now.month, now.day, now.hour, now.minute),
            "color": COLORS[now.microsecond % 4],
            "rot": "%.1f" % ((now.microsecond % 61) / 10 - 3),
        }
        notes = load_notes()
        notes.insert(0, note)          # 新便签钉在最前
        save_notes(notes)
        self._json({"ok": True, "notes": notes})

    def log_message(self, fmt, *args):
        pass  # 安静模式，日志由启动端重定向


if __name__ == "__main__":
    print("WU_JIAXU.com 本地服务器已启动: http://%s:%d  (留言板数据: %s)"
          % (HOST, PORT, DATA_FILE))
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
