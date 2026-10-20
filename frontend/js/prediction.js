const API_URL = "http://127.0.0.1:5000";


document.addEventListener("DOMContentLoaded", () => {

    const form = document.getElementById("prediction-form");

    const button =
        document.getElementById("prediction-button");


    if (!form) {
        console.error("Prediction form not found.");
        return;
    }


    form.addEventListener("submit", async (event) => {

        // VERY IMPORTANT:
        // Stop the browser from reloading the page
        event.preventDefault();


        /* =========================
           GET INPUT VALUES
        ========================= */

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


        /* =========================
           CHECK EMPTY VALUES
        ========================= */

        if (
            data.study_hours === "" ||
            data.attendance === "" ||
            data.previous_score === "" ||
            data.assignments_completed === "" ||
            data.sleep_hours === ""
        ) {

            alert("Please fill in all the fields.");

            return;
        }


        /* =========================
           CONVERT TO NUMBERS
        ========================= */

        const studyHours =
            Number(data.study_hours);

        const attendance =
            Number(data.attendance);

        const previousScore =
            Number(data.previous_score);

        const assignments =
            Number(data.assignments_completed);

        const sleepHours =
            Number(data.sleep_hours);


        /* =========================
           VALIDATE RANGES
        ========================= */

        if (
            studyHours < 0 ||
            studyHours > 24
        ) {

            alert(
                "Study Hours must be between 0 and 24."
            );

            return;
        }


        if (
            attendance < 0 ||
            attendance > 100
        ) {

            alert(
                "Attendance must be between 0 and 100%."
            );

            return;
        }


        if (
            previousScore < 0 ||
            previousScore > 100
        ) {

            alert(
                "Previous Score must be between 0 and 100."
            );

            return;
        }


        if (
            assignments < 0 ||
            assignments > 100
        ) {

            alert(
                "Assignments Completed must be between 0 and 100."
            );

            return;
        }


        if (
            sleepHours < 0 ||
            sleepHours > 24
        ) {

            alert(
                "Sleep Hours must be between 0 and 24."
            );

            return;
        }


        /* =========================
           SHOW LOADING
        ========================= */

        if (button) {

            button.disabled = true;

            button.textContent =
                "⏳ Generating Prediction...";

        }


        /* =========================
           SEND TO FLASK
        ========================= */

        try {

            const response = await fetch(
                `${API_URL}/predict`,
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        study_hours:
                            studyHours,

                        attendance:
                            attendance,

                        previous_score:
                            previousScore,

                        assignments_completed:
                            assignments,

                        sleep_hours:
                            sleepHours

                    })

                }
            );


            const result =
                await response.json();


            console.log(
                "Prediction response:",
                result
            );


            /* =========================
               HANDLE BACKEND ERROR
            ========================= */

            if (!response.ok) {

                throw new Error(
                    result.error ||
                    "The prediction request failed."
                );

            }


            /* =========================
               GET PREDICTION
            ========================= */

            const prediction =
                result.prediction;


            if (!prediction) {

                throw new Error(
                    "The server did not return a prediction."
                );

            }


            /* =========================
               DISPLAY SCORE
            ========================= */

            const scoreElement =
                document.getElementById(
                    "prediction-score"
                );


            const categoryElement =
                document.getElementById(
                    "prediction-category"
                );


            if (scoreElement) {

                scoreElement.textContent =
                    prediction.predicted_score;

            }


            if (categoryElement) {

                categoryElement.textContent =
                    prediction.performance;

            }


            /* =========================
               DISPLAY RECOMMENDATIONS
            ========================= */

            const recommendationBox =
                document.getElementById(
                    "recommendations"
                );


            if (
                recommendationBox &&
                result.recommendations
            ) {

                recommendationBox.innerHTML = "";


                result.recommendations.forEach(
                    recommendation => {

                        const item =
                            document.createElement(
                                "div"
                            );


                        item.className =
                            "recommendation";


                        item.innerHTML = `

                            <strong>
                                ${recommendation.title}
                            </strong>

                            <p>
                                ${recommendation.message}
                            </p>

                        `;


                        recommendationBox.appendChild(
                            item
                        );

                    }
                );

            }


        } catch (error) {

            console.error(
                "Prediction error:",
                error
            );


            alert(
                "Prediction failed: " +
                error.message
            );


        } finally {

            /* =========================
               RESTORE BUTTON
            ========================= */

            if (button) {

                button.disabled = false;

                button.textContent =
                    "🚀 Generate Prediction";

            }

        }

    });

});