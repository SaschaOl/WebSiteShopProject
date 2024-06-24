let product_cookies = document.cookie.split("=")[1].split(" ")
let created_products = []
let product_count = 0

for (let cookies_id = 0; cookies_id < product_cookies.length; cookies_id++) {
    let product_id = product_cookies[cookies_id]
    let product_div = document.getElementById(`${product_id}`)
    let count = product_div.querySelector(".text")
    count.innerHTML = Number(count.innerHTML) + 1
    product_count++
}

document.querySelector(".big_button").addEventListener("click", function() {
    console.log(89)
    document.querySelector(".form_checkout").style.display = "block"
})

const list_div = document.querySelectorAll(".product")
const total_price = document.querySelector(".total-price")
const all_price = document.querySelector(".full-price")
const discount = document.querySelector(".discount")

let full_price = 0
let price = 0

for (let div_id = 0; div_id < list_div.length; div_id++) {
    let div = list_div[div_id]

    full_price += +div.querySelector(".var").innerHTML * +div.querySelector(".text").innerHTML
    console.log(div.querySelector(".var").innerHTML) 
    price += +div.querySelector(".price").innerHTML * +div.querySelector(".text").innerHTML
    

    let plus = div.querySelector(".plus")
    let minus = div.querySelector(".minus")

    
    plus.addEventListener("click", function(){
        console.log(div_id)
        let data_cookie = document.cookie.split("=")[1]
        document.cookie = `product = ${data_cookie} ${div.id}; path = /`
        
        window.location.reload()   
        }
    )
    

    minus.addEventListener("click", function(){
        console.log(div_id)
        let data_cookie = document.cookie.split("=")[1]
        let list_cookie = data_cookie.split(" ")
        for (let id = 0; id < list_cookie.length; id++){
            if (list_cookie[id] == div.id) {
                delete list_cookie[id] 
                console.log(list_cookie)
                break
            }   
        }
        new_cookie = ''
        for (let id = 0; id < list_cookie.length; id++){
            if (list_cookie[id] != undefined) {
                
                new_cookie = new_cookie + list_cookie[id] + " "
            }
        }
        document.cookie = `product = ${new_cookie}; path = /`
        window.location.reload()
    })



}

function product_amount(amount) {
    if (amount == 1) {
        return "товар"
    }
    else if (amount >= 2 && amount <= 4) {
        return "товари"
    }
    else if (amount >= 5){
        return "товарiв"
    }

}

total_price.querySelector(".price-desc").innerHTML = `${product_count} ${product_amount(amount = product_count)} на суму`
total_price.querySelector(".price-count").innerHTML = `${full_price}`

discount.querySelector(".price-discount").innerHTML = `${Math.round((1 - (price / full_price).toFixed(2)) * 100)}%`
discount.querySelector(".price-count").innerHTML = full_price - price

all_price.querySelector(".price-desc").innerHTML = `Загальна сума`
all_price.querySelector(".price-count").innerHTML = `${price}`


document.querySelector(".price-input").value = price
document.querySelector(".product-input").value = document.cookie.split("=")[1]

