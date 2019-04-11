$(function(){
    $('#accordian h3').click(function(){
      //Hiding all open accordian
      $(this).parent().parent().find('ul').slideUp();
      // Looking if any ul is not open then slide down accordian
      if(!$(this).next().is(":visible")){
        $(this).next().slideDown();
      }
    })
  })