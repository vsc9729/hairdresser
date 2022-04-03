Webcam.set({
    width: 350,
    height: 261,
    image_format:'jpeg',
    jpeg_quality:90,
});
var captured_image;
Webcam.attach("#camera");
function take_snapshot() {
    Webcam.snap(function(data_uri){
        captured_image = data_uri;
        document.getElementById("camera").innerHTML = 
        '<img src = "'+data_uri+'">';
    });
}
$("#retake-button").click(function(){
    $("#camera").innerHTML = '';
    Webcam.attach("#camera");
});
$("#result-button").click(async function(){
    await $.ajax({
        url: "/process",
        data:{
            base64Image: captured_image
        },
        type: "POST",
        success: function(response){
            window.location.replace(response);
            console.log('received');
        }
    });
});
