let allRecipes = []; // store recipes for searching

// Load recipes on page load
document.addEventListener("DOMContentLoaded", () => {
    loadRecipes();
    setupSearch();
});

function loadRecipes() {
    fetch("/recipes")
        .then(res => res.json())
        .then(recipes => {
            allRecipes = recipes; // save for search
            displayRecipes(recipes);
        })
        .catch(err => console.error("Error loading recipes:", err));
}

function displayRecipes(recipes) {
    const container = document.getElementById("recipe-container");
    container.innerHTML = "";

    if (!recipes.length) {
        container.innerHTML = "<p>No recipes found.</p>";
        return;
    }

    recipes.forEach(r => {
        const card = document.createElement("div");
        card.classList.add("recipe-card");

        card.innerHTML = `
            <h3>${r.Title || "Untitled Recipe"}</h3>
            <p>${r.Description || "No description available."}</p>
            <p><strong>Prep:</strong> ${r.Prep_Time || 0} mins</p>
            <p><strong>Cook:</strong> ${r.Cook_Time || 0} mins</p>
            <p><strong>Servings:</strong> ${r.Servings || "N/A"}</p>
        `;

        container.appendChild(card);
    });
}

// Search bar logic
function setupSearch() {
    const searchInput = document.getElementById("search");
    if (!searchInput) return; // if no search bar, skip

    searchInput.addEventListener("input", () => {
        const term = searchInput.value.toLowerCase();

        const filtered = allRecipes.filter(r =>
            r.Title.toLowerCase().includes(term) ||
            (r.Description && r.Description.toLowerCase().includes(term)) ||
            (r.Label && r.Label.toLowerCase().includes(term))
        );

        displayRecipes(filtered);
    });
}
