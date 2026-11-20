// Tuinen Vergote Mathieu: responsive navigation + footer year.
// The menu is a native popover when the links do not fit, and an inline
// list when they do. Without script it stays a popover (still works).
(function () {
  var header = document.querySelector('.site-header');
  var inner = header && header.querySelector('.header-inner');
  var menu = document.getElementById('site-menu');
  var button = header && header.querySelector('.menu-button');
  var hasPopover = Object.prototype.hasOwnProperty.call(HTMLElement.prototype, 'popover');

  if (!hasPopover) {
    // Old browsers (e.g. iOS before 18.3): a simple toggle instead of a polyfill.
    document.documentElement.classList.add('no-popover');
    if (button && menu) {
      button.setAttribute('aria-expanded', 'false');
      button.addEventListener('click', function () {
        var open = menu.classList.toggle('is-open');
        button.setAttribute('aria-expanded', String(open));
      });
    }
  }

  if (header && inner && menu) {
    var collapsedAt = 0;

    var isOpen = function () {
      if (!hasPopover) return menu.classList.contains('is-open');
      try { return menu.matches(':popover-open'); } catch (e) { return false; }
    };

    var layout = function () {
      var width = header.clientWidth;
      var wide = header.classList.contains('is-wide');
      // While collapsed, only remeasure when the header got wider.
      if (!wide && collapsedAt && width <= collapsedAt) return;

      var wasOpen = isOpen();
      header.classList.add('is-measuring', 'is-wide');
      if (hasPopover) menu.removeAttribute('popover');

      if (inner.scrollWidth <= inner.clientWidth) {
        collapsedAt = 0;
      } else {
        header.classList.remove('is-wide');
        if (hasPopover) {
          menu.setAttribute('popover', 'auto');
          if (wasOpen) menu.showPopover();
        }
        collapsedAt = width;
      }
      requestAnimationFrame(function () { header.classList.remove('is-measuring'); });
    };

    if ('ResizeObserver' in window) {
      var ro = new ResizeObserver(layout);
      ro.observe(header);
      ro.observe(menu);
    } else {
      layout();
      window.addEventListener('resize', layout);
    }
  }

  var year = document.getElementById('jaar');
  if (year) year.textContent = String(new Date().getFullYear());
})();
