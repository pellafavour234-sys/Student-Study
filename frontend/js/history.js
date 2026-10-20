const API_URL = "http://127.0.0.1:5000";


async function loadHistory() {

    const body =
        document.getElementById(
            "history-body"
        );


    try {

        const response =
            await fetch(
                `${API_URL}/history`
            );


        const data =
            await response.json();


        body.innerHTML = "";


        if (
            !data.history ||
            data.history.length === 0
        ) {

            body.innerHTML = `

                <tr>

                    <td
                        colspan="6"
                        style="text-align:center;"
                    >

                        No predictions yet.

                    </td>

                </tr>

            `;

            return;

        }


        data.history.forEach(
            record => {

                const row =
                    document.createElement(
                        "tr"
                    );


                const date =
                    new Date(
                        record.created_at
                    ).toLocaleString();


                row.innerHTML = `

                    <td>
                        ${date}
                    </td>

                    <td>
                        ${record.study_hours}
                    </td>

                    <td>
                        ${record.attendance}%
                    </td>

                    <td>
                        ${record.previous_score}
                    </td>

                    <td>
                        <strong>
                            ${record.predicted_score}
                        </strong>
                    </td>

                    <td>
                        ${record.performance}
                    </td>

                `;


                body.appendChild(row);

            }
        );


    } catch (error) {

        body.innerHTML = `

            <tr>

                <td colspan="6">

                    Unable to load prediction history.

                </td>

            </tr>

        `;

        console.error(error);

    }

}


loadHistory();