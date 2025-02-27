const socket = new WebSocket("ws://localhost:8081");

socket.onopen = () => {
    console.log("Connected to WebSocket server");
};

socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    document.getElementById("ram-usage").textContent = data.ram_usage;
    document.getElementById("disk-usage").textContent = data.disk_usage;

    const alertElement = document.getElementById("alert");
    alertElement.textContent = data.alert ? data.alert : "";
};

socket.onerror = (error) => {
    console.error("WebSocket error:", error);
};

socket.onclose = () => {
    console.log("WebSocket connection closed");
};
