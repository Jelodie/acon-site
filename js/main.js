// Interactions du site d'Acon — léger, sans dépendance externe.
(function () {
  "use strict";

  // 1) Menu mobile : ouvre / ferme la navigation.
  var btn = document.querySelector(".nav-toggle");
  var nav = document.getElementById("nav");
  if (btn && nav) {
    btn.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        nav.classList.remove("open");
        btn.setAttribute("aria-expanded", "false");
      }
    });
  }

  // 2) Année courante dans le pied de page.
  document.querySelectorAll(".js-annee").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  // 3) Widget « Aujourd'hui à Acon » : date, saint du jour, météo en direct.
  var today = document.getElementById("today");
  if (today) {
    var now = new Date();
    var jours = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];
    var mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
                "août", "septembre", "octobre", "novembre", "décembre"];
    var elJour = today.querySelector(".jour");
    var elSaint = today.querySelector(".saint");
    if (elJour) {
      elJour.textContent = jours[now.getDay()] + " " + now.getDate() + " " + mois[now.getMonth()];
    }
    // Saint du jour (données locales dans js/saints.js)
    if (elSaint && window.SAINTS) {
      var m = window.SAINTS[now.getMonth()];
      var noms = m ? m.split(";") : [];
      var s = noms[now.getDate() - 1];
      elSaint.textContent = s ? "Nous fêtons les " + s : "";
    }
    // Météo en direct (Open-Meteo, sans clé d'API) pour les coordonnées d'Acon
    var elIco = today.querySelector(".meteo .ico");
    var elTemp = today.querySelector(".meteo .temp");
    var elDesc = today.querySelector(".meteo .desc");
    var url = "https://api.open-meteo.com/v1/forecast?latitude=48.783&longitude=1.169" +
              "&current=temperature_2m,weather_code&timezone=Europe%2FParis";
    fetch(url).then(function (r) { return r.json(); }).then(function (d) {
      if (!d.current) throw new Error("no data");
      var code = d.current.weather_code;
      var t = Math.round(d.current.temperature_2m);
      var w = meteoLabel(code);
      if (elIco) elIco.textContent = w.ico;
      if (elTemp) elTemp.textContent = t + "°C";
      if (elDesc) elDesc.textContent = w.desc;
    }).catch(function () {
      var meteo = today.querySelector(".meteo");
      if (meteo) meteo.style.display = "none";
    });
  }

  function meteoLabel(c) {
    if (c === 0) return { ico: "☀️", desc: "Ensoleillé" };
    if (c === 1 || c === 2) return { ico: "🌤️", desc: "Éclaircies" };
    if (c === 3) return { ico: "☁️", desc: "Couvert" };
    if (c === 45 || c === 48) return { ico: "🌫️", desc: "Brouillard" };
    if (c >= 51 && c <= 57) return { ico: "🌦️", desc: "Bruine" };
    if (c >= 61 && c <= 67) return { ico: "🌧️", desc: "Pluie" };
    if (c >= 71 && c <= 77) return { ico: "🌨️", desc: "Neige" };
    if (c >= 80 && c <= 82) return { ico: "🌦️", desc: "Averses" };
    if (c === 85 || c === 86) return { ico: "🌨️", desc: "Averses de neige" };
    if (c >= 95) return { ico: "⛈️", desc: "Orage" };
    return { ico: "🌡️", desc: "" };
  }

  // 4) Formulaire de contact (envoi sans recharger la page).
  var form = document.getElementById("form-contact");
  if (form) {
    var msg = document.getElementById("form-msg");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (form.action.indexOf("VOTRE_ID") !== -1) {
        show("Le formulaire sera actif très prochainement. En attendant, merci de votre patience.", "err");
        return;
      }
      var btnEnvoi = form.querySelector("button");
      if (btnEnvoi) { btnEnvoi.disabled = true; btnEnvoi.textContent = "Envoi…"; }
      fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { "Accept": "application/json" }
      }).then(function (r) {
        if (r.ok) {
          form.reset();
          show("Merci ! Votre message a bien été envoyé.", "ok");
        } else {
          show("Une erreur est survenue. Réessayez dans un instant.", "err");
        }
      }).catch(function () {
        show("Une erreur est survenue. Réessayez dans un instant.", "err");
      }).finally(function () {
        if (btnEnvoi) { btnEnvoi.disabled = false; btnEnvoi.textContent = "Envoyer"; }
      });
    });
    function show(text, cls) { if (msg) { msg.textContent = text; msg.className = cls; } }
  }
})();
