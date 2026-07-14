// Menu mobile : ouvre/ferme la navigation. Rien d'autre — le site reste volontairement simple.
(function () {
  var btn = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (!btn || !nav) return;

  btn.addEventListener("click", function () {
    var open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", open ? "true" : "false");
  });

  // Referme le menu après un clic sur un lien (mobile)
  nav.addEventListener("click", function (e) {
    if (e.target.tagName === "A") {
      nav.classList.remove("open");
      btn.setAttribute("aria-expanded", "false");
    }
  });
})();
