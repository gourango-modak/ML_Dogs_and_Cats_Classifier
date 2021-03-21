
$(document).ready(function(){
    function readURL(input) {
        if (input.files && input.files[0]) {
          var reader = new FileReader();
          
          reader.onload = function(e) {
            $('#image_src').attr('src', e.target.result);
          }
          
          reader.readAsDataURL(input.files[0]); // convert to base64 string
        }
    }
    $("#image_data").change(function() {
        readURL(this);
    });
    $("#upload_image").submit(function(e) {
      e.preventDefault();
      // $("#spinner").html('<i class="fas fa-spinner fa-xs"></i>');
      var data = new FormData(this);
      $.ajax({
        url: "image/",
        type: 'POST',
        data: data,
        contentType: false,
        processData: false,
        success: function(result){
          console.log(result);
          $(".class_label").html(result);
        }
      });
    
  
    });
});
