function click_animal_image(num) {
    $(".animal").val(num).prop("selected", true);
}

function click_color_image(num) {
    $("select#id_color_code").val(num).prop("selected", true);
}



$(document).ready(function () {
    $('body').on('click','img.animal', function(){
        var num = $(this).attr('id');
        click_animal_image(num);
    });

    $('label.color').on('click', function(){
        var num = $(this).attr('id');
        console.log(num);
        click_color_image(num);
    });
});
