$(document).ready(function(){
    $('.social-media-post').each(function(element){
        let postId = this.id
        console.log(this.id)
        $.ajax({
            url: `check_views/${postId}`,
            type: 'get',
            dataType: 'json',
            success: function(response){
                console.log('success');
            }
        });
    });
});