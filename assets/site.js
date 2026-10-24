// AVATAR LIVE — small progressive enhancements. Every page works without this file.
(function () {
  var doc = document.documentElement;
  doc.classList.add("js");
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Light or dark follows the system setting (site.css); there is no switch of our own.
  try { localStorage.removeItem("al-theme"); } catch (e) {}

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
    if (e.key !== "Escape") return;
    document.querySelectorAll("details.lang[open]").forEach(function (d) { d.open = false; d.querySelector("summary").focus(); });
    if (side && side.classList.contains("open")) { side.classList.remove("open"); docsBtn.setAttribute("aria-expanded", "false"); docsBtn.focus(); }
    if (menuBtn && mobile && !mobile.hidden) { menuBtn.setAttribute("aria-expanded", "false"); mobile.hidden = true; menuBtn.focus(); }
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

  // Videos: muted loops that play only while visible, each with a pause button
  // (and no autoplay at all with reduced motion: then the browser's own controls show).
  var hero = document.querySelector(".hero-video");
  if (hero && reduce) { hero.removeAttribute("autoplay"); hero.pause(); hero.controls = true; }
  var vids = document.querySelectorAll("video.lazyvideo");
  vids.forEach(function (v) { v.controls = reduce; });
  var PAUSE = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
  var PLAY = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.4-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5z"/></svg>';
  function pauseButton(v) {
    var b = document.createElement("button");
    b.type = "button"; b.className = "vid-toggle";
    function show() { var on = !v.dataset.stopped; b.innerHTML = on ? PAUSE : PLAY; b.setAttribute("aria-label", on ? v.dataset.pause : v.dataset.play); }
    b.addEventListener("click", function () {
      if (v.dataset.stopped) { delete v.dataset.stopped; var p = v.play(); if (p && p.catch) p.catch(function () {}); }
      else { v.dataset.stopped = "1"; v.pause(); }
      show();
    });
    show();
    v.parentNode.appendChild(b);
  }
  if (!reduce) {
    if (hero) pauseButton(hero);
    vids.forEach(pauseButton);
  }
  if ("IntersectionObserver" in window && !reduce) {
    var vo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        var v = en.target;
        if (en.isIntersecting && !v.dataset.stopped) { if (v.preload !== "auto") { v.preload = "auto"; } var p = v.play(); if (p && p.catch) p.catch(function () {}); }
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
