var bindEventCommentToggle = function(){
    $('body').on('click', 'a.pylp', function(){
        console.log('222')
        var weiboCell = $(this).closest(".blogs-cell")
        console.log('333')
        var weiboComment = weiboCell.find('.comment-div')
        console.log('111', weiboComment)
        weiboComment.slideToggle()
        return false;
    })
}



var bindEvents = function() {
    bindEventCommentToggle()
}

$(document).ready(function(){
    bindEvents()
})
