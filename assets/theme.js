(() => {
  const themes = ['gruvbox', 'light', 'dark'];
  let theme = 'gruvbox';
  try {
    const saved = localStorage.getItem('enirox-theme');
    if (themes.includes(saved)) theme = saved;
  } catch (_) { /* The default also works when storage is unavailable. */ }
  document.documentElement.dataset.theme = theme;
  document.addEventListener('DOMContentLoaded', () => {
    const picker = document.getElementById('theme');
    if (!picker) return;
    picker.value = theme;
    picker.addEventListener('change', () => {
      if (!themes.includes(picker.value)) return;
      document.documentElement.dataset.theme = picker.value;
      try { localStorage.setItem('enirox-theme', picker.value); } catch (_) {}
    });
  });
})();
