from platform import window

ws = window.WebSocket.new("wss://あなたのWorker名.workers.dev")

def on_open(event):
    print("接続成功")
    ws.send("こんにちは！")

def on_message(event):
    print("サーバーから:", event.data)

ws.onopen = on_open
ws.onmessage = on_message
