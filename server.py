<h1>Connexions live</h1>

<p>Utilisateurs en ligne: <span id="count">0</span></p>
<p id="list"></p>

<script>
async function update() {
  const r = await fetch("https://chat-server-1xnj.onrender.com/status");
  const data = await r.json();

  document.getElementById("count").innerText = data.online;
  document.getElementById("list").innerText = data.clients.join(", ");
}

setInterval(update, 2000);
update();
</script>
