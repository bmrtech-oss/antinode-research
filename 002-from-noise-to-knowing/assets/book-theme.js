(function () {
  var THEMES = [
    { id: "dark", label: "Dark", dark: true },
    { id: "solarized", label: "Solarized", dark: false },
    { id: "logseq", label: "Logseq", dark: true },
    { id: "light", label: "Light", dark: false }
  ];
  var MOON = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';
  var SUN = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';

  function index() {
    var cur = document.documentElement.getAttribute("data-theme");
    for (var i = 0; i < THEMES.length; i++) if (THEMES[i].id === cur) return i;
    return 0;
  }

  function apply(i, btn) {
    var t = THEMES[i], next = THEMES[(i + 1) % THEMES.length];
    document.documentElement.setAttribute("data-theme", t.id);
    // Keep Material's own dark/light defaults (code colours, shadows) in step.
    if (document.body) document.body.setAttribute("data-md-color-scheme", t.dark ? "slate" : "default");
    try { localStorage.setItem("antinode-theme", t.id); } catch (e) {}
    if (btn) {
      btn.innerHTML = (t.dark ? MOON : SUN) + '<span class="theme-toggle__label">' + t.label + "</span>";
      btn.title = "Theme: " + t.id + " (click for " + next.id + ")";
      btn.setAttribute("aria-label", "Theme: " + t.id + ". Switch to " + next.id);
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.createElement("button");
    btn.type = "button";
    btn.className = "theme-toggle";
    btn.addEventListener("click", function () { apply((index() + 1) % THEMES.length, btn); });
    var inner = document.querySelector(".md-header__inner");
    if (inner) {
      var search = inner.querySelector("label[for=__search]");
      inner.insertBefore(btn, search || null);
    }
    apply(index(), btn);
  });
})();

/* Shrink wide ASCII diagrams to fit narrow screens (down to a readable minimum) */
(function () {
  var MIN_PX = 6.5, MAX_WIDTH = 900;
  function fit() {
    var blocks = document.querySelectorAll(".md-typeset pre > code");
    Array.prototype.forEach.call(blocks, function (code) {
      code.style.fontSize = "";
      if (window.innerWidth > MAX_WIDTH) { return; }
      var pre = code.parentElement, avail = pre.clientWidth, need = code.scrollWidth;
      if (avail > 0 && need > avail + 1) {
        var base = parseFloat(getComputedStyle(code).fontSize);
        code.style.fontSize = Math.max(MIN_PX, Math.floor(base * avail / need * 10) / 10) + "px";
      }
    });
  }
  var timer;
  function later() { clearTimeout(timer); timer = setTimeout(fit, 120); }
  document.addEventListener("DOMContentLoaded", function () {
    fit();
    if (document.fonts && document.fonts.ready) { document.fonts.ready.then(fit); }
    window.addEventListener("load", fit);
  });
  window.addEventListener("resize", later);
  window.addEventListener("orientationchange", later);
})();