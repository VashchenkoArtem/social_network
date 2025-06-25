$(document).ready(function(){
    $(".button-delete").each(function(){
        $(this).on('click', function(){
            let url = $(this)
            $.ajax({
                url: url.attr('id'),
                type: "get",
                success: function(){
                    let userId = url.attr('id').split("/")[3];
                    console.log(userId)
                    if ($(`#card-request-${userId}`)){
                        let card = $(`#card-request-${userId}`);
                        card.toggleClass("hidden");
                    }
                }
            })
        })
    })
    $(".button-delete-recommended").each(function(){
        $(this).on('click', function(){
            let url = $(this)
            $.ajax({
                url: url.attr('id'),
                type: "get",
                success: function(){
                    let userId = url.attr('id').split("/")[3];
                    console.log(userId)
                    if ($(`#card-recommended-${userId}`)){
                        let card = $(`#card-recommended-${userId}`);
                        card.toggleClass("hidden");
                    }
                }
            })
        })
    })
    $(".button-delete-friend").each(function(){
        $(this).on('click', function(){
            let url = $(this)
            $.ajax({
                url: url.attr('id'),
                type: "get",
                success: function(){
                    let userId = url.attr('id').split("/")[3];
                    console.log(userId)
                    if ($(`#card-friend-${userId}`)){
                        let card = $(`#card-friend-${userId}`);
                        console.log(card)
                        card.toggleClass("hidden");
                    }
                }
            })
        })
    })
    $(".add-button").each(function(){
        $(this).on('click', function(){
            let url = $(this)
            $.ajax({
                url: url.attr('id'),
                type: "get",
                success: function(){
                    $(".confirm-delete-div").toggleClass('hidden')
                }
            })
        })
    })
    $(".button-confirm-recomended").each(function(){
        $(this).on('click', function(){
            let url = $(this)
            $.ajax({
                url: url.attr('id'),
                type: "get",
                success: function(){
                    let userId = url.attr('id').split("/")[3];
                    console.log(userId)
                    if ($(`#card-recommended-${userId}`)){
                        let card = $(`#card-recommended-${userId}`);
                        card.toggleClass("hidden");
                    }
                }
            })
        })
    })
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
                    let updatedLikes = Number(likes.text()) + 1
                    likes.text(updatedLikes)
                }
            })
        })
    });
})

