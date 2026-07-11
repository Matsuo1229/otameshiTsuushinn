export default {
  async fetch(request) {
    if (request.headers.get("Upgrade") !== "websocket") {
      return new Response("WebSocket only", { status: 426 });
    }

    const pair = new WebSocketPair();
    const [client, server] = Object.values(pair);

    server.accept();

    server.addEventListener("message", (event) => {
      console.log("受信:", event.data);

      // クライアントへ返信
      server.send("サーバー: " + event.data);
    });

    server.addEventListener("close", () => {
      console.log("切断されました");
    });

    return new Response(null, {
      status: 101,
      webSocket: client,
    });
  },
};
