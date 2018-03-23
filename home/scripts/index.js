$(function(context) {
   return function() {

      var top_blogs = $('.top_blog_div');
      var recent_blogs = $('.recent_blog_div');
      hover_div(top_blogs);
      hover_div(recent_blogs);
}

}(DMP_CONTEXT.get()))


// function hover_div(divs) {
//
//    divs.mouseenter(function(event) {
//    $(this).addClass('shadow');
//    $(this).addClass('shadow_text');
//    });
//    divs.mouseleave(function(event) {
//    $(this).removeClass('shadow');
//    $(this).removeClass('shadow_text');
//    });
//
//
// }
function hover_div(divs) {

   divs.mouseenter(function(event) {
   $(this).addClass('shadow');
   $(this).find('h3').addClass('shadow_text');
   });
   divs.mouseleave(function(event) {
   $(this).removeClass('shadow');
   $(this).find('h3').removeClass('shadow_text');
   });


}
