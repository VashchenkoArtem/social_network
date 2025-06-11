$(document).ready(function(){
    $(".button-delete").each(function(){
        $(this).on('click', function(){
            $.ajax({
                url: $(this).attr('id'),
                type: "get",
                success: function(){
                    console.log("success")
                }
            })
        })
    })
})