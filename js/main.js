// Petites interactions du site — volontairement léger, sans dépendance.
(function () {
  // 1) Menu mobile : ouvre / ferme la navigation.
  var btn = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (btn && nav) {
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
  }

  // 2) Adresses e-mail protégées des robots : on reconstruit le lien à la volée.
  //    L'adresse complète n'apparaît jamais en clair dans le code HTML.
  document.querySelectorAll(".contact-mail").forEach(function (el) {
    var user = el.getAttribute("data-user");
    var domain = el.getAttribute("data-domain");
    if (!user || !domain) return;
    var addr = user + "@" + domain;
    var subject = el.getAttribute("data-subject");
    el.textContent = addr;
    el.setAttribute("href", "mailto:" + addr + (subject ? "?subject=" + encodeURIComponent(subject) : ""));
    el.removeAttribute("data-user");
    el.removeAttribute("data-domain");
  });

  // 3) Année courante dans le pied de page.
  document.querySelectorAll(".js-annee").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
