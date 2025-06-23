$(document).ready(function(){
    $(".icon-like").each(function(element){
        $(this).on('click', function(){
            let id = this.id;
            let classObject = $(this).attr("class").split(' ')[2]
            console.log(classObject)
            $.ajax({
                url: id,
                type: "get",
                success: function(){
                    let likes = $(`#likesPost-${classObject}`);
                    console.log(likes)
                    let updatedLikes = Number(likes.text()) + 1
                    likes.text(updatedLikes)
                }
            })
        })

    })
});