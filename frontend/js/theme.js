/* =========================
   STUDENTAI THEME SYSTEM
========================= */

function applyPageTheme() {

    const savedTheme =
        localStorage.getItem(
            "studentAI-theme"
        );


    if (savedTheme === "dark") {

        document.body.classList.add("dark");

    } else {

        document.body.classList.remove("dark");

    }

}


applyPageTheme();