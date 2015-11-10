var imgNumber = 0;
var currentImgID = 0;
function selectImg(){
    document.getElementById("id_nested-0-image").click();
    $(document).ready(function(){
        $('#id_nested-0-image').change(function(e){
            var fileName = e.target.files[0].name;
            alert('The file "' + fileName +  '" has been selected.');
            $('#select-txt').val(fileName);
        });
    });
}

//setImgInfo except img file url
function setImgInfo() {
    $('#image-Modal').modal('toggle');
    var title = $('#img-title').val();
    var content = $('#img-content').val();
    $('#id_nested-0-title').val(title);
    $('#id_nested-0-content').val(content);

    //clean after close modal
    $('#img-title').val('');
    $('#img-content').val('');
    $('#select-txt').val('');
}
