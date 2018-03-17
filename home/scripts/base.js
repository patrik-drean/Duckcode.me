$( window ).load(function() {
  if ($(window).height() > $('#content').height() + $('#navigation').height()) {
    $('.date-footer').css({
      position: 'fixed'
      bottom: 0
    });
  }
});
