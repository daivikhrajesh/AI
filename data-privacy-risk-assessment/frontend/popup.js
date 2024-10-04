document.getElementById("assessButton").addEventListener("click", async () => {
  const data = document.getElementById("dataInput").value;

  const response = await fetch("http://localhost:5000/assess", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ data }),
  });

  const result = await response.json();
  document.getElementById("result").innerText = JSON.stringify(result);
});
