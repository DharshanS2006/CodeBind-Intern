/**
 * static/js/main.js
 * TalentScan ATS — global JS
 * Dark/light mode toggle + misc helpers
 */

// ── Dark / Light Mode ────────────────────────────────────────────────────────
const htmlRoot   = document.getElementById('html-root');
const themeBtn   = document.getElementById('themeToggle');
const themeIcon  = document.getElementById('themeIcon');

function applyTheme(theme) {
  htmlRoot.setAttribute('data-bs-theme', theme);
  if (themeIcon) {
    themeIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
  }
  localStorage.setItem('ars-theme', theme);
}

// Load saved preference
const savedTheme = localStorage.getItem('ars-theme') || 'light';
applyTheme(savedTheme);

if (themeBtn) {
  themeBtn.addEventListener('click', () => {
    const current = htmlRoot.getAttribute('data-bs-theme') || 'light';
    applyTheme(current === 'light' ? 'dark' : 'light');
  });
}

// ── Auto-dismiss alerts after 4 s ────────────────────────────────────────────
document.querySelectorAll('.alert').forEach(el => {
  setTimeout(() => {
    const bsAlert = bootstrap.Alert.getOrCreateInstance(el);
    if (bsAlert) bsAlert.close();
  }, 4000);
});

// ── Chart.js global defaults ──────────────────────────────────────────────────
if (typeof Chart !== 'undefined') {
  Chart.defaults.font.family = "'Inter', system-ui, sans-serif";
  Chart.defaults.font.size   = 12;
  Chart.defaults.color       = '#94a3b8';
  Chart.defaults.plugins.tooltip.cornerRadius = 10;
  Chart.defaults.plugins.tooltip.padding      = 10;
  Chart.defaults.plugins.tooltip.boxPadding   = 4;
}

// ── Animate score bars on page load ──────────────────────────────────────────
window.addEventListener('load', () => {
  document.querySelectorAll('.score-bar-fill').forEach(el => {
    const target = el.style.width;
    el.style.width = '0%';
    setTimeout(() => { el.style.transition = 'width .7s ease'; el.style.width = target; }, 100);
  });
});
