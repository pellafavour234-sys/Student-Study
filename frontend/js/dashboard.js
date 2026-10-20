const API_URL = "http://127.0.0.1:5000";


async function loadDashboard() {

    try {

        const response =
            await fetch(
                `${API_URL}/analytics`
            );


        const data =
            await response.json();


        document.getElementById(
            "total-predictions"
        ).textContent =
            data.total_predictions;


        document.getElementById(
            "average-score"
        ).textContent =
            data.average_score;


        document.getElementById(
            "highest-score"
        ).textContent =
            data.highest_score;


        document.getElementById(
            "lowest-score"
        ).textContent =
            data.lowest_score;


    } catch (error) {

        console.error(
            "Dashboard error:",
            error
        );

    }

}


loadDashboard();