fetch('http://localhost:5000/products')
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('product-list');
        data.forEach(product => {
            const item = document.createElement('li');
            item.textContent = product.name + ' - $' + product.price;
            list.appendChild(item);
        });
    });

