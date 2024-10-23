document.getElementById('startButton').addEventListener('click', function () {
    const duration = parseInt(document.getElementById('duration').value);
    const count = parseInt(document.getElementById('count').value);
    const image = document.getElementById('rotatingImage');

    let rotations = 0;
    const totalRotations = count * 360; // Total derajat yang akan diputar
    const rotationInterval = setInterval(() => {
        rotations += 360 / count;
        image.style.transform = `rotate(${rotations}deg`;

        if (rotations >= totalRotations) {
            clearInterval(rotationInterval);
        }
    }, duration * 1000 / count);
});
