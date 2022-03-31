const btnMenu = document.getElementById('btn-menu');
const navLinks = document.getElementById('nav-links')

const toggleMenu = () => {
  navLinks.classList.toggle('hidden')
}
btnMenu.onclick = toggleMenu

// numero respaldo mundo pacifico para tecnico: 132 91 86