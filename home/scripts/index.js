$(function(context) {
   return function() {

      var top_blogs = $('.top_blog_div');
      var recent_blogs = $('.recent_blog_div');
      var category_div = $('.category_div');
      hover_div(top_blogs);
      hover_div(recent_blogs);
      hover_category_div(category_div);
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

function hover_category_div(divs) {

   divs.mouseenter(function(event) {
   $(this).addClass('category_shadow');
   // $(this).find('.category_name').addClass('category_name_hover');
   });
   divs.mouseleave(function(event) {
   $(this).removeClass('category_shadow');
   // $(this).find('.category_name').removeClass('category_name_hover');
   });
}
