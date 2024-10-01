document.getElementById("compare-prices").addEventListener("click", () => {
  const itemName = document.getElementById("item-name").value;

  fetch("http://localhost:5000/compare", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ item: itemName }),
  })
    .then((response) => response.json())
    .then((data) => {
      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = `
            <p>Amazon Price: ${data.amazon_price}</p>
            <p>Best Buy Price: ${data.bestbuy_price}</p>
        `;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
