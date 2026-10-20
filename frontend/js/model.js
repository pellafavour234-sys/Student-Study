const API_URL = "http://127.0.0.1:5000";


async function loadModel() {

    try {

        const response =
            await fetch(
                `${API_URL}/model-info`
            );


        const data =
            await response.json();


        document.getElementById(
            "model-name"
        ).textContent =
            data.model_type;


        const features =
            document.getElementById(
                "features"
            );


        features.innerHTML = "";


        data.features.forEach(
            (feature, index) => {

                const div =
                    document.createElement(
                        "div"
                    );


                div.style.padding =
                    "12px 0";

                div.style.borderBottom =
                    "1px solid #edf0f5";


                div.innerHTML = `
                    <strong>
                        ${index + 1}.
                    </strong>
                    ${feature}
                `;


                features.appendChild(div);

            }
        );


        loadImportance();


    } catch (error) {

        console.error(
            "Model error:",
            error
        );

    }

}


async function loadImportance() {

    const container =
        document.getElementById(
            "importance"
        );


    try {

        const response =
            await fetch(
                `${API_URL}/feature-importance`
            );


        const data =
            await response.json();


        if (!response.ok) {

            container.innerHTML =
                `<p>${data.error}</p>`;

            return;

        }


        container.innerHTML = "";


        Object.entries(
            data.feature_importance
        ).forEach(
            ([feature, value]) => {

                const percentage =
                    value * 100;


                const wrapper =
                    document.createElement(
                        "div"
                    );


                wrapper.style.marginBottom =
                    "18px";


                wrapper.innerHTML = `

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-bottom:7px;
                        font-size:13px;
                    ">

                        <strong>
                            ${feature}
                        </strong>

                        <span>
                            ${percentage.toFixed(1)}%
                        </span>

                    </div>

                    <div class="progress">

                        <div
                            class="progress-bar"
                            style="width:${percentage}%"
                        >
                        </div>

                    </div>

                `;


                container.appendChild(
                    wrapper
                );

            }
        );


    } catch (error) {

        container.innerHTML =
            "<p>Unable to load feature importance.</p>";

    }

}


loadModel();