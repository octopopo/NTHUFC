var imgNumber = 0;
var currentImgID = 0;
var nameset = '';
var fileName = '';
var firstfile = true;
//check img number whether exceed 5
function checkImgNumber() {
    if(imgNumber <= 4){
        $('#image-Modal').modal('toggle');
    }
    else{
        $('#msg-Modal').modal('show');
        $('#msg-txt').text('Max photo number is five!');
    }
}

function selectImg(){
    document.getElementById('id_nested-'+currentImgID+'-image').click();
    $(document).ready(function(){
        $('#id_nested-'+currentImgID+'-image').change(function(e){
            fileName = e.target.files[0].name;
            alert('The file "' + fileName +  '" has been selected.');
            $('#select-txt').val(fileName);
        });
    });
}

//setImgInfo except img file url
function setImgInfo() {
    $('#image-Modal').modal('toggle');
    var title = $('#img-name').val();
    var content = $('#img-content').val();
    $('#id_nested-'+currentImgID+'-title').val(title);
    $('#id_nested-'+currentImgID+'-content').val(content);

    //clean after close modal
    $('#img-name').val('');
    $('#img-content').val('');
    $('#select-txt').val('');
    imgNumber = imgNumber + 1;
    currentImgID = currentImgID + 1;
    $('#img-number').text('Number of upload image: '+imgNumber);

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
}

function resetPopup(){
    //clean img modal
    document.getElementById("popup-img-form").reset();

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
}

//check img number whether is 0
function submitCheck(){
    if(imgNumber == 0){
        $('#msg-Modal').modal('show');
        $('#msg-txt').text('At least submit one photo!');
        return false;
    }
}

