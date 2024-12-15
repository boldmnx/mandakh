document.addEventListener("DOMContentLoaded", function () {
    const savedTheme = localStorage.getItem("theme") || "light";
    document.documentElement.setAttribute("data-bs-theme", savedTheme);

    const toggleButton = document.getElementById("toggleDarkMode");
    if (toggleButton) {
        toggleButton.addEventListener("click", function () {
            const htmlElement = document.documentElement;
            const currentTheme = htmlElement.getAttribute("data-bs-theme");
            const newTheme = currentTheme === "dark" ? "light" : "dark";

            htmlElement.setAttribute("data-bs-theme", newTheme);
            localStorage.setItem("theme", newTheme); // Store the theme preference in localStorage
        });
    }
});
