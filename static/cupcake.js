$(document).ready( function() {
    BASE_URL = ""

    $("#new_cupcake_form").on("submit", async function(evt) {
        evt.preventDefault();

        newCupcake = {
            flavor: $("#flavor").val(),
            size: $("#size").val(),
            rating: $("#rating").val(),
            image: $("#image").val()
        }

        response = await $.ajax({
            method: "POST",
            url: `${BASE_URL}/cupcakes`,
            contentType: "application/json",
            data: JSON.stringify(newCupcake)
        });

    })
})

