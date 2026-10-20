const API_URL = "http://127.0.0.1:5000";


async function loadAnalytics() {

    try {

        const response =
            await fetch(
                `${API_URL}/analytics`
            );


        const data =
            await response.json();


        document.getElementById("total")
            .textContent =
            data.total_predictions;


        document.getElementById("average")
            .textContent =
            data.average_score;


        document.getElementById("highest")
            .textContent =
            data.highest_score;


        document.getElementById("lowest")
            .textContent =
            data.lowest_score;


        document.getElementById("average-bar")
            .style.width =
            `${Math.min(
                data.average_score,
                100
            )}%`;


    } catch (error) {

        console.error(
            "Analytics error:",
            error
        );

    }

}


loadAnalytics();