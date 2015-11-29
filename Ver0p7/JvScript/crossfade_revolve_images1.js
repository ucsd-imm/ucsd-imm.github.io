function crossfade_revolve_images(){
   var $current = $('#crossfade_revolver .active');
   var $next = ($current.next().length > 0) ? $current.next() : $('#crossfade_revolver img:first');
   $next.css('z-index', 2); // bring the next image on top of the pile
   $current.fadeOut(1500, function(){ // fade out the top image
      $current.css('z-index', 1).show().removeClass('active'); // reset the z-index and make the image visible
      $next.css('z-index', 3).addClass('active'); // bring the next image to the top
   });
}
