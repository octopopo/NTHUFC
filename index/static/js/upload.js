var imgNumber = 0;
var currentImgID = 0;
var nameset = '';
var fileName = '';
var firstfile = true;
var page;

function init(number, page_name){
    imgNumber = number;
    currentImgID = number;
    page = page_name;
}
//check img number whether exceed 5
function checkImgNumber(action) {
    if(action == 'upload'){
        if(imgNumber <= 4){
            $('#image-Modal').modal('toggle');
        }
        else{
            showMsgModal('Max photo number is five!');
        }
    }
    else if(action == 'submit'){
        if(imgNumber == 0){
            showMsgModal('At least submit one photo!');
            return false;
        }
        showMsgModal('Photos are uploading...');
    }
}

//click the hidden input type="file"
function selectImg(){
    document.getElementById('id_nested-'+currentImgID+'-image').click();
}
//accept the input file change event
$(document).ready(function(e) {
    //$('#div_id_nested-'+currentImgID+'-image').find("input").change(function(e){
    $('.controls .clearablefileinput').change(function(e){
        fileName = e.target.files[0].name;
        alert('The file "' + fileName + '" has been selected.');
        $('#select-txt').val(fileName);
        readURL(this);
    });
});
//read URL to show the preview image
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            document.getElementById("preview_img").style.display = "block";
            $('#preview_img').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}

//setImgInfo except img file url
function setImgInfo() {
    //check modal form
    var valid = validationError();
    if(valid == false){
        return false;
    }
    else {
        $('#image-Modal').modal('toggle');
        var title = $('#img-title').val();
        var content = $('#img-content').val();
        $('#id_nested-'+currentImgID+'-title').val(title);
        $('#id_nested-'+currentImgID+'-content').val(content);

        //clean after close modal
        $('#img-title').val('');
        $('#img-content').val('');
        $('#select-txt').val('');
        //clean the preview img
        document.getElementById("preview_img").src = "#";
        document.getElementById("preview_img").style.display = "none";

        changeValidationError('title', 'correct');
        changeValidationError('content', 'correct');
        changeValidationError('txt', 'correct');


        imgNumber = imgNumber + 1;
        currentImgID = currentImgID + 1;
        $('#img-number').text('Number of upload image: ' + imgNumber);

        //fill-in nameset
        if(!firstfile){
            document.getElementById("img-nameset").rows = document.getElementById("img-nameset").rows + 1;
            nameset = $('#img-nameset').val();
            $('#img-nameset').val(nameset + '\n' + imgNumber + '. ' + fileName);
        }
        else{
            $('#img-nameset').val(imgNumber + '. ' + fileName);
            firstfile = !firstfile;
        }

        //profile page
        if(page == 'profile'){
            document.getElementById('profile_update').click();
        }

    }
}

function resetModalForm(){
    //clean img modal
    document.getElementById("popup-img-form").reset();

    //clean the preview img
    document.getElementById("preview_img").src = "#";
    document.getElementById("preview_img").style.display = "none";
    //clean the actual img url
    $('#id_nested-'+currentImgID+'-image').val('');
}

function resetParticipateForm(){
    imgNumber = 0;
    currentImgID = 0;
    $('#img-number').text('Number of upload image: '+imgNumber);
    //reset nameset
    $('#img-nameset').val('');
    document.getElementById("img-nameset").rows = 1;

    //reset upload-img-btn name
    $('#upload-btn').val('上傳');

    firstfile = true;
}

//modal form validationerror
function validationError(){
    var valid = true;
    if($('#img-title').val() == ''){
        changeValidationError('title', 'wrong');
        valid = false;
    }
    else
        changeValidationError('title', 'correct');


    if($('#img-content').val() == ''){
        changeValidationError('content', 'wrong');
        valid = false;
    }
    else
        changeValidationError('content', 'correct');

    if($('#select-txt').val() == ''){
        changeValidationError('txt', 'wrong');
        valid = false;
    }
    else
        changeValidationError('txt', 'correct');

    return valid;
}

function changeValidationError(field, status){
    if(field == 'title'){
        if(status == 'wrong'){
            $('#popup-img-form .form-group:eq(0)').addClass('has-error');
            $('#popup-img-form .asteriskField:eq(0)').css("color","#f04124");
        }
        else{
            $('#popup-img-form .form-group:eq(0)').removeClass('has-error');
            $('#popup-img-form .asteriskField:eq(0)').css("color","#222222");
        }
    }
    else if(field == 'content'){
        if(status == 'wrong'){
            $('#popup-img-form .form-group:eq(1)').addClass('has-error');
            $('#popup-img-form .asteriskField:eq(1)').css("color","#f04124");
        }
        else{
            $('#popup-img-form .form-group:eq(1)').removeClass('has-error');
            $('#popup-img-form .asteriskField:eq(1)').css("color","#222222");
        }
    }
    else if(field == 'txt'){
        if(status == 'wrong'){
            $('#popup-img-form .form-group:eq(2)').addClass('has-error');
            $('#popup-img-form .asteriskField:eq(2)').css("color","#f04124");
        }
        else{
            $('#popup-img-form .form-group:eq(2)').removeClass('has-error');
            $('#popup-img-form .asteriskField:eq(2)').css("color","#222222");
        }
    }
}

