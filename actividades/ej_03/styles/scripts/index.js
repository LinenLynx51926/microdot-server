document.addEventListener('DOMContentLoaded', () => {
    const setpointSlider = document.getElementById("setpoint");
    const setpointValue = document.getElementById("setpoint-value");
    const tempActual = document.getElementById("temp-actual");
    const buzzerStatus = document.getElementById("buzzer-status");
    const tempIndicator = document.getElementById("temp-indicator");

    // Actualizar el valor del setpoint al mover el slider
    setpointSlider.addEventListener("input", () => {
        setpointValue.textContent = setpointSlider.value;
    });

    // Enviar el nuevo setpoint al soltar el slider
    setpointSlider.addEventListener("change", () => {
        fetch("/setpoint", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ setpoint: parseFloat(setpointSlider.value) })
        });
    });

    // Función para actualizar los datos de temperatura y estado del buzzer
    async function actualizarDatos() {
        try {
            const res = await fetch("/estado");
            const data = await res.json();
            
            // Actualizar temperatura actual
            tempActual.textContent = data.temp;
            
            // Actualizar estado del buzzer con animación
            if (data.buzzer) {
                buzzerStatus.textContent = "ACTIVO";
                buzzerStatus.className = "value buzzer active";
            } else {
                buzzerStatus.textContent = "INACTIVO";
                buzzerStatus.className = "value buzzer";
            }
            
            // Actualizar indicador visual
            const diff = data.temp - parseFloat(setpointSlider.value);
            const percentage = Math.min(Math.max((diff + 15) / 30 * 100, 0), 100);
            tempIndicator.style.left = `${percentage}%`;
            
        } catch (err) {
            console.error("Error al obtener datos:", err);
            tempActual.textContent = "Error";
            buzzerStatus.textContent = "Error";
            buzzerStatus.className = "value buzzer";
        }
    }

    // Actualizar cada 2 segundos
    setInterval(actualizarDatos, 2000);
    actualizarDatos(); // Llamada inicial
});