let edit_buttons = document.querySelectorAll(".edit")
let edit_image = document.querySelectorAll(".edit-image")

// Adding functionality to the non file edit buttons:
// Showing the form for non file values editing
for (let list_edit_button = 0; list_edit_button < edit_buttons.length; list_edit_button++) {
    edit_buttons[list_edit_button].addEventListener("click", function () {
        let form_class = document.querySelector(".modal_window")
        form_class.style.display = "flex"
        form_class.querySelector(".submit-button").value = edit_buttons[list_edit_button].id
        form_class.querySelector(".submit-button").name = "id"
        form_class.querySelector(".var").value = edit_buttons[list_edit_button].name
        }
    )
}

// Adding functionality to the image edit buttons:
// Showing the form for imgage editing
for (let list_edit_image = 0; list_edit_image < edit_image.length; list_edit_image++) {
    edit_image[list_edit_image].addEventListener("click", function(){
        let form_class = document.querySelector(".image-edit")
        form_class.style.display = "flex"
        console.log(edit_image[list_edit_image].id)
        form_class.querySelector(".submit-button").value = edit_image[list_edit_image].id


        }
    )
}
