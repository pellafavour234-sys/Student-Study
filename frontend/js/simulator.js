const API_URL = "http://127.0.0.1:5000";


async function runSimulation() {

    const data = {

        study_hours:
            document.getElementById("study_hours").value,

        attendance:
            document.getElementById("attendance").value,

        previous_score:
            document.getElementById("previous_score").value,

        assignments_completed:
            document.getElementById(
                "assignments_completed"
            ).value,

        sleep_hours:
            document.getElementById("sleep_hours").value

    };


    const scoreElement =
        document.getElementById(
            "simulation-score"
        );


    const categoryElement =
        document.getElementById(
            "simulation-category"
        );


    const messageElement =
        document.getElementById(
            "simulation-message"
        );


    scoreElement.textContent = "...";


    try {

        const response =
            await fetch(
                `${API_URL}/predict`,
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify(data)

                }
            );


        const result =
            await response.json();


        if (!response.ok) {

            throw new Error(
                result.error ||
                "Simulation failed."
            );

        }


        scoreElement.textContent =
            result.prediction.predicted_score;


        categoryElement.textContent =
            result.prediction.performance;


        messageElement.textContent =
            "The model generated this result using the current simulation inputs.";


    } catch (error) {

        scoreElement.textContent = "--";

        categoryElement.textContent =
            "Error";

        messageElement.textContent =
            error.message;

    }

}