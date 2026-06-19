const navLinks = document.querySelectorAll("nav a");
const sectionLinks = document.querySelectorAll('a[href^="#"]');
const sections = document.querySelectorAll("main section");

function showSection(targetId) {
    sections.forEach(section => {
        section.classList.remove("active");
    });

    document.getElementById(targetId).classList.add("active");

    navLinks.forEach(link => {
        link.classList.remove("active-nav");
    });

    const activeNav = document.querySelector(`nav a[href="#${targetId}"]`);
    if (activeNav) {
        activeNav.classList.add("active-nav");
    }
}

showSection("home");

sectionLinks.forEach(link => {
    link.addEventListener("click", function (event) {
        event.preventDefault();

        const targetId = this.getAttribute("href").substring(1);
        showSection(targetId);
    });
});