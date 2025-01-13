/*!
    * Start Bootstrap - SB Admin v7.0.7 (https://startbootstrap.com/template/sb-admin)
    * Copyright 2013-2023 Start Bootstrap
    * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    // 
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Toggle the side navigation
    const sidebarToggle = document.body.querySelector('#sidebarToggle');
    if (sidebarToggle) {
        // Uncomment Below to persist sidebar toggle between refreshes
        // if (localStorage.getItem('sb|sidebar-toggle') === 'true') {
        //     document.body.classList.toggle('sb-sidenav-toggled');
        // }
        sidebarToggle.addEventListener('click', event => {
            event.preventDefault();
            document.body.classList.toggle('sb-sidenav-toggled');
            localStorage.setItem('sb|sidebar-toggle', document.body.classList.contains('sb-sidenav-toggled'));
        });
    }

});

document.addEventListener("DOMContentLoaded", () => {
    const dropdowns = document.querySelectorAll(".dropdown");

    dropdowns.forEach((dropdown) => {
        const button = dropdown.querySelector(".dropdown-btn");

        button.addEventListener("click", () => {
            // 모든 드롭다운을 닫기
            dropdowns.forEach((d) => d.classList.remove("open"));

            // 현재 드롭다운 열기
            if (!dropdown.classList.contains("open")) {
                dropdown.classList.add("open");
            }
        });
    });

    // 페이지 다른 곳 클릭 시 드롭다운 닫기
    document.addEventListener("click", (event) => {
        if (!event.target.closest(".dropdown")) {
            dropdowns.forEach((dropdown) => dropdown.classList.remove("open"));
        }
    });
});
