var api = {}

api.ajax = function(url, method, form, callback) {
  var request = {
    url: url,
    type: method,
    data: form,
    success: function(response){
        var r = JSON.parse(response)
        callback(r)
    },
    error: function(err){
      var r = {
        'success': false,
        message: '网络错误'
      }
      callback(r)
    }
  }
  console.log('123456')
  $.ajax(request)
}

api.get = function(url, response) {
    api.ajax(url, 'get', {}, response)
}


api.post = function(url, form, response) {
    api.ajax(url, 'post', form, response)
}


api.weiboAdd = function(form, response) {
    var url = '/api/weibo/add'
    api.post(url, form, response)
}

api.weiboUpdate = function(weiboId, form, response) {
    var url = '/api/weibo/update/' + weiboId
    api.post(url, form, response)
    console.log('url', url)
}

api.weiboDelete = function(weiboId, response) {
    var url = '/api/weibo/delete/' + weiboId
    var form = {}
    api.get(url, response)
}
