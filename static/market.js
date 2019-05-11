console.log('test');
function chageImage(image) {                              
    document.getElementById('main-image').innerHTML = ''; //span같은 태그 밸류 삭제 코드
    var str = ('<img src="'+image+'" width=500 height=500 />');
    $('#main-image').append(str);
}

function addReCommentForm(comment_id, category) {
    /* form 태그를 만들어주고 속성을 부여한다*/
    var a = document.createElement("form");
    a.setAttribute('method', 'POST');
    a.setAttribute('action', '/market/'+category+'/addrecomment/'+comment_id);
    a.setAttribute('id', 'reComment'+comment_id);
    /* 댓글 입력값을 받는 input field를 만든다 */
    var b = document.createElement("input");
    b.type = "text";
    b.name = "text";
    /* submit 버튼을 만든다 */
    var c = document.createElement("input");
    c.type = "submit";
    c.value = "작성";
    /* csrftoken을 부여한다. */
    var d = document.createElement("input");
    d.setAttribute('name', 'csrfmiddlewaretoken');
    d.setAttribute('value', '{{ csrf_token }}');
    d.type = "hidden";
    /* 만들어진 필드들을 폼에 넣는다 */
    a.appendChild(b);
    a.appendChild(c);
    a.appendChild(d);
    /* 만들어진 폼을 지정된 위치에 넣는다 */
    document.getElementById(comment_id+'recomment').appendChild(a);
}

/* Ajax를 이용한 댓글 달기 */
$('.addComment').click(function() {
    // $('#commentForm').submit(function(event) {
    //     event.preventDefault();
    $.ajax ({
        type: "POST",
        url: "/market/book/addcomment/"+postid,
        cache: false,
        data:  $('#commentBody').serialize(),
        dataType: 'json',
        success  : function(data){
            // $('#commentList').append(data+"<br>");
            for(var count in data)
            {
                count++;
            }
            $('#commentList').remove();
            $('#commentBlock').append('<div id=commentList>', '</div>');
            for(let i = 0; i < count; i++)
            {
                if (data[i].parent_id == null) {
                    var commentid = data[i].id;
                    $('#commentList').append(data[i].body + ' <button id='+ commentid +'"reComment" onclick="'+ 'addReComment(' + commentid + ');"> 댓글달기 </button>' +'<br>'
                    , '<div id="' + commentid + 'recomment"></div>');
                } else {
                    $('#'+ data[i].parent_id + 'recomment').append('ㄴ' + data[i].body);
                }
            }
            $('#commentForm input').val('');
            },
        error: function (xhr, status) {
            alert("Sorry, there was a problem!");
            }
    });
    return false;
// });
});