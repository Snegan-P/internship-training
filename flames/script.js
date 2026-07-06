async function calculate() {
    let name1 = document.getElementById("name1").value;
    let name2 = document.getElementById("name2").value;

    let response = await fetch("http://127.0.0.1:8000/calculate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name1, name2 })
    });

    let data = await response.json();

    document.getElementById("result").innerText = data.result;
}