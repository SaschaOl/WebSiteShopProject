const button_list = document.querySelectorAll(".purchase-button")
const basket = document.querySelector(".basket p")

// Adding functionality to all "buy" buttons:
// Adding the product id to the cookie files 
for (let button_id = 0; button_id < button_list.length; button_id++) {
    let button = button_list[button_id]
    button.addEventListener('click', function () {
        if (document.cookie != "") {
            let product_id = document.cookie.split("=")[1]
            let product = product_id + " " + button.id
            document.cookie = `product = ${product}; path = /`
        }
        else {
            document.cookie = `product = ${button.id}; path = /`
        }
        window.location.reload()
    })
}


