document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);
    // modal initialization
    let modals = document.querySelectorAll('.modal');
    M.Modal.init(modals);
});
