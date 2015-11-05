var ID;
function fileup(id){
  var fileup = document.getElementById("fileupload");
  file.click();
  ID = id;
}
function change(input){
    var file = document.getElementById("file"),
    fileup = document.getElementById("fileupload");
    fileup.value = fileup.value + file.value + ' ';
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#img' + ID)
                .attr('src', e.target.result);
                //.width(150)
                //.height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
    $("#glyphicon" + ID).css({"display": "none"});
    $("#col" + ID).css({"border": "0px"});
    $("#img" + ID).css({"display": "block"});
}
function cancel(){
    for(var i=1; i<=4; i++){
        $("#glyphicon" + i).css({"display": "block"});
        $("#col" + i).css({"border": "6px dashed #ccc"});
        $("#img" + i).css({"display": "none"});
        $("#img" + i).attr("src","#");
    }
}
