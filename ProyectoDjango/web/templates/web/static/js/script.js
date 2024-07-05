let cart = [];
let totalPrice = 0.00;

function addToCart(productName, productPrice) {
    // Añadir producto al carrito
    cart.push({ name: productName, price: productPrice });
    // Actualizar el precio total
    totalPrice += productPrice;
    // Actualizar la interfaz de usuario
    updateCartUI();
}

function updateCartUI() {
    const cartItemsElement = document.getElementById('cart-items');
    const totalPriceElement = document.getElementById('total-price');

    // Limpiar la lista del carrito
    cartItemsElement.innerHTML = '';

    // Añadir cada producto del carrito a la lista
    cart.forEach(item => {
        const li = document.createElement('li');
        li.textContent = `${item.name} - $${item.price.toFixed(2)}`;
        cartItemsElement.appendChild(li);
    });

    // Actualizar el precio total
    totalPriceElement.textContent = totalPrice.toFixed(2);
}
/**  Este código JavaScript gestiona un carrito de compras:

Variables Globales:

cart: Un arreglo para almacenar los productos añadidos al carrito. Cada producto es un objeto con name y price.
totalPrice: Un número que representa el precio total de los productos en el carrito.
Función addToCart(productName, productPrice):

Añade un producto al arreglo cart y actualiza el totalPrice.
Llama a updateCartUI() para reflejar los cambios en la interfaz de usuario.
Función updateCartUI():

Actualiza la lista de productos en el carrito y el precio total en la interfaz de usuario.
Limpia la lista actual y la repuebla con los elementos del arreglo cart.
Actualiza el contenido del elemento con id="total-price" al totalPrice actual, formateado a dos decimales.
*/