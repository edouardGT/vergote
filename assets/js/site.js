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

// Seasonal touch, automatic on the visitor's date (no deploy needed):
//   7–26 December: holly berries on the logo, a small pill above the home headline, a footer greeting.
//   27 December – 15 January: a gold star on the logo, a New Year pill and footer greeting.
// Preview with ?seizoen=kerst, ?seizoen=nieuwjaar or ?seizoen=geen.
(function () {
  var now = new Date();
  var month = now.getMonth(); // 0 = January, 11 = December
  var day = now.getDate();
  var season = null;
  if (month === 11 && day >= 7 && day <= 26) season = 'kerst';
  else if ((month === 11 && day >= 27) || (month === 0 && day <= 15)) season = 'nieuwjaar';

  var forced = new URLSearchParams(window.location.search).get('seizoen');
  if (forced === 'kerst' || forced === 'nieuwjaar') season = forced;
  if (forced === 'geen') season = null;
  if (!season) return;

  document.documentElement.setAttribute('data-seizoen', season);
  var newYear = month === 0 ? now.getFullYear() : now.getFullYear() + 1; // in January it's this year's

  var pill = document.querySelector('.season-pill'); // home page only
  if (pill) {
    pill.querySelector('span').textContent = season === 'kerst' ? 'Fijne feestdagen' : 'Gelukkig nieuwjaar';
    pill.hidden = false;
  }
  var greeting = document.querySelector('.season-greeting'); // footer, every page
  if (greeting) {
    greeting.textContent = season === 'kerst'
      ? 'Mathieu wenst u fijne feestdagen.'
      : 'Gelukkig nieuwjaar! Mathieu wenst u een groen en gezond ' + newYear + '.';
    greeting.hidden = false;
  }
})();

// "Nu in de tuin" (home) + saffron year line (saffraan page): follow the visitor's month.
// All 12 months are in the HTML; this shows the current one and lets visitors peek at others.
// Preview another month with ?maand=1 … ?maand=12.
(function () {
  var MONTHS = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli',
                'augustus', 'september', 'oktober', 'november', 'december'];
  var current = new Date().getMonth();
  var forced = parseInt(new URLSearchParams(window.location.search).get('maand'), 10);
  if (forced >= 1 && forced <= 12) current = forced - 1;

  var section = document.getElementById('nu-in-de-tuin');
  if (section) {
    var articles = section.querySelectorAll('.maand');
    var buttons = section.querySelectorAll('.maand-knop');
    var show = function (i) {
      for (var a = 0; a < articles.length; a++) articles[a].hidden = a !== i;
      for (var b = 0; b < buttons.length; b++) buttons[b].setAttribute('aria-pressed', String(b === i));
      section.setAttribute('data-seizoen-tuin', articles[i].getAttribute('data-seizoen'));
    };
    if (articles.length === 12 && buttons.length === 12) {
      articles[current].querySelector('.maand-nu').hidden = false;
      buttons[current].classList.add('is-nu');
      var nu = section.querySelector('.tuinjaar-nu');
      nu.textContent = 'Het is ' + MONTHS[current] + ', ' +
        articles[current].querySelector('.maand-seizoen').textContent + ' in de tuin.';
      nu.hidden = false;
      section.querySelector('.maand-strip').hidden = false;
      for (var k = 0; k < buttons.length; k++) {
        buttons[k].addEventListener('click', function () { show(Number(this.getAttribute('data-maand'))); });
      }
      show(current);
    }
  }

  var saffraan = document.querySelector('.saffraan-nu');
  if (saffraan) {
    var line = saffraan.querySelector('[data-maand="' + current + '"]');
    if (line) {
      line.hidden = false;
      saffraan.querySelector('.saffraan-nu-label').textContent = 'Nu, in ' + MONTHS[current] + ':';
      saffraan.hidden = false;
    }
  }
})();
