let count_basket = document.querySelector(".basket p")

// Updating the basket product count value
if (document.cookie && document.cookie.split("=")[1] != "") {
    count_basket.style.display = "block"
    for (let cookie_id = 0; cookie_id < document.cookie.split("=")[1].split(" ").length; cookie_id++) {
        count_basket.innerHTML = Number(count_basket.innerHTML) + 1
    }
} else {
    count_basket.style.display = "none"
}