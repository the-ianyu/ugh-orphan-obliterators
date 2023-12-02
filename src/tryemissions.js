function calculateEmissionAndPrice() {
    const smallCarEmissions = 0.0001386; // kg CO2 per kilometer
    const mediumCarEmissions = 0.0001848; // kg CO2 per kilometer
    const largeCarEmissions = 0.000231; // kg CO2 per kilometer (7 seater cars)
    const basePrice = 27;
    const farPrice = 93.5;
  
    const carType = document.getElementById("carType").value.toLowerCase();
    let carEmissions;
  
    if (carType === "s") {
      carEmissions = smallCarEmissions;
    } else if (carType === "m") {
      carEmissions = mediumCarEmissions;
    } else if (carType === "e") {
      carEmissions = 0;
    } else {
      carEmissions = largeCarEmissions;
    }
  
    const distanceInput = document.getElementById("distance");
    const distance = parseFloat(distanceInput.value);
  
    const trafficInput = document.getElementById("traffic");
    let traffic = parseFloat(trafficInput.value);
  
    if (isNaN(traffic)) {
      traffic = 0;
    } else {
      traffic = Math.round(traffic);
    }
  
    if (!isNaN(distance)) {
      let emissionLevels;
  
      if (carEmissions === 0) {
        emissionLevels = 0;
      } else {
        const distanceInMeters = distance * 1000;
        emissionLevels = carEmissions * distanceInMeters;
        emissionLevels = Math.round(emissionLevels * 100) / 100;
      }
  
      let price;
  
      if (distance > 9) {
        price = farPrice + (((distance / 0.2) - 45) * 1.3);
      } else if (distance < 9 && distance > 2.199) {
        price = basePrice + (((distance - 2) / 0.2) * 1.9);
      } else if (distance <= 2.2) {
        price = basePrice;
      } else {
        price = farPrice;
      }
  
      const trafficMoney = traffic * 1.5;
      price += trafficMoney;
      price = Math.round(price * 100) / 100;
  
      const result = document.getElementById("result");
      result.innerHTML = `<p>${emissionLevels}kg of CO<sub>2</sub> were emitted from your journey.</p>
                          <p>Price: $${price.toFixed(2)}HKD</p>`;
    } else {
      const result = document.getElementById("result");
      result.textContent = "Invalid input for the distance. Please input a valid number.";
    }
  }
  
  calculateEmissionAndPrice();