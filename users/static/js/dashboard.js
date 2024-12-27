// Dynamic updates for the stats (mock data example)
document.addEventListener("DOMContentLoaded", () => {
    const totalRequests = 124;
    const completedPickups = 78;
    const pendingPickups = totalRequests - completedPickups;

    document.getElementById('total-requests').textContent = totalRequests;
    document.getElementById('completed-pickups').textContent = completedPickups;
    document.getElementById('pending-pickups').textContent = pendingPickups;
});
