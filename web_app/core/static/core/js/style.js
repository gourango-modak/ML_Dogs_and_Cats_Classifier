
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
      $(".alert").hide();
      
      var val = $(this).val();
      switch(val.substring(val.lastIndexOf('.') + 1).toLowerCase()){
          case 'gif': case 'jpg': case 'png':
              readURL(this);
              $(".alert").hide();
              break;
          default:
              $(this).val('');
              $(".alert").html("It is not an image file");
              $(".alert").show();
              $("#image_src").attr("src", "");
              break;
      }
    });
    
    $(".alert").hide();
    $("#predict").on('click', function() {
      if ($("#image_data").val() == "") {
        $(".alert").html("Please Input an Image");
        $(".alert").show();
        $('#predict').blur();
      } else {
        $(".main_content").css("filter", "blur(3px)");
        $(".spinner_loader").css("display", "block");
      }
    });
    
    $("#upload_image").submit(function(e) {
      e.preventDefault();
      if ($("#image_data").val() != "") {
        var data = new FormData(this);
        $.ajax({
          url: "image/",
          type: 'POST',
          data: data,
          contentType: false,
          processData: false,
          success: function(result){
            $(".class_label").html(result);
            $(".main_content").css("filter", "blur(0px)");
            $(".spinner_loader").css("display", "none");
            $("#image_data").val('');
            $('#predict').blur();
          }
        });
      }
    
  
    });
});
