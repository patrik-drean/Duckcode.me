$(function(context) {
   return function() {


      var top_blogs = $('.top_blog_div');
      var recent_blogs = $('.recent_blog_div');
      hover_div(top_blogs);
      hover_div(recent_blogs);


}

}(DMP_CONTEXT.get()))


function hover_div(divs) {

   divs.mouseenter(function(event) {

   main_img.attr('src', this.src);
   });



}
