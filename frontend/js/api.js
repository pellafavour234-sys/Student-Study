const API_URL = "http://127.0.0.1:5000";


/* =========================
   API REQUEST
========================= */

async function apiRequest(endpoint, options = {}) {

    try {

        const response = await fetch(
            `${API_URL}${endpoint}`,
            {
                ...options,

                headers: {
                    "Content-Type": "application/json",
                    ...(options.headers || {})
                }
            }
        );


        const text = await response.text();

        let data;

        try {
            data = JSON.parse(text);
        } catch {
            data = {
                error: text || "Invalid response from server."
            };
        }


        if (!response.ok) {

            throw new Error(
                data.error ||
                `Server error: ${response.status}`
            );

        }


        return data;

    } catch (error) {

        console.error(
            "API REQUEST ERROR:",
            error
        );

        throw error;

    }

}


/* =========================
   API STATUS
========================= */

async function checkAPI() {

    const status =
        document.getElementById("api-status");

    if (!status) return;


    try {

        const data =
            await apiRequest("/health");


        if (data.status === "healthy") {

            status.textContent =
                "🟢 AI API Online";

            status.style.background =
                "#ecfdf3";

            status.style.color =
                "#15803d";

        }

    } catch (error) {

        status.textContent =
            "🔴 AI API Offline";

        status.style.background =
            "#fef2f2";

        status.style.color =
            "#dc2626";

    }

}


checkAPI();


/* =========================
   MOBILE MENU
========================= */

const menuButton =
    document.getElementById("menu-button");

const sidebar =
    document.querySelector(".sidebar");

const overlay =
    document.getElementById("sidebar-overlay");


function openSidebar() {

    if (!sidebar) return;

    sidebar.classList.add("open");

}


function closeSidebar() {

    if (!sidebar) return;

    sidebar.classList.remove("open");

}


if (menuButton) {

    menuButton.addEventListener(
        "click",
        (event) => {

            event.stopPropagation();

            if (
                sidebar.classList.contains("open")
            ) {

                closeSidebar();

            } else {

                openSidebar();

            }

        }
    );

}


/* CLOSE WHEN OVERLAY IS CLICKED */

if (overlay) {

    overlay.addEventListener(
        "click",
        closeSidebar
    );

}


/* CLOSE AFTER NAVIGATION */

const navigationLinks =
    document.querySelectorAll(
        ".sidebar nav a"
    );


navigationLinks.forEach(link => {

    link.addEventListener(
        "click",
        () => {

            if (window.innerWidth <= 800) {

                closeSidebar();

            }

        }
    );

});


/* =========================
   DARK MODE
========================= */

const themeButton =
    document.getElementById("theme-button");


function applyTheme() {

    const theme =
        localStorage.getItem(
            "studentAI-theme"
        ) || "light";


    document.body.classList.toggle(
        "dark",
        theme === "dark"
    );


    if (themeButton) {

        themeButton.textContent =
            theme === "dark"
                ? "☀️ Light Mode"
                : "🌙 Dark Mode";

    }

}


applyTheme();


if (themeButton) {

    themeButton.addEventListener(
        "click",
        () => {

            const isDark =
                document.body.classList.contains(
                    "dark"
                );


            const newTheme =
                isDark
                    ? "light"
                    : "dark";


            localStorage.setItem(
                "studentAI-theme",
                newTheme
            );


            applyTheme();


            /*
             * Tell the iframe to reload so
             * its theme.js can read localStorage.
             */

            const iframe =
                document.querySelector(
                    ".content-frame"
                );


            if (iframe) {

                iframe.contentWindow.location.reload();

            }

        }
    );

}