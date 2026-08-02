/* ==========================================================================
   Himalayan Foundation — main.js
   Vanilla JS: nav, scroll effects, filters, accordion, lightbox, form, year
   ========================================================================== */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initNav();
    initHeaderScroll();
    initReveal();
    initFilters();
    initAccordion();
    initLightbox();
    initForm();
    initToTop();
    initYear();
  });

  /* ---------------- Mobile navigation ---------------- */
  function initNav() {
    var toggle = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.nav');
    if (!toggle || !nav) return;

    function close() {
      nav.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('nav-open');
    }

    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      document.body.classList.toggle('nav-open', open);
    });

    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', close);
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 900) close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
  }

  /* ---------------- Sticky header shadow ---------------- */
  function initHeaderScroll() {
    var header = document.querySelector('.header');
    if (!header) return;
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---------------- Reveal on scroll ---------------- */
  function initReveal() {
    var items = document.querySelectorAll('.reveal');
    if (!items.length) return;

    if (!('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('in'); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    items.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 70 + 'ms';
      io.observe(el);
    });
  }

  /* ---------------- Product filters ---------------- */
  function initFilters() {
    var buttons = document.querySelectorAll('.filter-btn');
    var items = document.querySelectorAll('[data-category]');
    if (!buttons.length || !items.length) return;

    function apply(filter) {
      items.forEach(function (item) {
        var show = filter === 'all' || item.dataset.category === filter;
        item.style.display = show ? '' : 'none';
      });
    }

    buttons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        buttons.forEach(function (b) { b.classList.remove('active'); });
        btn.classList.add('active');
        apply(btn.dataset.filter);
        history.replaceState(null, '', btn.dataset.filter === 'all' ? location.pathname : '#' + btn.dataset.filter);
      });
    });

    // Deep link support: products.html#pashmina
    var hash = location.hash.replace('#', '');
    if (hash) {
      var match = document.querySelector('.filter-btn[data-filter="' + hash + '"]');
      if (match) match.click();
    }
  }

  /* ---------------- FAQ accordion ---------------- */
  function initAccordion() {
    var btns = document.querySelectorAll('.acc__btn');
    if (!btns.length) return;

    btns.forEach(function (btn) {
      var panel = btn.nextElementSibling;
      btn.addEventListener('click', function () {
        var isOpen = btn.getAttribute('aria-expanded') === 'true';

        // close siblings within the same accordion
        btn.closest('.acc').querySelectorAll('.acc__btn').forEach(function (other) {
          other.setAttribute('aria-expanded', 'false');
          other.nextElementSibling.style.maxHeight = null;
        });

        if (!isOpen) {
          btn.setAttribute('aria-expanded', 'true');
          panel.style.maxHeight = panel.scrollHeight + 'px';
        }
      });
    });
  }

  /* ---------------- Lightbox ---------------- */
  function initLightbox() {
    var triggers = document.querySelectorAll('[data-lightbox]');
    if (!triggers.length) return;

    var box = document.createElement('div');
    box.className = 'lightbox';
    box.innerHTML =
      '<button class="lightbox__close" aria-label="Close">&times;</button>' +
      '<img alt=""><p class="lightbox__cap"></p>';
    document.body.appendChild(box);

    var img = box.querySelector('img');
    var cap = box.querySelector('.lightbox__cap');

    function open(src, caption) {
      img.src = src;
      img.alt = caption || '';
      cap.textContent = caption || '';
      box.classList.add('open');
      document.body.classList.add('nav-open');
    }
    function close() {
      box.classList.remove('open');
      document.body.classList.remove('nav-open');
    }

    triggers.forEach(function (t) {
      t.addEventListener('click', function () {
        var source = t.querySelector('img');
        open(t.dataset.lightbox || (source && source.src), t.dataset.caption || (source && source.alt));
      });
    });

    box.addEventListener('click', function (e) {
      if (e.target === box || e.target.classList.contains('lightbox__close')) close();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
  }

  /* ---------------- Contact form (front-end validation) ---------------- */
  function initForm() {
    var form = document.querySelector('.form');
    if (!form) return;
    var success = form.querySelector('.form-success');

    function setInvalid(field, invalid) {
      field.classList.toggle('invalid', invalid);
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;

      form.querySelectorAll('.field').forEach(function (field) {
        var input = field.querySelector('input, textarea, select');
        if (!input || !input.hasAttribute('required')) return;
        var value = input.value.trim();
        var bad = !value;
        if (!bad && input.type === 'email') {
          bad = !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value);
        }
        setInvalid(field, bad);
        if (bad) ok = false;
      });

      if (!ok) {
        var firstBad = form.querySelector('.field.invalid input, .field.invalid textarea, .field.invalid select');
        if (firstBad) firstBad.focus();
        return;
      }

      // No backend on a static site — hand off to email client and confirm on screen.
      if (success) {
        success.classList.add('show');
        success.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
      form.reset();
      setTimeout(function () { if (success) success.classList.remove('show'); }, 8000);
    });

    form.querySelectorAll('input, textarea, select').forEach(function (input) {
      input.addEventListener('input', function () {
        var field = input.closest('.field');
        if (field && field.classList.contains('invalid')) setInvalid(field, false);
      });
    });
  }

  /* ---------------- Back to top ---------------- */
  function initToTop() {
    var btn = document.querySelector('.to-top');
    if (!btn) return;
    window.addEventListener('scroll', function () {
      btn.classList.toggle('show', window.scrollY > 500);
    }, { passive: true });
    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ---------------- Footer year ---------------- */
  function initYear() {
    document.querySelectorAll('[data-year]').forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }
})();
