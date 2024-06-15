document.getElementById('industryForm').addEventListener('submit', function(event) {
    const industry = document.getElementById('industry').value;
    const segment = document.getElementById('segment').value;
    const productType = document.getElementById('productType').value;
    const quantity = document.getElementById('quantity').value;
    const productionDays = document.getElementById('productionDays').value;

    if (!industry || !segment || !productType || !quantity || !productionDays) {
        event.preventDefault();
        alert('Por favor, preencha todos os campos.');
    }
});