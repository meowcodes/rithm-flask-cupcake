$(document).ready( function() {
    const BASE_URL = "";
    const $picList = $("#pic_list");

    $("#new_cupcake_form").on("submit", async function(evt) {
        evt.preventDefault();

        let newCupcake = {
            flavor: $("#flavor").val(),
            size: $("#size").val(),
            rating: $("#rating").val(),
            image: $("#image").val() || null
        };

        let response = await $.ajax({
            method: "POST",
            url: `${BASE_URL}/cupcakes`,
            contentType: "application/json",
            data: JSON.stringify(newCupcake)
        });

        $picList.append(
        `<div>
            <img src="${ response.response.image }">
            <p>Flavor: ${ response.response.flavor }</p>
            <p>Size: ${ response.response.size }</p>
            <p>Rating: ${ response.response.rating }</p>
        </div>`);


    });
});

