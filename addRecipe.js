document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        // Take raw instructions and split into lines
        const rawInstructions = document.getElementById("instructions").value
            .split("\n")
            .map(line => line.trim())
            .filter(line => line.length > 0);

        // Convert each line into "Step X: text"
        const formattedInstructions = rawInstructions
            .map((line, index) => `Step ${index + 1}: ${line}`)
            .join("\n");

        const recipe = {
            name: document.getElementById("name").value,
            ingredients: document.getElementById("ingredients").value,
            instructions: formattedInstructions,
            prep: document.getElementById("prep").value,
            cook: document.getElementById("cook").value,
            servings: document.getElementById("servings").value,
            category: document.getElementById("category").value
        };

        fetch("/add-recipe", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(recipe)
        })
        .then(res => res.json())
        .then(data => {
            alert(data.message);
            form.reset();
            document.getElementById("previewBox").textContent = ""; // clear preview
        })
        .catch(err => console.error("Error:", err));
    });

    // Live preview of formatted steps
    document.getElementById("instructions").addEventListener("input", function () {
        const lines = this.value
            .split("\n")
            .map(l => l.trim())
            .filter(l => l.length > 0);

        const preview = lines
            .map((line, i) => `Step ${i + 1}: ${line}`)
            .join("\n");

        document.getElementById("previewBox").textContent = preview;
    });
});
