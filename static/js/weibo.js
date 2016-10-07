var log = function() {
  console.log(arguments)
}

var weiboTemplate = function(weibo) {
    var w = weibo
    var t = `
        <div class="blogs-cell  weibo-cell" style="padding-top: 5px;">
            <img src="${ w.avatar }" class="avatar">
            <div class="right">
            <span class="">${ w.created_time }</span>
            <span class="">by: ${ w.name }</span>
            </div>
            <div class="blog-content">
                <span class="weibo-content">${ w.weibo }</span>
                <a href="#" class="right pylp" style="color: white;">评论(${ w.comments_num })</a>
            </div>

            <button class="button-blogs weibo-delete" data-id="${ w.id }">删除</button>
            <button class="button-blogs weibo-edit" data-id="${ w.id }">编辑</button>
            <div class="xqgl hide">
                <br>
                <input class="profile-uuru" id="id-eidt-weibo" type="text" placeholder="eidt weibo" value="${ w.weibo }">
                <br>
                <button class="weibo-update button-blogs" data-id=${ w.id }>更改</button>
            </div>
            <div class="comment-div hide">
                <form action="/comment" method="post" class="comment-form">
                    <input type="hidden" name="weibo_id" class="profile-uuru" value="${ w.id }">
                    <input name="comment" class="profile-uuru" placeholder="Comment"  style="width: 50%;">
                    <br>
                    <button class="button-blogs"  style="margin: 2px;">发表</button>
                </form>
            </div>
        </div>
    `
    return t
}

var bindEventCommentToggle = function(){
    $('body').on('click', 'a.pylp', function(){
        var weiboCell = $(this).closest(".weibo-cell")
        var weiboComment = weiboCell.find('.comment-div')
        console.log('111', weiboComment)
        weiboComment.slideToggle()
        return false;
    })
}

var bindEventWeiboAdd = function() {
    $('#id-button-weibo-add').on('click', function(){
      var weibo = $('#id-input-weibo').val()
      log('weibo,', weibo)
      var form = {
        weibo: weibo,
      }
      var response = function(r) {
          console.log('成功', arguments)
          log(r)
          if(r.success) {
              console.log('456')
              var w = r.data
              var a = $('.weibo-container')
              $('.weibo-container').prepend(weiboTemplate(w))
              $('#id-input-weibo').val('')
              console.log('123', a)
          } else {
              alert(r.message)
          }
      }

      api.weiboAdd(form, response)
    })
}

var bindEventWeiboDelete = function() {
    $('body').on('click', '.weibo-delete', function(){
      var weiboId = $(this).data('id')
      log(weiboId)
      var weiboCell = $(this).closest('.weibo-cell')

      api.weiboDelete(weiboId, function(response) {
          var r = response
          if(r.success) {
              console.log('成功', arguments)
              $(weiboCell).slideUp()
          } else {
              console.log('错误', arguments)
              alert("删除失败")
          }
      })
    })
}

var bindEventWeiboEdit = function() {
    $('body').on('click', '.weibo-edit', function(){
        var button = $(this)
        var weiboId = $(this).data('id')
        var weiboCell = button.closest('.weibo-cell')
        var weiboContent = weiboCell.find('.weibo-content').text()
        console.log('content', weiboContent)
        var uurukd = weiboCell.find('.xqgl')
        uurukd.slideToggle()

    })
}

var bindEventWeiboUpdate = function() {
    $('body').on('click', '.weibo-update', function(){
        var button = $(this)
        var weiboId = $(this).data('id')
        var weiboCell = button.closest('.weibo-cell')
        var weiboNew = weiboCell.find('#id-eidt-weibo').val()
        var weiboContent = weiboCell.find('.weibo-content')
        console.log('1234', weiboContent, '111', weiboCell.find('.weibo-content'), '222')
        var xqgl = weiboCell.find('.xqgl')
        var form = {
            weibo: weiboNew,
        }

        var response = function(r) {
            if(r.success) {
                console.log('456')
                var w = r.data
                var a = $('.weibo-container')
                console.log('123', a)
                alert("修改成功")
                $(weiboContent.text( weiboNew ))
                $(xqgl).slideUp()
            } else {
                alert(r.message)
            }
        }

        api.weiboUpdate(weiboId, form, response)
    })
}


var bindEvents = function() {
    bindEventCommentToggle()
    bindEventWeiboAdd()
    bindEventWeiboDelete()
    bindEventWeiboEdit()
    bindEventWeiboUpdate()
}

$(document).ready(function(){
    bindEvents()
})
