// AVATAR LIVE — small progressive enhancements. Every page works without this file.
(function () {
  var doc = document.documentElement;
  doc.classList.add("js");
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Theme: dark by default; the choice is kept per browser.
  var themeBtn = document.querySelector("[data-theme-toggle]");
  if (themeBtn) themeBtn.addEventListener("click", function () {
    var next = doc.dataset.theme === "light" ? "dark" : "light";
    doc.dataset.theme = next;
    try { localStorage.setItem("al-theme", next); } catch (e) {}
  });

  // Header: a backdrop once the page has scrolled.
  var header = document.querySelector("[data-header]");
  function onScroll() { if (header) header.classList.toggle("scrolled", window.scrollY > 8); }
  addEventListener("scroll", onScroll, { passive: true }); onScroll();

  // Mobile navigation.
  var menuBtn = document.querySelector("[data-menu-toggle]");
  var mobile = document.getElementById("mobile-nav");
  if (menuBtn && mobile) {
    menuBtn.addEventListener("click", function () {
      var open = menuBtn.getAttribute("aria-expanded") !== "true";
      menuBtn.setAttribute("aria-expanded", String(open));
      mobile.hidden = !open;
    });
    mobile.addEventListener("click", function (e) {
      if (e.target.closest("a")) { menuBtn.setAttribute("aria-expanded", "false"); mobile.hidden = true; }
    });
  }

  // Guide contents on narrow screens.
  var docsBtn = document.querySelector("[data-docs-toggle]");
  var side = document.getElementById("docs-side");
  if (docsBtn && side) {
    docsBtn.addEventListener("click", function () {
      var open = !side.classList.contains("open");
      side.classList.toggle("open", open);
      docsBtn.setAttribute("aria-expanded", String(open));
    });
    document.addEventListener("click", function (e) {
      if (side.classList.contains("open") && !side.contains(e.target) && !docsBtn.contains(e.target)) {
        side.classList.remove("open"); docsBtn.setAttribute("aria-expanded", "false");
      }
    });
  }

  // The language menu closes on outside click and Escape.
  document.addEventListener("click", function (e) {
    document.querySelectorAll("details.lang[open]").forEach(function (d) { if (!d.contains(e.target)) d.open = false; });
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      document.querySelectorAll("details.lang[open]").forEach(function (d) { d.open = false; });
      if (side) { side.classList.remove("open"); }
    }
  });

  // Sections appear as they scroll in.
  var items = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add("in"); });
  }

  // Videos: muted loops that play only while visible (and not at all with reduced motion).
  var hero = document.querySelector(".hero-video");
  if (hero && reduce) { hero.removeAttribute("autoplay"); hero.pause(); hero.controls = true; }
  var vids = document.querySelectorAll("video.lazyvideo");
  vids.forEach(function (v) { v.controls = reduce; });
  if ("IntersectionObserver" in window && !reduce) {
    var vo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting) { if (v.preload !== "auto") { v.preload = "auto"; } var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        else v.pause();
      });
    }, { threshold: 0.25 });
    vids.forEach(function (v) { vo.observe(v); });
  }

  // The guide's "on this page" follows the reading position.
  var links = [].slice.call(document.querySelectorAll(".toc a"));
  if (links.length) {
    var heads = links.map(function (a) { return document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1))); });
    function spy() {
      var y = scrollY + 120, cur = 0;
      heads.forEach(function (h, i) { if (h && h.offsetTop <= y) cur = i; });
      links.forEach(function (a, i) { a.classList.toggle("on", i === cur); });
    }
    addEventListener("scroll", spy, { passive: true }); spy();
  }
})();
