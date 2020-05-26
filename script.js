$(document).ready(function() {
    // executes when HTML-Document is loaded and DOM is ready
   console.log("document is ready");
     
   
     $( ".card" ).hover(
     function() {
       $(this).addClass('shadow p-3 mb-5 bg-white rounded').css('cursor', 'pointer'); 
     }, function() {
       $(this).removeClass('shadow p-3 mb-5 bg-white rounded');
     }
    );
    $(".search ul li .sub-menu ul li").click(function(){
      console.log("clicked")
    })
});
  