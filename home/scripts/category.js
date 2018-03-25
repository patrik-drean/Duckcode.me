$(function(context) {
   return function() {
      var category_div = $('.category_blog_div');
      hover_div(category_div);

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
   $(this).find('.category_name').addClass('shadow_text');
   });
   divs.mouseleave(function(event) {
   $(this).removeClass('shadow');
   $(this).find('h3').removeClass('shadow_text');
   $(this).find('.category_name').removeClass('shadow_text');
   });
}
