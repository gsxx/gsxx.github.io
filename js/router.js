async function fetchRomList() {
    const response = await fetch('roms-list.json');
    const data = await response.json();
    return data.games;
}

function loadGame(romFile) {
    fetch(`roms/${romFile}`)
        .then(response => response.arrayBuffer())
        .then(romBuffer => {
            const canvas = document.getElementById("screen");
            const emulator = new Binjgb(canvas, romBuffer);
            emulator.start();
        })
        .catch(err => console.error("Error loading ROM:", err));
}

async function initRouter() {
    const roms = await fetchRomList();
    const currentPath = window.location.pathname;

    // Verifica si la ruta corresponde a un archivo ROM
    const romFile = currentPath.split("/").pop();
    if (roms.includes(romFile)) {
        loadGame(romFile);
    } else {
        document.body.innerHTML = "<p>Game not found</p>";
    }
}

window.onload = initRouter;
