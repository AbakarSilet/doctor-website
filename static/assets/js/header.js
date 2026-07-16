const langBtn = document.getElementById('lang-btn');
  const langDropdown = document.getElementById('lang-dropdown');

  langBtn.addEventListener('click', () => {
    langDropdown.style.display = langDropdown.style.display === 'block' ? 'none' : 'block';
  });

  // Clic en dehors pour fermer
  document.addEventListener('click', (e) => {
    if (!langBtn.contains(e.target) && !langDropdown.contains(e.target)) {
      langDropdown.style.display = 'none';
    }
  });

  /* ===== Dropdown Services =====
     - Desktop (>= 1150px) : ouverture au survol de la souris, gérée en CSS pur (:hover).
       Aucun JS n'est nécessaire pour cette taille d'écran.
     - Mobile / tablette (< 1150px) : pas de souris, donc ouverture au clic. */
  const servicesBtn = document.getElementById('services-btn');
  const servicesDropdown = document.getElementById('services-dropdown');

  if (servicesBtn && servicesDropdown) {
    servicesBtn.addEventListener('click', (e) => {
      if (window.innerWidth < 1150) {
        e.preventDefault();
        servicesDropdown.classList.toggle('show-dropdown');
      }
    });

    // Clic en dehors pour fermer (mobile)
    document.addEventListener('click', (e) => {
      if (!servicesBtn.contains(e.target) && !servicesDropdown.contains(e.target)) {
        servicesDropdown.classList.remove('show-dropdown');
      }
    });

    // Si l'écran repasse en desktop (rotation, redimensionnement), on nettoie l'état mobile
    window.addEventListener('resize', () => {
      if (window.innerWidth >= 1150) {
        servicesDropdown.classList.remove('show-dropdown');
      }
    });

    // Fermer le dropdown ET le menu mobile plein écran quand on choisit un service.
    // Nécessaire car un lien vers une ancre de la même page (ex: on est déjà sur
    // services.html et on clique un autre service) ne déclenche pas de rechargement
    // de page, donc rien d'autre ne referme le menu automatiquement.
    const navMenu = document.getElementById('nav-menu');
    const serviceLinks = servicesDropdown.querySelectorAll('a');

    serviceLinks.forEach((link) => {
      link.addEventListener('click', () => {
        servicesDropdown.classList.remove('show-dropdown');
        if (navMenu) {
          navMenu.classList.remove('show-menu');
        }
      });
    });
  }