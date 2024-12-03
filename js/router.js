const routes = {
    "/game1": "roms/game1.gb",
    "/game2": "roms/game2.gb",
    "/game3": "roms/game3.gb"
};

function loadGame(route) {
    const romPath = routes[route];
    if (romPath) {
        fetch(romPath)
            .then(response => response.arrayBuffer())
            .then(romBuffer => {
                const canvas = document.getElementById("screen");
                const emulator = new Binjgb(canvas, romBuffer);
                emulator.start();
            })
            .catch(err => console.error("Error loading ROM:", err));
    } else {
        document.body.innerHTML = "<p>Game not found</p>";
    }
}

function initRouter() {
    const currentPath = window.location.pathname;
    loadGame(currentPath);
}

window.onload = initRouter;

