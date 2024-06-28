let product_cookies = document.cookie.split("=")[1].split(" ")

// Increasing product amount values by iterating through the ids 
for (let cookies_id = 0; cookies_id < product_cookies.length; cookies_id++) {
    let product_id = product_cookies[cookies_id]
    let product_div = document.getElementById(`${product_id}`)
    let count = product_div.querySelector(".text")
    count.innerHTML = Number(count.innerHTML) + 1
}

const list_div = document.querySelectorAll(".product")
const final_price = document.querySelector(".final-price")

let price_count = 0

// Iterating though products and counting the total price
for (let div_id = 0; div_id < list_div.length; div_id++) {
    let div = list_div[div_id]

    price_count += +div.querySelector(".price").innerHTML * +div.querySelector(".text").innerHTML
}

final_price.innerHTML = `${price_count}`
