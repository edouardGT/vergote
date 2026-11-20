// Tuinen Vergote Mathieu: menu on small screens + current year in the footer.
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('hoofdmenu');

  if (toggle && nav) {
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
    };
    toggle.addEventListener('click', function () {
      setOpen(toggle.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        setOpen(false);
        toggle.focus();
      }
    });
  }

  var year = document.getElementById('jaar');
  if (year) { year.textContent = String(new Date().getFullYear()); }
})();
