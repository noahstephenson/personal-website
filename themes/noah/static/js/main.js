const toggle = document.getElementById('dark-toggle');
const root = document.documentElement;

function applyIcon() {
  toggle.textContent = root.classList.contains('dark') ? '☀' : '☽';
}

// Set icon to match the state that was applied by the inline <head> script
applyIcon();

toggle.addEventListener('click', () => {
  root.classList.toggle('dark');
  localStorage.setItem('theme', root.classList.contains('dark') ? 'dark' : 'light');
  applyIcon();
});
