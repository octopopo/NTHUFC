var imgNumber = 0;
var currentImgID = 0;
var nameset = '';
var fileName = '';
var firstfile = true;
var page;
var google_map;
var markerList = [];

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
            $('#image-Modal').on('shown.bs.modal', function () {
                //google.maps.event.trigger(google_map, "resize");
                initMap();
            });
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
        var tags_text = $('#img-tags').val()
        var location_text = $('#img-location').val();

        $('#id_nested-'+currentImgID+'-title').val(title);
        $('#id_nested-'+currentImgID+'-content').val(content);
        $('#id_nested-'+currentImgID+'-tags').val(tags_text);
        $('#id_nested-'+currentImgID+'-location_marker').children().each(function(){
            console.log($(this).text())
            if ($(this).text() == location_text){
                $(this).attr("selected", true);
            }
        });
        //clean after close modal
        $('#img-title').val('');
        $('#img-content').val('');
        $('#img-tgs').val('')
        $('#img-location').val('');
        $('#select-txt').val('');
        //clean the preview img
        document.getElementById("preview_img").src = "#";
        document.getElementById("preview_img").style.display = "none";

        changeValidationError('title', 'correct');
        changeValidationError('content', 'correct');
        changeValidationError('tags', 'correct');
        changeValidationError('location', 'correct');
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

    console.log(/^[^ ]{1,10}( [^ ]{1,10}){0,2}$/.test($('#img-tags').val()))
    if(/^[^ ]{1,10}( [^ ]{1,10}){0,2}$/.test($('#img-tags').val())){
        changeValidationError('tags', 'correct');
    }
    else{
        changeValidationError('tags', 'wrong');
        valid = false;
    }

    isLocationValid = false;
    for (i in markerList){
        if (markerList[i].title == $('#img-location').val() ){
            isLocationValid = true;
            break;
        }
    }

    if(isLocationValid == false){
        changeValidationError('location', 'wrong');
        valid = false;
    }
    else
        changeValidationError('location', 'correct');

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
    else if(field == 'tags'){
        if(status == 'wrong'){
            $('#popup-img-form .form-group:eq(2)').addClass('has-error');
            $('#popup-img-form .asteriskField:eq(2)').html('請輸入1~3個標籤(每個最多10個字)，兩個標籤之間要有1個空白').css("color","#f04124");
        }
        else{
            $('#popup-img-form .form-group:eq(2)').removeClass('has-error');
            $('#popup-img-form .asteriskField:eq(2)').html('*').css("color","#222222");
        }
    }
    else if(field == 'location'){
        if(status == 'wrong'){
            $('#popup-img-form .form-group:eq(3)').addClass('has-error');
            $('#popup-img-form .asteriskField:eq(3)').css("color","#f04124");
        }
        else{
            $('#popup-img-form .form-group:eq(3)').removeClass('has-error');
            $('#popup-img-form .asteriskField:eq(3)').css("color","#222222");
        }
    }
    else if(field == 'txt'){
        if(status == 'wrong'){
            $('#popup-img-form .form-group:eq(4)').addClass('has-error');
            $('#popup-img-form .asteriskField:eq(4)').css("color","#f04124");
        }
        else{
            $('#popup-img-form .form-group:eq(4)').removeClass('has-error');
            $('#popup-img-form .asteriskField:eq(4)').css("color","#222222");
        }
    }
}

function initMap() {
    var myLatLng = {lat: 24.7913341, lng: 120.994148};

    var mapOptions = {
        zoom: 16,
        center: myLatLng,
    };
    google_map = new google.maps.Map(document.getElementById('google_map'),mapOptions);
    for ( i in markerList){
        addMarker(google_map, markerList[i].title, {lat: markerList[i].lat, lng: markerList[i].lng})
    }
    console.log('google map loading finish')
}

function addMarker(map, title, location){
    var marker = new google.maps.Marker({
        position: location,
        map: map,
        label: title,
        title: title,
    });

    marker.addListener('click', function() {
        $('#img-location').val(marker.title)
        google_map.setCenter(marker.getPosition())
    });
}

function initMarker(markers){
    markerList = markers
}