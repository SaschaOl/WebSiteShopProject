if (document.cookie.split("=")[1] != undefined) {
    var product_cookies = document.cookie.split("=")[1].split(" ")
} 
else {
    var product_cookies = ""
}

let product_count = 0

// Checking if the cookie files are not empty
if (product_cookies.length > 0 && product_cookies[0] != "") {
    // Increasing product amount values by iterating through the ids
    for (let cookies_id = 0; cookies_id < product_cookies.length; cookies_id++) {
        let product_id = product_cookies[cookies_id]
        let product_div = document.getElementById(`${product_id}`)
        let count = product_div.querySelector(".text")
        count.innerHTML = Number(count.innerHTML) + 1
        product_count++
    }
}

document.querySelector(".big_button").addEventListener("click", function() {
    document.querySelector(".form_checkout").style.display = "block"
})

const list_div = document.querySelectorAll(".product")
const full_price = document.querySelector(".full-price")
const final_price = document.querySelector(".final-price")
const discount = document.querySelector(".discount")

let full_price_count = 0
let price_count = 0

// Checking if the cookie files are not empty
if (product_cookies.length > 0 && product_cookies[0] != "") {
    // Iterating though products to count the prices and add eventListeners
    for (let div_id = 0; div_id < list_div.length; div_id++) {
        let div = list_div[div_id]

        full_price_count += +div.querySelector(".var").innerHTML * +div.querySelector(".text").innerHTML 
        price_count += +div.querySelector(".price").innerHTML * +div.querySelector(".text").innerHTML
        

        let plus = div.querySelector(".plus")
        let minus = div.querySelector(".minus")

        // Adding the functionality to the add product button:
        // Adding one more of the pruduct
        plus.addEventListener("click", function(){
            console.log(div_id)
            let data_cookie = document.cookie.split("=")[1]
            document.cookie = `product = ${data_cookie} ${div.id}; path = /`
            
            window.location.reload()   
            }
        )
        
        // Adding the functionality to the add product button:
        // Making one less of the product
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
}

// Grammaticaly conjugates the word for the product amount
function product_amount(amount) {
    if (amount == 1) {
        return "товар"
    }
    else if (amount >= 2 && amount <= 4) {
        return "товари"
    }
    else{
        return "товарiв"
    }

}

// Setting the full price
full_price.querySelector(".price-desc").innerHTML = `${product_count} ${product_amount(amount = product_count)} на суму`
full_price.querySelector(".price-count").innerHTML = `${full_price_count}`

// Checking if the cookie files are not empty
if (product_cookies.length > 0 && product_cookies[0] != "") {
    // Setting the discount percentage
    discount.querySelector(".price-discount").innerHTML = `${Math.round((1 - (price_count / full_price_count).toFixed(2)) * 100)}%`
}
// Setting the discount
discount.querySelector(".price-count").innerHTML = full_price_count - price_count

// Setting the final price
final_price.querySelector(".price-desc").innerHTML = `Загальна сума`
final_price.querySelector(".price-count").innerHTML = `${price_count}`

// Setting the price and products values for placeholders in the form
document.querySelector(".price-input").value = price_count
document.querySelector(".product-input").value = document.cookie.split("=")[1]

