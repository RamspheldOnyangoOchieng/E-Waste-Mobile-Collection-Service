// Example of JavaScript functionality (smooth scroll for CTA buttons)
document.querySelectorAll('.cta-btn').forEach(button => {
    button.addEventListener('click', function (event) {
        event.preventDefault();
        const targetId = this.getAttribute('href').slice(1);
        const targetElement = document.getElementById(targetId);
        window.scrollTo({
            top: targetElement.offsetTop - 20,
            behavior: 'smooth'
        });
    });
});
