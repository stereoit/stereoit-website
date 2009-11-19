// Emenu v1 - 29 Jan 2009
// by Chris Jaure - http://www.chromasynthetic.com/blog/

(function($){
  $.fn.emenu = function(o){
    
    var options = $.extend($.fn.emenu.defaults, o);
    
    return this.each(function() {
      var menu = $(this).addClass('emenu'),
          first_list = menu.children('ul:first-child'),
          first_list_lis = first_list.children(),
          li_width = Math.floor(parseInt(menu.width(), 10) / first_list_lis.length),
          menu_bg = menu.children('div:first'),
          menu_height = parseInt(menu.height(), 10);
      
      // attach custom events
      $.each(['over', 'out', 'show', 'hide'], function(i, val){
        menu.bind('emenu.'+val, options[val]);
      });
      
      // fire emenu.over and emenu.out on first ul hover
      first_list.hover(
        function() {
          menu.trigger('emenu.over', [menu_bg]);
        },
        function() {
          menu.trigger('emenu.out', [menu_bg]);
        }
      );
      
      first_list_lis.each(function(i){
        var li = $(this),
           second_list = li.children('ul'),
           new_width = 0;
        
        if (i === 0) li.addClass('first-child');
        second_list.children('li:first-child').addClass('first-child');
        
        // calculate the widths of the menu and submenu items
        if (options.autocalc) {
          new_width = li_width - ( parseInt( li.outerWidth({margin: true}), 10 ) - parseInt(li.width(), 10) );
          li.width(new_width);
          
          $.each(options.trim, function(i, val){
            new_width -= parseInt(second_list.css(val), 10);
          });
          second_list.css({
            width: new_width,
            height: menu_height
          });
        }
        
        // fire emenu.show and emenu.hide on menu item hover
        li.hover(
          function(){
            $(this).addClass(options.hoverclass);
            menu.trigger('emenu.show', [second_list, li, new_width, menu_height]);
          },
          function(){
            $(this).removeClass(options.hoverclass);
            menu.trigger('emenu.hide', [second_list, li]);
          }
        );
      });
    });    
  }
  
  $.fn.emenu.defaults = {
    autocalc: true,
    hoverclass: 'hover',
    trim: ['border-left-width', 'margin-left', 'padding-left'],
    over: function(event, bg){
      bg.stop().fadeTo(400, 0.5);
    },
    out: function(event, bg){
      bg.stop().fadeTo(400, 1);
    },
    show: function(event, ul){
      ul.css('visibility', 'visible').stop(true).fadeTo(200, 1);
    },
    hide: function(event, ul){
      ul.stop(true).fadeTo(200, 0, function(){
        ul.css('visibility', 'hidden');
      });
    }
  }
})(jQuery);
